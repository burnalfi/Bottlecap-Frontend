from django.shortcuts import render, redirect

from django.http import HttpResponse

import requests

def login(request):
    return render(request, 'main/login.html', {})

def logout(request):
    if request.session.has_key('user'):
        request.session.flush()
        
    return redirect('/main/login/')

def register(request):
    return render(request, 'main/register.html', {})

def register_personal(request):
    return render(request, 'main/regpersonal.html', {})

def register_organization(request):
    return render(request, 'main/regorganization.html', {})

def order(request):
    if 'user' in request.session:
        usersesh = request.session['user']
        return render(request, 'main/order.html', {})

    else:    
        return redirect('/main/login/')

def orders(request):
    if 'user' in request.session:
        usersesh = request.session['user']
        return render(request, 'main/orders.html', {})
    
    else:
        return redirect('/main/login/')
    
def home(request):
    return render(request, 'main/home.html', {})

def parse(request):
    Register = request.POST.get('register')
    RegNext = request.POST.get('next')
    RegPersonal = request.POST.get('personal sign up')
    RegOrganization = request.POST.get('organization sign up')
    Login = request.POST.get('login')
    Logout = request.POST.get('logout')
    Order = request.POST.get('order')

    if(Register == 'Register'):
        return redirect("/main/register/")

    if(RegNext == 'Next'):
        
        Customer = request.POST.get('customer')
        
        if(Customer == 'Personal'):
            return redirect("/main/register/personal/")

        elif(Customer == 'Organization'):
            return redirect("/main/register/organization/")

        else:
            return HttpResponse("<h1>Didn't Work</h1>")

    if(RegPersonal == 'Sign Up'):
        
        personal_full_name = request.POST.get('personal_full_name')
        personal_phone_number = request.POST.get('personal_phone_number')
        personal_email = request.POST.get('personal_email')
        personal_password = request.POST.get('personal_password')
        personal_conf_password = request.POST.get('personal_confpassword')
        
        if(personal_conf_password == personal_password):
            
            data = {'personal_phone_number' : personal_phone_number, 'personal_email' : personal_email, 'personal_password' : personal_password,
                    'personal_full_name' : personal_full_name, 'personal_city' : '', 'personal_address' : '', 'personal_postal_code' : ''}
                
            r = requests.post('http://127.0.0.1:5000/register/personal', data = data)

            if(r.status_code == 200):
                return redirect("/main/login/")

            elif(r.status_code == 400 | r.status_code == 500):
                return redirect("/main/register/personal/")
                
            else:
                return redirect("/main/register/personal/")          
            

        else:
            return redirect("/main/register/personal/")

        return redirect("/main/register/personal/")

    if(RegOrganization == 'Sign Up'):
        organization_name = request.POST.get('organization_name')
        repr_phone_number = request.POST.get('repr_phone_number')
        repr_email = request.POST.get('repr_email')
        repr_password = request.POST.get('repr_password')
        repr_confpassword = request.POST.get('repr_confpassword')
        repr_full_name = request.POST.get('repr_full_name')

        if(repr_password == repr_confpassword):
            
            data = {'organization_name' : organization_name, 'repr_phone_number' : repr_phone_number, 
                    'repr_email' : repr_email, 'repr_password' : repr_password, 'repr_full_name' : repr_full_name, 
                    'organization_address' : '', 'organization_city' : '', 'organization_postal_code' : ''}

            r = requests.post('http://127.0.0.1:5000/register/organization', data = data)

            if(r.status_code == 200):
                return redirect('/main/login/')

            elif(r.status_code == 400 | r.status_code == 500):
                return redirect ('/main/login/')
            
            else:
                return redirect('/main/login/')
        else:
            return redirect('/main/register/organization/')
        
        return redirect('main/register/personal/')

    if(Login == 'Login'):
        log_email = request.POST.get('credential_input')
        log_password = request.POST.get('password_input')

        credentials = {'email' : log_email, 'password' : log_password}

        r = requests.post('http://127.0.0.1:5000/login', data = credentials)

        if(r.json()['status'] == True):
            request.session['user'] = r.json()['session_id']
            return redirect("/main/order/")
        
        return redirect("/main/login/")

    if(Order == 'Order'):
        return redirect("/main/orders/")
        
        
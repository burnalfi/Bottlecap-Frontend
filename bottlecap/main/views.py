from django.shortcuts import render, redirect

from django.http import HttpResponse

import requests

def about(request):
    return render(request, 'main/about.html', {})

def cart(request):
    return render(request, 'main/cart.html', {})

def contact(request):
    return render(request, 'main/contact.html', {})

def home(request):
    return render(request, 'main/index.html', {})

def login(request):
    return render(request, 'main/login.html', {})

def logout(request):
    if request.session.has_key('user'):
        request.session.flush()
        
    return redirect('/main/login/')

def product(request):
    return render(request, 'main/product.html', {})

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

        
def register(request):
    return render(request, 'main/register.html', {})

def register_personal(request):
    return render(request, 'main/regpersonal.html', {})

def register_organization(request):
    return render(request, 'main/regorganization.html', {})

def term(request):
    return render(request, 'main/term.html', {})
    

def parse(request):
    Register = request.POST.get('register')
    RegNext = request.POST.get('next')
    RegPersonal = request.POST.get('personal sign up')
    RegOrganization = request.POST.get('organization sign up')
    Login = request.POST.get('login')
    Logout = request.POST.get('logout')
    Order = request.POST.get('order')
    Proceed = request.POST.get('proceed to checkout')

    if(Register == 'Register'):
        return redirect("/main/register/")


    if(RegPersonal == 'Sign Up Personal'):
        
        personal_full_name = request.POST.get('personal_full_name')
        personal_phone_number = request.POST.get('personal_phone_number')
        personal_email = request.POST.get('personal_email')
        personal_password = request.POST.get('personal_password')
        personal_conf_password = request.POST.get('personal_confpassword')
        personal_address = request.POST.get('personal_address')
        personal_city = request.POST.get('personal_city')
        personal_postal_code = request.POST.get('personal_postal_code') 
        
        if(personal_conf_password == personal_password):
            
            data = {'personal_phone_number' : personal_phone_number, 'personal_email' : personal_email, 'personal_password' : personal_password,
                    'personal_full_name' : personal_full_name, 'personal_city' : personal_city, 'personal_address' : personal_address, 'personal_postal_code' : personal_postal_code}
                
            r = requests.post('http://127.0.0.1:5000/register/personal', data = data)

            if(r.status_code == 200):
                return redirect("/main/login/")

            elif(r.status_code == 400 | r.status_code == 500):
                return redirect("/main/register/")
                
            else:
                return redirect("/main/register/")          
            

        else:
            return redirect("/main/register/")

        return redirect("/main/register/")

    if(RegOrganization == 'Sign Up Organization'):
        organization_name = request.POST.get('organization_name')
        organization_address = request.POST.get('organization_address')
        organization_city = request.POST.get('organization_city')
        organization_postal_code = request.POST.get('organization_postal_code')
        repr_phone_number = request.POST.get('repr_phone_number')
        repr_email = request.POST.get('repr_email')
        repr_password = request.POST.get('repr_password')
        repr_confpassword = request.POST.get('repr_confpassword')
        repr_full_name = request.POST.get('repr_full_name')

        if(repr_password == repr_confpassword):
            
            data = {'organization_name' : organization_name, 'repr_phone_number' : repr_phone_number, 
                    'repr_email' : repr_email, 'repr_password' : repr_password, 'repr_full_name' : repr_full_name, 
                    'organization_address' : organization_address, 'organization_city' : organization_city, 'organization_postal_code' : organization_postal_code}

            r = requests.post('http://127.0.0.1:5000/register/organization', data = data)

            if(r.status_code == 200):
                return redirect('/main/login/')

            elif(r.status_code == 400 | r.status_code == 500):
                return redirect ('/main/register/')
            
            else:
                return redirect('/main/register/')
        else:
            return redirect('/main/register/')
        
        return redirect('main/register/')

    if(Login == 'Login'):
        log_email = request.POST.get('credential_input')
        log_password = request.POST.get('password_input')

        credentials = {'email' : log_email, 'password' : log_password}

        r = requests.post('http://127.0.0.1:5000/login', data = credentials)

        if(r.json()['status'] == True):
            request.session['user'] = r.json()['session_id']
            return redirect("/main/cart/")
        
        return redirect("/main/login/")

    if(Order == 'Order'):
        return redirect("/main/orders/")

    if (Proceed == 'Proceed To Checkout'):
        if('user' in request.session):
            quantity = request.POST.get('quantity')
            print(quantity)
            return redirect("/main/home/")

        else:
            return redirect("/main/login/")
            
        
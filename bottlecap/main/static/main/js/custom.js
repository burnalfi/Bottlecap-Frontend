$("#main-form").hide();
$("#personal_form").hide();
$("#organization_form").hide();

$(document).ready(function(){
	$("#personal_selected").click(function(){
		$("#selection").hide(500);
		$("#main-form").show(500);
		$(".selection_sm").removeClass('bg-success text-white');
		$("#organization_selected_sm").addClass('bg-default');
		$("#personal_selected_sm").addClass('bg-success text-white');
		$("#organization_form").hide();
		$("#personal_form").show(500);
	});

	$("#organization_selected").click(function(){
		$("#selection").hide(500);
		$("#main-form").show(500);
		$(".selection_sm").removeClass('bg-success text-white');
		$("#personal_selected_sm").addClass('bg-default');
		$("#organization_selected_sm").addClass('bg-success text-white');
		$("#personal_form").hide();
		$("#organization_form").show(500);
	});

	$("#personal_selected_sm").click(function(){
		$(".selection_sm").removeClass('bg-success text-white');
		$("#organization_selected_sm").addClass('bg-default');
		$("#personal_selected_sm").addClass('bg-success text-white');
		$("#organization_form").hide();
		$("#personal_form").show(500);
	});

	$("#organization_selected_sm").click(function(){
		$(".selection_sm").removeClass('bg-success text-white');
		$("#personal_selected_sm").addClass('bg-default');
		$("#organization_selected_sm").addClass('bg-success text-white');
		$("#personal_form").hide();
		$("#organization_form").show(500);
	});
});
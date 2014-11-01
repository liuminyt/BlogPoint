$(document).ready(function(){
	$("#menu li").mouseover(function(){
		$(this).css("background", "#ec23ba");
	}).mouseout(function(){
		$(this).css("background", "none");
	});


	$("#menu").css("height", $(window).height());
	$("#showPic").css("height", $(window).height());

	$(window).resize(function(){
		$("#menu").css("height", $(window).height());
		$("#showPic").css("height", $(window).height());
	});
})
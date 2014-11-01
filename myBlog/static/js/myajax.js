$(document).ready(function(){
	$(".likeit").click(function(){
		var article_id;
		var elem = $(this);
		$(this).animate({
			opacity: '0.7'
		});
		article_id = elem.attr("data-article_id");
		$.get("/blog/likeit/"+article_id+"/", function(likecount){
			elem.html("<img src='/static/img/like.png'> &nbsp; " + likecount);
			elem.animate({ opacity: '1'})
		});
	});
});

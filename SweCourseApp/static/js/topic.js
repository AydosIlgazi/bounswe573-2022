
  $(document).ready(function () {
	$( "#addResource" ).hide();
	$( "#addResourceButton" ).click(function() {
		$( "#addResource" ).toggle();
	  });
	  $('.comment').click(function() {
		$(this).parent().parent().parent().children().eq(1).toggle();
	  });

	  $('.like').click(function() {
		likeResource($(this).attr('value'),$(this).children().eq(0) );
	  });    
  });



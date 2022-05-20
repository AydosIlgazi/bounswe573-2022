
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

	  $( "#add-note" ).click(function() {
		$( ".add-note" ).toggle();
	  });
	  $( "#my-notes" ).click(function() {
		$( ".my-notes" ).toggle();
	  });
	  $( "#other-notes" ).click(function() {
		$( ".other-notes" ).toggle();
	  });
	  $( "#close-mynotes" ).click(function() {
		$( ".my-notes" ).hide();
	  });
	  $( "#close-othernotes" ).click(function() {
		$( ".other-notes" ).hide();
	  });
	  $( "#note-close" ).click(function() {
		$( ".add-note" ).hide();
	  });
	  

  });



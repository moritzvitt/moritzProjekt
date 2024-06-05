$(document).ready(function() {
    $('.collapse').on('show.bs.collapse', function() {
      var openedCollapse = $('.collapse.show'); // Find the currently opened collapse element
      openedCollapse.collapse('hide'); // Hide the previously opened collapse
    });
  });
  

  $(document).ready(function() {
    $('.navbar-brand').mouseenter(function() { // Mouse enter
      $('.animate-item').each(function(i) {
        setTimeout(function() {
          $('.animate-item').eq(i).addClass('show');
        }, 100 * (i+1));
      });
    });
  
    $('nav.navbar').mouseleave(function() { // Mouse leave
      $('.animate-item').removeClass('show');
    });
  });

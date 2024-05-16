$(document).ready(function() {
    $('.collapse').on('show.bs.collapse', function() {
      var openedCollapse = $('.collapse.show'); // Find the currently opened collapse element
      openedCollapse.collapse('hide'); // Hide the previously opened collapse
    });
  });
  
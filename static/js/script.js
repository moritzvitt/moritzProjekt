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

  $(document).ready(function() {
    // Function to update the visibility of divs in div_values.html
    function updateDivVisibility() {
        ['hint', 'test', 'synonyms', 'explanation', 'definition', 'first_example', 'second_example', 'grammar', 'conjugation', 'translation'].forEach(function(id) {
            var displayStyle = localStorage.getItem('display-' + id) || 'none';
            $('#' + id).css('display', displayStyle);
        });
    }

    // Checks if it's running on the div_values.html
    if ($('.box').length > 0) {
        updateDivVisibility(); // Initial visibility update
        window.addEventListener('storage', updateDivVisibility); // Listen for changes
    }

    // Checks if it's running on the list.html
    if ($('#tickedFieldsCheckboxes').length > 0) {
        $('input[type="checkbox"]').change(function() {
            var checkboxId = $(this).attr('id');
            var targetId = checkboxId.replace('Checkbox', '');
            var isChecked = $(this).is(':checked');

            // Send a message to div_values.html through localStorage
            localStorage.setItem('display-' + targetId, isChecked ? 'block' : 'none');
            // Trigger an event to notify div_values.html page
            window.dispatchEvent(new Event('storage'));
        });
    }
});


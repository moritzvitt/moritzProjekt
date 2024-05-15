// Array of language codes and their corresponding names
var languages = [
    { code: "en", name: "English" },
    { code: "fr", name: "French" },
    { code: "es", name: "Spanish" },
    { code: "de", name: "German" },
    { code: "it", name: "Italian" },
    { code: "pt", name: "Portuguese" },
    { code: "nl", name: "Dutch" },
    { code: "pl", name: "Polish" },


    // Add more languages as needed
];

var selectLanguage = document.getElementById("languageSelect");

// Loop through the languages array and create options for language selection
languages.forEach(function(language) {
    var option = document.createElement("option");
    option.value = language.code;
    option.textContent = language.name;
    selectLanguage.appendChild(option);
});

// Array of wanted fields
var wantedFields = [
    "synonyms",
    "test",
    "first example",
    "second example",
    "explanation",
    "hint",
    "definition",
    "grammar",
    "conjugation",
    "long_test_message"
  ];
  
  var checkboxesContainer = document.getElementById("wantedFieldsCheckboxes");
    
  // Loop through the wantedFields array and create checkboxes
  wantedFields.forEach(function(field) {
    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = field;
    checkbox.name = "wantedFields";
    checkbox.value = field;
  
    var label = document.createElement("label");
    label.htmlFor = field;
    label.appendChild(document.createTextNode(field));
  
    checkboxesContainer.appendChild(checkbox);
    checkboxesContainer.appendChild(label);
    checkboxesContainer.appendChild(document.createElement("br"));
  });
  
//   window.onload = function() {
//     document.getElementById('submit').addEventListener('click', function(event) {
//       var fileUpload = document.getElementById('fileUpload');
//       if (!fileUpload.value) {
//         event.preventDefault();
//         // Load test data frame
//         fetch('/Users/moritzvitt/src/LR2Anki/test_dataframes/jn_items.csv')
//           .then(response => response.text())
//           .then(data => {
//             // Do something with the data
//             console.log(data);
//           })
//           .catch(error => console.error(error));
//       }
//     });
// };

window.onload = function() {
  document.getElementById('fileUpload').addEventListener('change', function(event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function(e) {
          var contents = e.target.result;
          var lines = contents.split('\n');
          var html = '<table class="table">';
          lines.forEach(function(line) {
              html += '<tr>';
              var cells = line.split(',');
              cells.forEach(function(cell) {
                  html += '<td>' + cell + '</td>';
              });
              html += '</tr>';
          });
          html += '</table>';
          document.getElementById('uploadedDataframe').innerHTML = html;
      };
      reader.readAsText(file);
  });
};
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
  
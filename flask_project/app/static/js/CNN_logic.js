// Select all the interactive  elements in the html
let imageButton = d3.select("#imageButton");
let revealButton = d3.select('#revealButton');
let dropdown = d3.select('.dropdownMenu');
let image = d3.select('#xrayimage');

let userScore  = d3.select('#counter1');
let modelScore  = d3.select('#counter2');


var imageID = null;
var actualResult = null;
var modelResult = null;

function changeImage(imageSrc) {
    image.attr('src', imageSrc);
};

function createImage() {
    //get random image
    fetch('/api/v1/images/randomone')
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        const imageData = data.image_data;
        const mimeType = data.mime_type;
        actualResult = data.choice;
        imageID = data.image_id;
        // Create an img URL and call changeImage to set the src to the base64 image data
        const dataUrl = `data:${mimeType};base64,${imageData}`;
        changeImage(dataUrl);
    })
    .catch(error => console.error('Error fetching image:', error));
};

function modelPredict(imageID, actualResult){
    fetch('/api/v1/images/predict/' + imageID + '/' + actualResult)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        modelResult = data.model;
    });
}
//enable dropdown after image has been generated and disable after:
function enableDropdown() {
    dropdown.attr('disabled', null);
    };

function disableDropdown(){
    dropdown.attr('disabled', true);
};

// enable diagnosis after user has guessed and then disable after:
function enableReveal(){
    revealButton.attr('disabled', null);
};

function disableReveal(){
    revealButton.attr('disabled', true);
};

// reset to how it was before image generated, except for score
function reset(){
    dropdown.property('value', 'option1');
};

//Generating an image makes all other aspects of the code run
// generate new image
imageButton.on('click', function(){

        createImage();
        modelPredict(imageID, actualResult);
        enableDropdown();
        reset();

    var userSelects = '';

    // update model guess, after user selects from dropdown
    dropdown.on('change', function(){
        userSelects = dropdown.select('option:checked').text();
        disableDropdown();
        enableReveal();
    });

    // reveal model guess
    revealButton.on('click', function(){
    
      if (userSelects == actualResult){
        let currentScore = parseInt(userScore.text()) + 1;
        userScore.text(currentScore);
      };

      if (modelResult == actualResult){
        let currentScoreModel = parseInt(modelScore.text()) + 1;
        modelScore.text(currentScoreModel);
      };
      disableReveal();

    });

});
// Select all the interactive  elements in the html
let imageButton = d3.select(".imageButton");
let revealButton = d3.select('.revealButton');
let dropdown = d3.select('.dropdownMenu');
let modelGuess = d3.select('#text');
let image = d3.select('#image');

let diagnosis = d3.select('.diagnosis')
let userScore  = d3.select('#counter1');
let modelScore  = d3.select('#counter2');


//get random image source 

// find what model predicts from image 
var prediction = 'Pneumonia'

// change image based off input source and store the result (actual diagnosis)
var result = ''

function changeImage(imageSrc) {
    image.attr('src', imageSrc);
    result = 'Pneumonia'
};

//enable dropdown after image has been generated and disable after:
function enableDropdown() {
    dropdown.attr('disabled', null);
    };

function disableDropdown(){
    dropdown.attr('disabled', true)
};

// enable diagnosis after user has guessed and then disable after:
function enableReveal(){
    revealButton.attr('disabled', null);
};

function disableReveal(){
    revealButton.attr('disabled', true)
}

// reset to how it was before image generated, except for score
function resetAll(){
    modelGuess.text('Waiting for your guess...')
    diagnosis.text('');
    dropdown.property('value', 'option1')
};

//Generating an image makes all other aspects of the code run
// generate new image
imageButton.on('click', function(){

        changeImage('test/PNEUMONIA/person8_virus_27.jpeg')

        enableDropdown();
        resetAll();

    var userSelects = ''

    // update model guess, after user selects from dropdown
    dropdown.on('change', function(){
        userSelects = dropdown.select('option:checked').text();
        disableDropdown();
        modelGuess.text(prediction);
        enableReveal();
    });

    // reveal model guess
    revealButton.on('click', function(){
        diagnosis.text(result)

      if (userSelects == result){
        let currentScore = parseInt(userScore.text()) + 1
        userScore.text(currentScore)
      };

      if (prediction == result){
        let currentScoreModel = parseInt(modelScore.text()) + 1
        modelScore.text(currentScoreModel)
      };
      disableReveal()

    });

});
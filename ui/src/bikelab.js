var openjscad = require('@jscad/openjscad/src/ui/min.js');

var bikelab = {
  'gProcessor': null,
  'debug_callback': function(message) {
    console.log(message);
  }
}

document.addEventListener('DOMContentLoaded', function (event) {
  bikelab.gProcessor = openjscad.init();
  window.bikelab = bikelab;
})

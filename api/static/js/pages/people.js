/* global Mustache $ */
var stuSpin = $("#numStu")
  .TouchSpin( {
    verticalbuttons: true,
    min: 1,
    step: 1,
    initval: 1
  });

var collabSpin = $("#numCollab")
  .TouchSpin( {
    verticalbuttons: true,
    min: 0,
    max: 4,
    step: 1,
    initval: 0
  });


api = urcpp("v1")

// In
   
/* global api, username */

var prevSpin = 0;

/* global Mustache */
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
    step: 1,
    initval: 0
  });

collabSpin.on("change", function () {
  var spin = $("#numCollab").val();
  var dir  = 0;
  
  if (spin > prevSpin) {
    var tmpl = $("#collabInputT").html();
    var view = { "count": spin, "id" : "" + spin - 1};
    var rendered = Mustache.render(tmpl, view);
    console.log("> spin: " + spin + " prev: " + prevSpin);
    $("#moreCollaborators").append(rendered);
  } else {
    if (prevSpin > 0) {
      
      var removeMe = "#cgroup" + (prevSpin - 1); 
      console.log("Removing: " + removeMe)
      $(removeMe).remove();
      console.log("< spin: " + spin + " prev: " + prevSpin);
    }
  }
  
  prevSpin = spin;
  
});
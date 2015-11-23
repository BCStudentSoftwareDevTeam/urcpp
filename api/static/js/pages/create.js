// The API object. All our calls to the
// server happen through this object.
var api = urcpp('v1');

//********************************************
// DATA SUBMISSION
//********************************************
 
function handleResponse (data) {
  if (data.response == "OK") {
    window.location.href = window.location.href = api.next();
  } else {
    /* global swal, urcpp */
    swal({  title: "Please contact " + urcpp.constants.alertEmail,   
            text: data["details"],   
            type: "error",   
            confirmButtonText: "Uh-Oh." 
    });
  }
};
 
function submitData () {
  var obj = formToObj(document.querySelector("form"));
  console.log("Sending data to server: " + JSON.stringify(obj) + "\n\n");
  api.set.create (username, obj, handleResponse ); 
  api.go();
};

//********************************************
// PAGE INTERACTIONS (GETETING DATA)
//********************************************
 
// This function sets the project title field
function setTitleAndStartDate (data) {
  // console.log(JSON.stringify(data));
  if ("project" in data) {
    console.log("Using project to set things: " + data);
    
    $("#title").val(data.project.title);
    $("#startDate").val(data.project.startDate);
    $("#duration").val(data.project.duration);
  }
};

function setOptions (element, options) {
  var $el = $("#" + element);
  $el.empty(); // remove old options
  $.each(
    options, 
    function (value,key) {
      $el.append($("<option></option>")
         .attr("value", value).text(key));
    }
  );  
}

function setProgram (data) {
  var programs = data.programs;
  // console.log(JSON.stringify(programs));

  var options = {};
  for (var ndx = 0; ndx < programs.length ; ndx++ ) {
    var prog = programs[ndx];
    console.log("Name: " + prog.name + " ID: " + prog.pID);
    options[prog.pID] = prog.name;
  }
  
  setOptions ("program", options);
};

function setFacultyProgram (data) {
  console.log("Using faculty to set things: " + JSON.stringify(data));
  console.log("\n");
  if (data.faculty && data.faculty.programID.pID) {
    var index = parseInt(data.faculty.programID.pID);
    console.log("Index for Program: " + index)
    $("#program").val(index);
  } else {
    $("#program").val(0); 
  }
};

function setDuration (data) {
  var durations = data.durations;
  
  var options = {};
  for (var ndx = 0; ndx < durations.length ; ndx++ ) {
    var dur = durations[ndx];
    options[dur] = dur + " weeks";
  }
 
  setOptions("duration", options);
};

function setDate (data) {
  // console.log(JSON.stringify(data));
  if ("startDate" in data) {
    $("#startDate").val(data.project.startDate);
  }
};

$(document).ready(function () {
  // API calls happen in-order.
  // First, we queue up the actions we want to take.
  api.programs.getAll(setProgram);
  api.projects.getPossibleDurations(setDuration);
  api.projects.get(username, setTitleAndStartDate);
  api.faculty.get(username, setFacultyProgram);
  // Then, we set them all in motion.
  api.go();
});

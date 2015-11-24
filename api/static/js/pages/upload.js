/* global username, urcpp, Dropzone */
var api = urcpp("v1");

// This turns out to be annoying...
Dropzone.autoDiscover = false;

function setPageElements (data) {
   console.log(data);
   var fac = data["details"];
   $("#firstname").html(fac["firstname"]);
}

//********************************************
// DATA SUBMISSION
//********************************************

function acceptUpload (file, done) {
  console.log("Done with: " + file);
  done();
}

var theDrop = null;

function configureDropzone () {
  /* global uploadType */
  
  console.log("Setting up dropzone.");
  console.log("Upload type for this dropzone is '" + uploadType + "'");
  
  var cfg =  {   
        url           :   "/urcpp/v1/file/upload/" + uploadType + "/" + username,
        method        :   "POST",
        maxFiles      :   1,
        // This is the "element name" for file transfer
        paramName     : "file",
        // In megabytes
        maxFilesize   :   5,
        accept        : acceptUpload
        
    };
    
  theDrop = new Dropzone("#drop", cfg);
  
  theDrop.on ("complete", function (file, done) {
    console.log("File upload complete");
    done();
  });
  
  theDrop.on ("success", function (response) {
    window.location.href = window.location.href = api.next();
  });
}

var setFields = function (data) {
  if (data.response = "OK") {
    $("#fileLabel").text(data.uploadType);
  }
}
  
$(document).ready ( function () {
   console.log ("Looking up: " + username);
   configureDropzone();
   // api.faculty.get (username, setPageElements);
   // api.go();
  api.projects.getNarrative (username, (location.pathname).split("/").pop(), setFields);
  api.go();
   
});

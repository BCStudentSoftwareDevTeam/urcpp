/* global username, urcpp, Dropzone, referrer */

function buttonMoveForward () {
  var localNextPage = "/";
  if (referrer != "") {
    localNextPage = localNextPage.concat(username + "/" + nextPage);
    window.location.href =  localNextPage;
  }
};

function goNextPage() {
   // If coming from the home page to upload CV, this takes you back there
  var localNextPage = "/";
  if (referrer != "") {
    console.log("Coming from [inside referrer check]: " + referrer);
    localNextPage = localNextPage.concat(username + "/" + nextPage);
    console.log("Local next page: " + localNextPage);
  }
  console.log("File upload complete");
  console.log("Actual next page: " + localNextPage); 
  $("#moveForward").removeAttr('disabled');
  $("#success").removeAttr('hidden');
 // window.location.href =  localNextPage;
};

$(document).ready ( function () {
  /*global nextPage*/
  console.log ("Looking up: " + username);
  
 
  Dropzone.options.drop = {
    paramName: "file",
    maxFilesize: 25,
    accept: function (file, done) {
      done()
    },
    init: function () {
      this.on("success", function (file, serverResponse) {       
				          goNextPage()
      });
    },
  };
});

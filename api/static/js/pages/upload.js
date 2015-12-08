/* global username, urcpp, Dropzone, referrer */

function buttonMoveForward () {
  var localNextPage = "/";
  if (referrer != "") {
    localNextPage = localNextPage.concat(username + "/" + nextPage);
    window.location.href =  localNextPage;
  }
};

$(document).ready ( function () {
  /*global nextPage*/
  console.log ("Looking up: " + username);
  
  // If coming from the home page to upload CV, this takes you back there
  var localNextPage = "/";
  if (referrer != "") {
    console.log("Coming from [inside referrer check]: " + referrer);
    localNextPage = localNextPage.concat(username + "/" + nextPage);
    console.log("Local next page: " + localNextPage);
  }
  
  Dropzone.options.drop = {
    paramName: "file",
    maxFilesize: 25,
    accept: function (file, done) {
      console.log("File upload complete");
      console.log("Actual next page: " + localNextPage);
      done();
    },
    
    init: function () {
      this.on("success", function (file, serverResponse) {       
                                        window.location.href =  localNextPage;
      });
    },
  };
});

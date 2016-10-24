/* global username, urcpp, Dropzone, referrer, getValue */

function buttonMoveForward () {
  var localNextPage = "/";
  localNextPage = localNextPage.concat(nextPage);
  if (getValue == "home") {
   // If coming from the home page to upload CV, this takes you back there
    window.location.href = "/";
  } else {
    window.location.href =  localNextPage;
  }
};

function goNextPage() {
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

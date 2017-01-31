/* global $ username, urcpp, Dropzone, referrer, getValue */

function buttonMoveForward () {
  var localNextPage = "/";
  localNextPage = localNextPage.concat(nextPage);
  if (getValue == "home") {
   // If coming from the home page to upload CV, this takes you back there
    window.location.href = "/";
  } else {
    window.location.href =  localNextPage;
  }
}

function goNextPage() {
  $("#moveForward").prop('disabled', false);
  $("#success").prop('hidden', false);
}

var localNextPage = "/";
localNextPage = localNextPage.concat(nextPage);
if (getValue == "home") {
   // If coming from the home page to upload CV, this takes you back there
    $(".breadcrumb").hide();
  
}

Dropzone.options.drop = {
  paramName: "file",
  maxFilesize: 25,
  accept: function (file, done) {
    console.log("jsdhf");
    done();
  },
  init: function () {
    console.log("sakdjfklasd");
    this.on("success", function (file, serverResponse) {
      console.log("success")
			          goNextPage()
    });
  },
};
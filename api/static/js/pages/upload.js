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
  $("#success").hide()
  $("#success").fadeIn("slow")
  $("#failed").hide()
}

var localNextPage = "/";
localNextPage = localNextPage.concat(nextPage);
if (getValue == "home") {
   // If coming from the home page to upload CV change the breadcrumbs to only go home
   $(".breadcrumb").html('<li><a href="/">Home</a></li>')  
}

Dropzone.options.drop = {
  paramName: "file",
  maxFilesize: 25,
  acceptedFiles: ".doc, .docx, .odt, .pdf, .rtf",
  error: function(file, errormessage, xhr){
    $("#success").hide()
    $("#failed").hide()
    $("#errormessage").text(errormessage)
    $("#failed").fadeIn("slow")
    this.removeFile(file)
  },
  init: function () {
    this.on("success", function (file, serverResponse) {
			          goNextPage()
    });
  },
};
/* global $ username, urcpp, Dropzone, referrer, getValue, prevFilepath */

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
function deleteFile(){
  if (prevFilepath != "")
  {
    var data = {"username": username, "uploadType":uploadType}
     $.ajax({
        type : "POST",
        url : removefileAPI,
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
          Dropzone.options.maxFiles = 1 
          console.log(Dropzone.options.maxFiles)
          $("#drop").removeClass("dz-max-files-reached")
        }
    });
  }
    $("#dropzone-cancel").hide()
    $("#dropzone-remove").show()
    $("#dropzone-download").hide()
    $("#successmessage").text("Your " + uploadType + " has been removed.")
    $("#moveForward").prop('disabled', true);

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
   $(".breadcrumb").html('<li><a href="/">Home</a></li>')  
}

Dropzone.options.drop = {
  paramName: "file",
  maxFilesize: 25,
  maxFiles: 1,
  processing: function(file)
  {
    $("#dropzone-cancel").show()

  },removedfiled: function(file){
    this.removeFile(file)
    this.options.maxFiles = this.options.maxFiles;
  },
  previewTemplate:document.querySelector('#tpl').innerHTML,
  acceptedFiles: ".doc, .docx, .odt, .pdf, .rtf",
  error: function(file, errormessage, xhr){
    $("#success").hide()
    $("#failed").hide()
    $("#errormessage").text(errormessage)
    $("#failed").fadeIn("slow")
    this.removeFile(file)
  },
  success: function(file, serverResponse){
    goNextPage()
    $("#dropzone-cancel").hide()
    $("#dropzone-remove").show()
    $("#dropzone-download").hide()
    $("#successmessage").text("Your " + uploadType + " has been uploaded.")

    
  },
  init: function () {
      if ( prevFilepath != "")
      {
        var  file = { name: prevFilepath, accepted:true};       
        this.options.addedfile.call(this, file);
        this.options.processing.call(this,file)
        this.options.success.call(this,file)
        this.files.push(file)
        this.options.complete.call(this,file)
        this.options.maxfilesreached.call(this,file)

        $("#dropzone-remove").show()
        $("#dropzone-download").show()

      }

  },
};
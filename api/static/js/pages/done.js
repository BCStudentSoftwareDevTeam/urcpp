  /* global api, swal, urcpp, username $ */
  api = urcpp("v1");
  function handleResponse (data) {
    if (data.response == "OK") {
      window.location.href = window.location.href = "/";
    } else {
     
      swal({  title: "Please contact " + urcpp.constants.alertEmail,   
              text: data["details"],   
              type: "error",   
              confirmButtonText: "Uh-Oh." 
      });
    }
  };
  
  function finalizeSubmission() {
    console.log("Finalizing application");
    api.done.finalize(username, handleResponse); 
    api.go();
  };
  
  
  function withdraw(projectID) {
    swal({
  title: "Are you sure?",
  text: "All files will be deleted!",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#DD6B55",
  confirmButtonText: "Yes, delete it!",
  cancelButtonText: "No, cancel please!",
  closeOnConfirm: false,
  closeOnCancel: false
},
function(isConfirm){
  if (isConfirm) {
    var postValue = {};
    postValue[projectID] = 'Withdrawn';
    $.post("/committee/allProjects/updateStatus", postValue, function(result){
    window.location.replace("/");
    });
    
  } else {
    swal("Cancelled", "Your imaginary file is safe :)", "error");
  }
});
    

  };
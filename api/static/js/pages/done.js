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
    var postValue = {};
    postValue[projectID] = 'withdrawn';
    $.post("/committee/allProjects/updateStatus", postValue, function(result){
    });
    window.location.replace("/");

  };
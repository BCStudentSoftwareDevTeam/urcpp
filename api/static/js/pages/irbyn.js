from ..API.collaborators import delete_all_collaborators, getCollaborators

function setAction() {
    if ($("#irbYes").checked) {
      $("#setIRB").attr("action", "/{{username}}/upload/irb");
    } else if ($("#irbNo").checked) {
      $("#setIRB").attr("action", "/{{username}}/upload/narrative");
    }
  }
  
function back_button {
  if (numCollab > 0)
    window.history.back(2);
  else {
    window.history.back(1);
  }
}
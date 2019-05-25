function setAction() {
    if ($("#irbYes").checked) {
      $("#setIRB").attr("action", "/{{username}}/upload/irb");
    } else if ($("#irbNo").checked) {
      $("#setIRB").attr("action", "/{{username}}/upload/narrative");
    }
  }
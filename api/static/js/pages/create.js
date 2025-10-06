$(document).ready(function(){
  $("#startDate").datepicker({
    dateFormat: "mm-dd-yy",
    startDate: "01-01-{{params.year}}",
    endDate: "12-31-{{params.year}}"
  });
  $("[ data-toggle='popover']").popover();
});

function checkForRequired() {
  if ($("#title").val().length == 0) {
    $("#projectTitleGroup").addClass("has-error");
  };
  if ($("#program").val() == "---") {
    $("#projectProgramGroup").addClass("has-error");
  };
}

$(document).ready(function(){
  $("#startDate").change(function(){
    changeEndDate();
  });
  $("#duration").change(function(){
    changeEndDate();
  });
});
function changeEndDate() {
  var startDateStr = $("#startDate").val();
  var startDateArr= startDateStr.split("-")
  var endDateObj = new Date(startDateArr[2], startDateArr[0]-1, startDateArr[1]);
  var weeks = $("#duration").val();
  endDateObj.setDate(endDateObj.getDate() + weeks*7);
  console.log(endDateObj);
  $("#endDate").val(endDateObj.getMonth()+1 + '-' + endDateObj.getDate() + '-' + endDateObj.getFullYear());
  $("#endDateDisplay").html(endDateObj.getMonth()+1 + '-' + endDateObj.getDate() + '-' + endDateObj.getFullYear());
}

$(function() {
  $("#startDate").datepicker({
    dateFormat: "mm-dd-yy", 
    startDate: "01-01-{{params.year}}", 
    endDate: "12-31-{{params.year}}"
  });
});
$("[ data-toggle='popover']").popover();


function checkForRequired() {
  if ($("#title").val().length == 0) {
    $("#projectTitleGroup").addClass("has-error");
  };
  if ($("#program").val() == "---") {
    $("#projectProgramGroup").addClass("has-error");
  };
}

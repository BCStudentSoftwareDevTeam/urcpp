$(document).ready(animate);

function animate(){
  var progressBar = $(".project-progress-bar");
  var projStatus = progressBar.data('status');
  console.log("projStatus: " + projStatus);
  var dateState = $("#dateStateDiv").data('datestate');
  var point = progressBar.find("#" + projStatus);

  if (dateState == "reviewopen") {
    point = progressBar.find("#pending")
  }
  if (dateState == "allclosed") {
    point = progressBar.find("#Accept")
  }
  point.addClass('point--active');
  point.prevAll().addClass('point--complete');
  point.nextAll().removeClass('point--complete');
  
  fillProgressBar(projStatus, dateState);
}

function fillProgressBar(projStatus, dateState) {
  console.log(projStatus);
  var fillPercent = 33.3;
  var step = 0;
  switch (projStatus) {
    case "AllClosed":
    case "Reject":
    case "Accept":
      step = 3;
      break;
    case "Pending":
      step = 2;
      break;
    case "Incomplete":
        step = (dateState != "appopen") ? 2 : 1
      break;
    case "Start":
        step = (dateState == "reviewopen") ? 2 : 0
      break;
    default:
      step = 0;
  }
  document.getElementById("bar_fill").style.width = (step*fillPercent) + "%";
}

$(document).ready(function(){
    $(function() {
      $("#startDate").datepicker({
        dateFormat: "mm-dd-yy",
        startDate: "01-01-{{params.year}}",
        endDate: "12-31-{{params.year}}"
      });
    });
    $("[ data-toggle='popover']").popover();

    $(function() {
      $("#endDate").datepicker({
        dateFormat: "mm-dd-yy",
        startDate: "01-01-{{params.year}}",
        endDate: "12-31-{{params.year}}",
        onSelect: function(endDateText) {
            var endDateStr = this.value;
            var endDateArr= endDateStr.split("-")
            var endDateObj = new Date(endDateArr[2], endDateArr[0]-1, endDateArr[1]);
            updateEndDateLabel(endDateObj);
        }
      });
    });
    $("[ data-toggle='popover']").popover();

  $("#startDate").change(function(){
  if ($("#duration").val() != null) {
    var startDateStr = $("#startDate").val();
    var startDateArr= startDateStr.split("-")
    var endDateObj = new Date(startDateArr[2], startDateArr[0]-1, startDateArr[1]);
    changeEndDate(endDateObj);
    }
  });

  $("#duration").change(function(){
      if ($("#startDate").val() != "") {
        var startDateStr = $("#startDate").val();
        var startDateArr= startDateStr.split("-")
        var endDateObj = new Date(startDateArr[2], startDateArr[0]-1, startDateArr[1]);
        changeEndDate(endDateObj);
      }
  });
});

$("#endDate").change(function(){
    var endDateStr = $("#endDate").val();
    var endDateArr= endDateStr.split("-")
    var endDateObj = new Date(endDateArr[2], endDateArr[0]-1, endDateArr[1]);
});

function changeEndDate(endDateObj) {
  var weeks = $("#duration").val();
  endDateObj.setDate(endDateObj.getDate() + weeks * 7);
  updateEndDateLabel(endDateObj);
  $("#endDate").val(endDateObj.getMonth()+1 + '-' + endDateObj.getDate() + '-' + endDateObj.getFullYear());
  $("#endDateDisplay").html(endDateObj.getMonth()+1 + '-' + endDateObj.getDate() + '-' + endDateObj.getFullYear());
  $("#endDate").focus();
}



function updateEndDateLabel(endDateObj) {
    const formatter = new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: '2-digit',
        weekday: 'short'
    });

      // Format the date
    const formattedDate = formatter.format(endDateObj);

    if (endDateObj != "Invalid Date") {
        $("#endDateCleanLabel").text(formattedDate);
    };
}

function checkForRequired() {
  if ($("#title").val().length == 0) {
    $("#projectTitleGroup").addClass("has-error");
  };
  if ($("#program").val() == "---") {
    $("#projectProgramGroup").addClass("has-error");
  };
}

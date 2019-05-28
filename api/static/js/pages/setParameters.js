/* global $, swal */ 
$(function() {
      $("#applicationOpenDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
      $("#applicationOpenDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
      $("#ProposalOpenDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
      $("#ProposalAcceptanceDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
       $("#ProposalClosedDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
       $("#AbstractnarrativesAcceptanceDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
       $("#AllSubmissionsClosedDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
    });
    
$('.selectpicker').selectpicker({
});

function change_check_color(parameters_id){
  $(".isCurrentParameter").addClass("disabled");
  
  $("#set_current_parameters-"+parameters_id).removeClass("disabled")
}

 function set_current_parameters(parameters_id) {
    swal({
  title: "Are you sure?",
  text: "This will change the current cycle to be under these parameters",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#DD6B55",
  confirmButtonText: "Confirm",
  cancelButtonText: "Cancel",
  closeOnConfirm: true,
  closeOnCancel: false
},
function(isConfirm){
  if (isConfirm) {
    $.get('/set/current_parameters/'+ parameters_id, function( data ){
    change_check_color(parameters_id);
    });
  } else {
    swal("Cancelled", "Everything is normal");
  }
});

  };
  
function warnBeforeRedirect(url) {
  swal({
  title: "Are you sure?",
  text: "This will delete these parameters and may cause unexpected behavior",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#DD6B55",
  confirmButtonText: "Confirm",
  cancelButtonText: "Cancel",
  closeOnConfirm: false,
  closeOnCancel: false
},
function(isConfirm){
  if (isConfirm) {
    location.replace(url);
  } else {
    swal("Cancelled", "Nothing has changed");
  }
});
}
  
$("#delete_parameters").click(function(e) {
  e.preventDefault();
  var linkURL = $(this).attr("href");
  warnBeforeRedirect(linkURL);
});

function editParameters(year){
  //populates inputs above table with info from set parameter
  // console.log("editParemeters called yo");
  
  // var year = document.getElementById('parameterYear').innerHTML;
  document.getElementById('newYear').value=(year);

  var unformattedOpenDate = document.getElementById('openDate'+year).innerHTML;
  var openDate = unformattedOpenDate.replace(/\//g, "-")
  document.getElementById('applicationOpenDate').value=(openDate);
  
  var unformattedCloseDate = document.getElementById('closeDate'+year).innerHTML;
  var closeDate = unformattedCloseDate.replace(/\//g, "-") //Replaces "/" with "-"
  document.getElementById('applicationCloseDate').value=(closeDate);
  
  var mileageRate = document.getElementById('mileageRates'+year).innerHTML.substr(1);
  document.getElementById('mileageRate').value=(mileageRate);
  
  var laborRate = document.getElementById('laborRates'+year).innerHTML.substr(1);
  document.getElementById('laborRate').value=(laborRate);
}

$("#laborRate").change(function() {
    var curr_val = parseFloat($(this).val());
    $(this).val(curr_val.toFixed(2));
});

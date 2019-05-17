/* global $, swal */ 
$(function() {
      $("#applicationOpenDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
      $("#applicationCloseDate").datepicker({
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
    swal("Cancelled", "Everything is normal");
  }
});
}
  
$("#delete_parameters").click(function(e) {
  e.preventDefault();
  var linkURL = $(this).attr("href");
  warnBeforeRedirect(linkURL);
});

function editParameters(){
  //populates inputs above table with info from set parameter
  console.log("editParemeters called yo");
  
  var year = document.getElementById('parameterYear').innerHTML;
  // console.log("year   "+ year);
  document.getElementById('newYear').value=(year);
  // console.log("After newYear");
  var openDate = document.getElementById('openDate').innerHTML;
  document.getElementById('applicationOpenDate').value=(openDate);
  
  var closeDate = document.getElementById('closeDate').innerHTML;
  document.getElementById('applicationCloseDate').value=(closeDate);
  
  // console.log("time for vroomies");
  // var mileageRate = document.getElementById('mileageRates').innerHTML;
  // console.log("mileageRate   "+ mileageRate);
  // document.getElementById('mileageRate').value=(mileageRate);
  // console.log("AHHH");
  
  // var laborRate = document.getElementById('laborRates').innerHTML;
  // document.getElementById('laborRate').value=(laborRate);
}
/* global $, swal */ 
$(function() {
      $("#applicationOpenDate").datepicker({
        dateFormat: "yy-mm-dd"
      });
      
      $("#applicationCloseDate").datepicker({
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
  // console.log($("#"+year+"_staff").attr("data-value"))
  // console.log($("#IRBchair_id").val())
  // console.log($("#staffsupport_id").val())
  $("#newYear")[0].value=$("#"+year+"_year")[0].innerText;
  $("#IRBchair_id").val($("#"+year+"_irb").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');  
  $("#currentchair_id").val($("#"+year+"_chair").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#staffsupport_id").val($("#"+year+"_staff").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#mileageRate").val($("#"+year+"_mile").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#laborRate").val($("#"+year+"_labor").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#applicationOpenDate").val($("#"+year+"_appopen").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#applicationCloseDate").val($("#"+year+"_appclose").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#ProposalOpenDate").val($("#"+year+"_proposalopen").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#ProposalAcceptanceDate").val($("#"+year+"_proposalaccept").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#ProposalClosedDate").val($("#"+year+"_proposalclose").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#AbstractnarrativesAcceptanceDate").val($("#"+year+"_abstract").attr("data-value"));
  $('.selectpicker').selectpicker('refresh');
  $("#AllSubmissionsClosedDate").val($("#"+year+"_allsubmit").attr("data-value"));
  $(".selectpicker").selectpicker('refressh');
}

$("#laborRate").change(function() {
    var curr_val = parseFloat($(this).val());
    $(this).val(curr_val.toFixed(2));
});

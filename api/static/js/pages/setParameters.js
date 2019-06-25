/* global $, swal */ 
$(function() {
      $("#applicationOpenDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      
      $("#applicationCloseDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      
      $("#ProposalOpenDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      $("#ProposalAcceptanceDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      
       $("#ProposalClosedDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      
       $("#AbstractnarrativesAcceptanceDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
      
       $("#AllSubmissionsClosedDate").datepicker({
        dateFormat: "mm/dd/yy"
      });
    });
    
$('.selectpicker').selectpicker({
});

function change_check_color(parameters_id){
  $(".isCurrentYear").removeClass("isCurrentYear");
  
  $("#set_current_parameters-"+parameters_id).addClass("isCurrentYear")
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
    		$.get('/set/current_parameters/'+ parameters_id, function(data){
    			change_check_color(parameters_id);
    		});
  	} else {
    		swal("Cancelled", "No changes made.");
  	}
    });
};
  
function warnBeforeRedirect(url) {
  swal({
  	title: "Are you sure?",
  	text: "This will delete the URCPP application for this year, including all projects!",
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
  //populates inputs in above table with info from lower table
  // console.log($("#"+year+"_staff").attr("data-value"))
  // console.log($("#IRBchair_id").val())
  // console.log($("#staffsupport_id").val())
  $("#newYear")[0].value=$("#"+year+"_year")[0].innerText;
  $("#IRBchair_id").val($("#"+year+"_irb").attr("data-value"));
  $("#currentchair_id").val($("#"+year+"_chair").attr("data-value"));
  $("#staffsupport_id").val($("#"+year+"_staff").attr("data-value"));
  $("#mileageRate").val(parseFloat($("#"+year+"_mile").attr("data-value")).toFixed(2));
  $("#laborRate").val(parseFloat($("#"+year+"_labor").attr("data-value")).toFixed(2));
  $("#applicationOpenDate").val($("#"+year+"_appopen").attr("data-value"));
  $("#applicationCloseDate").val($("#"+year+"_appclose").attr("data-value"));
  $("#ProposalOpenDate").val($("#"+year+"_proposalopen").attr("data-value"));
  $("#ProposalAcceptanceDate").val($("#"+year+"_proposalaccept").attr("data-value"));
  $("#ProposalClosedDate").val($("#"+year+"_proposalclose").attr("data-value"));
  $("#AbstractnarrativesAcceptanceDate").val($("#"+year+"_abstract").attr("data-value"));
  $("#AllSubmissionsClosedDate").val($("#"+year+"_allsubmit").attr("data-value"));
  $(".selectpicker").selectpicker('refresh');
  window.scrollTo(0, 0);  // Send user to the top of the page
}

$("#laborRate").change(function() {
    var curr_val = parseFloat($(this).val());
    $(this).val(curr_val.toFixed(2));
});

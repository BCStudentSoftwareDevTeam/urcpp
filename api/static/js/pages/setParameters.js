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

function addEvent(node, type, callback) {
  //Step 1 of form validation
  if (node.addEventListener) {
    node.addEventListener(type, function(e) {
      callback(e, e.target);
    }, false);
  } else if (node.attachEvent) {
    node.attachEvent('on' + type, function(e) {
      callback(e, e.srcElement);
    });
  }
}

function shouldBeValidated(field) {
  //Step 2 of form validation which simply tests that it’s neither disabled nor readonly, and that it has either a pattern or a required attribute
  return (
    !(field.getAttribute("readonly") || field.readonly) &&
    !(field.getAttribute("disabled") || field.disabled) &&
    (field.getAttribute("pattern") || field.getAttribute("required"))
  );
}

function instantValidation(field) {
  //Step 3 of form validation which tests the field and then performs the actual validation
  if (shouldBeValidated(field)) {
    //the field is invalid if:
    //it's required but the value is empty
    //it has a pattern but the (non-empty) value doesn't pass
    var invalid =
      (field.getAttribute("required") && !field.value) ||
      (field.getAttribute("pattern") &&
        field.value &&
        !new RegExp(field.getAttribute("pattern")).test(field.value));
    if (!invalid && field.getAttribute("aria-invalid")) {
      field.removeAttribute("aria-invalid");
    } else if (invalid && !field.getAttribute("aria-invalid")) {
      field.setAttribute("aria-invalid", "true");
    }
  }
}

addEvent(document, "change", function(e, target) {
  instantValidation(target);
});

//step4: now bind a change event to each applicable for field
var fields = [
  document.getElementsByTagName("input"),
  document.getElementsByTagName("textarea")
];
for (var a = fields.length, i = 0; i < a; i++) {
  for (var b = fields[i].length, j = 0; j < b; j++) {
    addEvent(fields[i][j], "change", function(e, target) {
      instantValidation(target);
    });
  }
}
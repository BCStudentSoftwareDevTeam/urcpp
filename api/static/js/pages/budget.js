/* global mileageRate */
// This little bit of script totals things up as 
// people enter their budget items.
function findTotal() {
  var arr = document.getElementsByClassName("quantity");
  var tot = 0;
  
  for(var i = 0; i < arr.length; i++){
    var value = arr[i].value;
    // console.log("Element value: " + value)
    if(parseInt(value)) {
      console.log(arr[i].id.trim().localeCompare("miles"));
      if (arr[i].id.trim().localeCompare("miles") == 0) {
        tot += parseInt(value)*mileageRate;
        if (mileageRate == 0) {
          $("#mileageWarning").removeAttr("hidden");
        }
      } else {
        tot += parseInt(value);
      }
    }
  }
  
// Set the total.
$("#total").val(tot.toFixed(2));

return tot;
};

// Need to run on first page load.
$(document).ready ( function () {
  findTotal();
});


<!-- Submit data to server -->
 /* global urcpp, api, username, formToObj, show */
api = urcpp("v1"); 

function submitData() {  
  var obj =  document.getElementById("budgetForm");
  console.log($("#budgetForm"));
  /* Ajax the data to /budget */
  $("#budgetForm")[0].submit();  
  console.log("Submitted");
};


function limit() {

  var currentTotal = findTotal();
  console.log(currentTotal);

  if( currentTotal > 8300) {
     $("#exceeding").modal();
   }
   else {
     console.log("About to submit");     
     submitData();
   }
 };
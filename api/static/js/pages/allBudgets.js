/* global numRows */
function countBudgetRows () {
  // console.log("Start counting");
  console.log("# rows: " + numRows);
  var grandTotal = 0;
  // Iterates through each row
  for (var idx = 0; idx < numRows; idx ++ ){
    if ($("#row" + idx).css('display') == "table-row") {
    var sum = 0;
    var rows = $("#row" + idx).find("td[name='rowValue']");
    rows.each(function (value, i) {
      sum += parseFloat($(this).text());
      // console.log("Summing: "  + sum);
    });
    // console.log("Sum: " + sum);
    var truncatedSum = Math.round(sum*100)/100;
    $("#rowTotal" + idx).html(truncatedSum);
    grandTotal += sum;
    $("#grandTotal").text("$" + grandTotal.toFixed(2));
    }
  };
};

function updateFilters () {
  var rows = document.getElementsByName("leRow");   // All rows
  var projectStatii = document.getElementsByName("projectStatus");
  var statii = document.getElementsByName("status");   // All filter status 

  // Iterates each row
  for (var j = 0; j < rows.length; j++) {
    // Iterates each status option
    for (var i = 0; i < statii.length; i++ ) {
      if (!statii[i].checked && 
          projectStatii[j].textContent.toLowerCase().trim() == statii[i].value.toLowerCase().trim()) {
        rows[j].style.display = 'none';
      } else if (statii[i].checked && 
                 projectStatii[j].textContent.toLowerCase().trim() == statii[i].value.toLowerCase().trim()) {
        rows[j].style.display = "table-row";
      }
    }
  }
  countBudgetRows();
  
};

$(document).ready(function () {
  $('#incomplete').attr('checked', false);
  updateFilters();
  countBudgetRows();
  $('#incomplete').attr('checked', false);
  $("[ data-toggle='popover']").popover();
});

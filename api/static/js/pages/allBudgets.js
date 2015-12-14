/* global numRows */
function countBudgetRows () {
  // console.log("Start counting");
  console.log("# rows: " + numRows);
  var grandTotal = 0;
  for (var idx = 0; idx < numRows; idx ++ ){
    var sum = 0;
    var rows = $("#row" + idx).find("td[name='rowValue']");
    rows.each(function (value, i) {
        sum += parseFloat($(this).text());
        // console.log("Summing: "  + sum);
        
    });
    // console.log("Sum: " + sum);
    $("#rowTotal" + idx).html(sum);
    grandTotal += sum;
    $("#grandTotal").text("$" + grandTotal);
  };
};

$(document).ready(function () {
  countBudgetRows();
});

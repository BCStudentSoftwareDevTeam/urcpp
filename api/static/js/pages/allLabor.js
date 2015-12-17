
/* global numRows, laborRate */
function countLaborRows () {
  // console.log("Start counting");
  console.log("# rows: " + numRows);
  var grandTotal = 0;
  for (var idx = 0; idx < numRows; idx ++ ){
    var sum = 0;
    var numStudents = $("#row" + idx).find("td[name='numStudents']").text();
    console.log("#studs: " + numStudents);
    var duration = $("#row" + idx).find("td[name='duration']").text();
    console.log("Dur: " + duration);
    sum = (numStudents * duration * laborRate);
    $("#rowTotal" + idx).html(sum.toFixed(2));
    grandTotal += sum;
  };
  $("#grandTotal").text("$" + grandTotal.toFixed(2));
  };

$(document).ready(function () {
  countLaborRows();
});

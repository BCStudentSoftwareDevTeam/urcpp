/* global numRows */
function recalculate () {
  var total = 0;
  for (var idx = 0; idx < numRows; idx ++ ){
    var sum = 0;
    var rows = $("#row" + idx).find("td.rowValue");
    rows.each(function (value, i) {
      // console.log(parseFloat(this.innerHTML));
      sum += (parseFloat(this.innerHTML));
      console.log("Sum " + sum);
      $("#average" + idx).html(parseFloat(sum/5).toFixed(2)); //Five 
    });
  };
};

$(document).ready(function(){
  // $('[data-toggle="tooltip"]').tooltip(); 
  recalculate();
});

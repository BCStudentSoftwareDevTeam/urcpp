/* global numRows */
function recalculate () {
  var total = 0;
  for (var idx = 0; idx < numRows; idx ++ ){
    var sum = 0;
    var rows = $("#row" + idx).find("select.rowValue");
    rows.each(function (value, i) {
        sum += (this.options.selectedIndex);
        $("#average" + idx).html(sum/3);   //3 is the number of ratings that each criteria has (Exceptional, Good, Needs Improvement)
    });
  };
};

$(document).ready(function(){
  recalculate();
});

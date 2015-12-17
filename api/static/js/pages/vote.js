/* global numRows */
function recalculate () {
  var total = 0;
  for (var idx = 0; idx < numRows; idx ++ ){
    var sum = 0;
    var rows = $("#row" + idx).find("select.rowValue");
    rows.each(function (value, i) {
        sum += (this.options.selectedIndex);
        $("#average" + idx).html(sum/5);    //Five 
    });
  };
};

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip(); 
  recalculate();
});

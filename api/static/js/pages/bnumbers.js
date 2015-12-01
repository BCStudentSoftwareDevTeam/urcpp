api = urcpp("v1")

// In milliseconds
var BNUMBERCHECKDELAY = 250;

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

function setBNumberStatus (id) {
  return function (data) {
    console.log("BNumber Status: " + JSON.stringify(data));  
    var selector = "#cgroup" + id;
    if (data["response"] == "OK") {
      $(selector).removeClass("has-error");
      $(selector).addClass("has-success");
    } else {
      $(selector).removeClass("has-success");
      $(selector).addClass("has-error");
    }
  };};

function checkValidBNumber (id) {
  /* global api */
  var bnumber = $("#cbnumber" + id).val();
  console.log("About to check " + bnumber);
  
  var post = aja()
    .method ('POST')
    .url ("/v1/checkBNumber/" + bnumber)
    .body ({})
    .on ('success', setBNumberStatus(id) )
    .go();
  
};
   
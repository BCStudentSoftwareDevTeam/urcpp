api = urcpp("v1")

// In milliseconds
var BNUMBERCHECKDELAY = 250;

var numCollabsChecked = 0;

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

function setBNumberStatus (id) {
  return function (data) {
    // console.log("Response: " + data["response"]);
    // console.log("BNumber Status: " + JSON.stringify(data));  
    var selector = "#cgroup" + id;
    if (data["response"] == "OK") {
      $(selector).removeClass("has-error");
      $(selector).addClass("has-success");
      numCollabsChecked += 1;
      // console.log(numCollabsChecked);
      /* global numCollabs */
      if (numCollabsChecked >= numCollabs) {
        // console.log("Probably enough good B-numbers");  //This is a weak solution. 
                                                        //If the user deletes a good B-number and re-enters another good B-numb 
                                                        // (same or different), they could potentially leave a B-number box blank
                                                        // Instead, a better solution should actually check the dom for all $(selector)'s 
                                                        // and ensure they all have the class "has-success" applied'
        $("#submit").prop('disabled', false);
      }
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
    .url ("/" + username + "/checkBNumber")
    .body({ 'bnum' : bnumber })
    .type('json')
    .on ('success', setBNumberStatus(id) )
    .go();
  
};

api = urcpp("v1")
0
// In milliseconds
var USERNAMECHECKDELAY = 250;

var numCollabsChecked = 0;

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

function setUsernameStatus (id) {
  return function (data) {
    // console.log("Response: " + data["response"]);
    // console.log("BNumber Status: " + JSON.stringify(data));  
    var selector = "#cgroup" + id;
    var wrong_alert =  '<div class="alert alert-danger col-sm-4" id="wrong-id-'+id+'"role="alert">Faculty Not Found</div>'
    var user_alert = '<div class="alert alert-danger col-sm-4" id="user-'+id+'"role="alert">You are already a collaborator</div>'
    $('#user-'+id).remove()
    $('#wrong-id-'+id).remove();
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
    } else if (data["response"] == "USER") {
      $(selector).removeClass( "has-success");
      $(selector).addClass("has-error");
      $(selector).append(user_alert);
      
    } else {
      $(selector).removeClass("has-success");
      $(selector).addClass("has-error");
      $(selector).append(wrong_alert);
    }
  };};

function checkValidUsername (id) {
  /* global api */
  var username = $("#cusername" + id);
  console.log("About to check " + username);
  
  var post = aja()
    .method ('POST')
    .url ("/check_username")
    .body({ 'u_name' : username })
    .type('json')
    .on ('success', setUsernameStatus(id) )
    .go();
  
};
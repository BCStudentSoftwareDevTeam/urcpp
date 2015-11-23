/* global username, urcpp */
var api = urcpp("v1");

function setPageElements (data) {
   console.log(data);
   var fac = data["details"];
   $("#lastname").html(fac["lastname"]);
   $("#firstname").html(fac["firstname"]);
}

$(document).ready ( function () {
   console.log ("Looking up: " + username);
   api.faculty.get (username, setPageElements);
   api.go();
});

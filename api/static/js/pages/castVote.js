
function success() {
  $('#success').removeAttr('hidden');
}

$(document).ready( function() {
  this.on("success", function(serverResponse) {
    success()
  
  });
  });
$("[ data-toggle='popover']").popover();
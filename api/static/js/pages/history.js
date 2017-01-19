/* global $ */
$(document).ready(function() {
    change_button();
    $(".checkbox_array").click(function() {
        change_button();
    });
});
function atLeastOneIsCheckedFromFaculty(){
    var faculty_check = $('.primary > .checkbox > label > input[type=checkbox]:checked').length > 0;
    
    var collaborators =  $(".collab_checks");
    var areAllCollabsChecked = false;
    collaborators.each(function(index, value) {
        
    });
}
function change_button() {
var atLeastOneIsChecked = $('input[type=checkbox]:checked').length > 0;
        if (atLeastOneIsChecked) {
            $("#submit").removeAttr("disabled");
        } else {
            $("#submit").prop("disabled", true);
        }
        
}
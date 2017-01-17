$(document).ready(function() {
    
    $(".checkbox_array").click(function() {
        var atLeastOneIsChecked = $('input[type=checkbox]:checked').length > 0;
        if (atLeastOneIsChecked) {
            $("#submit").removeAttr("disabled");
        } else {
            $("#submit").prop("disabled", true);
        }
    })
})
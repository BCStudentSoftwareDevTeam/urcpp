function getEmail(pID, username) {
    $.ajax({
        url: '/chair/awardLetters/send/'+ username +'/' + String(pID),
        dataType: 'json',
        type: 'GET',
        success: function(response) {
          result = response["mail_to"]

          if (result.includes("Failed")){
            $("#flash_message_div").removeClass("alert-success")
            $("#flash_message_div").addClass("alert-danger")
            $("#flash_message_div").show()
          }else{
            $("#flash_message_div").addClass("alert-success")
            $("#flash_message_div").removeClass("alert-danger")
            $("#flash_message_div").show()
          }
            $("#flash_message").text(result)
        },
        error: function(error) {
            $("#flash_message_div").removeClass("alert-success")
            $("#flash_message_div").addClass("alert-danger")
            $("#flash_message_div").show()
            $("#flash_message").text("Failed to send email")
        }
    });
}

function postLetter() {
    body = CKEDITOR.instances.body.getData()
    $.ajax({
        url: '/chair/awardLetters/save',
        data: { 'body': body, 'subject': $("#subject").val() },
        dataType: 'json',
        type: 'POST'
    });
}

function getLetter() {
    $.ajax({
        url: '/chair/awardLetters/get',
        dataType: 'json',
        type: 'GET',
        success: function(response) {
            CKEDITOR.instances.body.setData(response['body'])
            $("#subject").val(response["subject"])
        },
        error: function(error) {
            console.log(error);
        }
    });
}

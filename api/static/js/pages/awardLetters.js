function getEmail(pID, username) {
    $.ajax({
        url: '/chair/awardLetters/generate/'+ username +'/' + String(pID),
        dataType: 'json',
        type: 'GET',
        success: function(response) {
            window.location.href = response['mail_to'];
             console.log(response)
        },
        error: function(error) {
            console.log(error);
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
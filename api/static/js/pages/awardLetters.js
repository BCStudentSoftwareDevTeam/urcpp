
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

function getAcceptLetter(pid) {
    $.ajax({
        url: '/chair/awardLetters/get/'+pid,
        dataType: 'json',
        type: 'GET',
        success: function(response) {
            
            var modal = $('#emailPreviewModal');
            modal.find('.modal-body').html(response['body'])
        },
        error: function(error) {
            console.log(error);
        }
    });
}

$('#emailPreviewModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var pid = button.data('pid') // Extract info from data-* attributes
  var faculty = button.data('name')
  var project_title = button.data('project-title')
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  getAcceptLetter(pid)
  modal.find('.modal-title').text(faculty + ' - ' + project_title)
//   modal.find('.modal-body input').val(recipient)
})
$(document).ready(function(){
    CKEDITOR.replace( 'body' );
    CKEDITOR.replace( 'message' );
});


function getProjects (username) {
  $.getJSON("/urcpp/v1/history/"+username, function( data ){
      //remove any table that might have been left behind
      $("#pastProjects").remove();
      $("#collaboratedProjects").remove();
      var tableheading = '<tr><th style = "padding-right: 25px;">Year</th><th>Project Name</th></tr>'
      var projectCaption = "Projects";
      var collaboratedCaption = "Collaborative Projects"
      if (data["primaryFaculty"].length){
        $('#projectModalBody').append('<table id="pastProjects" class="table table-striped"></table>');
        $("#pastProjects").prepend("<caption>"+projectCaption+"</caption>");
        $('#pastProjects').append(tableheading);
        $.each(data['primaryFaculty'], function(index, project) {
            $('#pastProjects').append("<tr><td style='padding-bottom: 10px;' >"+project.year.year+"</td><td style='padding-bottom: 10px;' ><a href='/urcpp/v1/project/"+project.pID+"/"+username+"/"+project.year.year+"'>"+project.title+"</a></td></tr>")
        });
      }
      if (data["collaborated"].length){
        $('#projectModalBody').append('<table id="collaboratedProjects" class="table"></table>');
        $("#collaboratedProjects").prepend("<caption>"+collaboratedCaption+"</caption>");
        $('#CollaboratedProjects').append(tableheading);
        $.each(data['collaborated'], function(index, project) {
            $('#collaboratedProjects').append("<tr><td>"+project.year.year+"</td><td><a href='/urcpp/v1/project/"+project.pID+"/"+username+"/"+project.year.year+"'>"+project.title+"</a></td></tr>")
        });
        
      }
      
      $("#myModal").modal("show");
  });
}


$("option[value='withdrawn']").attr("disabled", "disabled");

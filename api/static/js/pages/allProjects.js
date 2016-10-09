function getProjects (username) {
  $.getJSON("/urcpp/v1/history/"+username, function( data ){
      //remove any table that might have been left behinf
      $("#pastProjects").remove();
      $("#collaboratedProjects").remove();
      var tableheading = '<tr><th>Year</th><th>Project Name</th></tr>'
      var projectCaption = "Projects";
      var collaboratedCaption = "collaborated Projects"
      if (data["primaryFaculty"].length){
        $('#projectModalBody').append('<table id="pastProjects" class="table"></table>');
        $("#pastProjects").prepend("<caption>"+projectCaption+"</caption>");
        $('#pastProjects').append(tableheading);
        $.each(data['primaryFaculty'], function(index, project) {
            $('#pastProjects').append("<tr><td>"+project.year.year+"</td><td>"+project.title+"</td></tr>")
        });
      }
      if (data["collaborated"].length){
        $('#projectModalBody').append('<table id="collaboratedProjects" class="table"></table>');
        $("#collaboratedProjects").prepend("<caption>"+collaboratedCaption+"</caption>");
        $('#CollaboratedProjects').append(tableheading);
        $.each(data['collaborated'], function(index, project) {
            $('#collaboratedProjects').append("<tr><td>"+project.year.year+"</td><td><a href='#'>"+project.title+"</a></td></tr>")
        });
        
      }
      
      $("#myModal").modal("show");
  });
}
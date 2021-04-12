function filterProjectsByYear() {
  var yearDropdown = $("#yearDropdown");
  var yearSelected = $('option:selected', yearDropdown).attr('value');
  newUrl = "/committee/allProjects/" + yearSelected
  document.location.href = newUrl;
}

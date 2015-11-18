var Populate = {
  fromURL: function (endpoint) {
    $.getJSON(endpoint, {})
              .done (
                function (json) {
                   // console.log("DONE: " + json);
                  for (var key in json) {
                    if (json.hasOwnProperty(key)) {
                      $("#" + key).val(json[key])
                    }
                  }
                })
              .fail (
                function (jqxhr, textStatus, error) {
                  console.log ( jqxhr.responseText);
                  var err = textStatus + ", " + error;
                  console.log( "Request Failed: " + err );
                });
  }
}

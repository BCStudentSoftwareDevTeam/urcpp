// See both:
// * https://github.com/mattdesl/module-best-practices
// * https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/

var urcpp = function (version) {
  var h = {
    client: null,

    init: function (version) {
      console.log("Creating a version '" + version + "' client.");

      var c = new $.RestClient('/urcpp/' + version + '/');
      // Establish all of our endpoints.
      c.add('get', { isSingle: true });
      c.add('set', { isSingle: true });
      c.get.add('facultydetails', { stripTrailingSlash: true});
      c.show();

      h.client = c;
    },

    // All functions should take a single dictionary (object)
    // as an argument. It would be good if we used consistent
    // keys for those arguments. For the moment, I'm going
    // to use good commenting practice to make sure the
    // programmer knows which keys to include...

    // PARAMS
    //  username: string
    //  data: dictionary
    // PURPOSE
    // Gets faculty details.
    fd: function (params) {
      h.client.get.facultydetails.create (params.username, params.data).done (params.done);
    }
  };

  h.init(version);

  return h;
}

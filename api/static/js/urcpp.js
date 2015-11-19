// See both:
// * https://github.com/mattdesl/module-best-practices
// * https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/

var urcpp = function (version) {
  var h = {
    client: null,

    init: function (version) {
      h.client = new $.RestClient('/urcpp/' + version + '/');
      // Lets have some more sensible names for things.
      h.client.addVerb ('post', "POST");
      h.client.addVerb ('get', "GET");
      
      // Establish all of our endpoints.
      h.client.add('gfd', { stripTrailingSlash: true });
    },
    
    // PARAMS
    // username: string
    // data: dictionary
    // PURPOSE
    // Gets faculty details.
    gfd: function (params) {
      h.client.gfd.post(params.username, params.data).done (params.done);
    }
  };

  h.init(version);

  return h;
}

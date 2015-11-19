// See both:
// * https://github.com/mattdesl/module-best-practices
// * https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/

var urcpp = function (version) {
  var h = {
    client: null,

    init: function (version) {
      h.client = new $.RestClient('/urcpp/' + version + '/');
      // Establish all of our endpoints.
      h.client.add('gfd', { stripTrailingSlash: true});
    },

    gfd: function (username, data) {
      h.client.gfd.create(username, data);
    }
  };

  h.init(version);

  return h;
}

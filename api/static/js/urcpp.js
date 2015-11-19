// See both:
// * https://github.com/mattdesl/module-best-practices
// * https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/

var urcpp = function (version) {
  var h = {
    client: null,

    init: function (version) {
      h.client = new $.RestClient('/urcpp/' + version + '/');
    },

    gfd: function (username) {
      h.client.add('gfd', { stripTrailingSlash: true});
      h.client.gfd.create(username, { "foo" : "bar" });
    }
  };

  h.init(version);

  return h;
}

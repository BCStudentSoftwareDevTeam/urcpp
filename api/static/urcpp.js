var urcpp = {

  v1: new $.RestClient('/urcpp/1/'),

  gfd: function (username) {
    urcpp.v1.add('gfd', { stripTrailingSlash: true});
    urcpp.v1.gfd.create(username, { "foo" : "bar" });
  }
}

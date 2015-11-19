var urcpp = {

  client: new $.RestClient('/urcpp/1/'),

  gfd: function (username) {
    urcpp.client.add('gfd', { stripTrailingSlash: true});
    urcpp.client.gfd.create(username, { "foo" : "bar" });
  }
}

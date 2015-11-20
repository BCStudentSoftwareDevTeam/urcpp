var urcpp = function (version) {
  var h =  {
    faculty: {
      details: function (username, fun) {
        aja()
          .method ('POST')
          .url ('/urcpp/' + version + '/faculty/details/' + username)
          .body ( { username: username })
          .on ('success', fun).go();
      }
    }
  }

  return h;
};

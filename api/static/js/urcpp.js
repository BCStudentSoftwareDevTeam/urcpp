/* global aja */

var urcpp = function (version) {
  
  var url = function (ls) { return ls.join('/'); };

  var h =  {

    faculty: {
      details: function (username, fun) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'details', username]))
          .body ( { username: username })
          .on ('success', fun).go();
      }
    },
    
    project: {
      getTitle: function (username, fun) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'project', 'getTitle', username]))
          .body ({})
          .on ('success', fun).go();
      }
    }
  }

  return h;
};

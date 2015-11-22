/* global aja */

var urcpp = function (version) {
  
  var url = function (ls) { return ls.join('/'); };
  
  var addToQueue = function (version, postAction) {
    $(document).queue(version, function () {
      postAction.go();
    });
  }

  var dq = function (callback) {
    return function (data) {
      callback(data);
      $(document).dequeue(version);
    };
  }
  
  var h =  {
    go: function () {
      $(document).dequeue(version);
    },

    //////////////////////////////////////////////
    // FACULTY
    faculty: {
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'get', username]))
          .body ({})
          .on ('success', dq(callback) );
          
        addToQueue(version, post);
      },
      
      previousYearsFunded: function(username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'previousYearsFunded', username]))
          .body ({ })
          .on ('success', dq(callback));
          
        addToQueue(version, post);
      }
    },
    
    //////////////////////////////////////////////
    // PROGRAMS
    programs: {
      getAll: function (callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'programs', 'getAll']))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);  
      }
    },
    
    //////////////////////////////////////////////
    // PROJECTS
    projects: {
      getPossibleDurations: function (callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getPossibleDurations']))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'get', username]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      getNarrative: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getNarrative', username]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      getIRB: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getIRB', username]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      getAgencyAndServiceCommunity: function(username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'get', username]))
          .body ({ })
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
    },
    
    set: {
      start: function(username, body, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'set', 'start', username]))
          .body (body)
          .on ('success', dq(callback));
        addToQueue(version, post);
      }
    }
  }

  return h;
};

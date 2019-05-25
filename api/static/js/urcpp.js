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
      console.log ("Calling callback.");
      callback(data);
      console.log ("Dequeuing next.");
      $(document).dequeue(version);
    };
  }
  
  var h =  {
    go: function () {
      $(document).dequeue(version);
    },
    
    enqueue: function (fun) {
      addToQueue(version, fun);
    },
    
    showHidden: function (element) {
      var forqueue = { go: function () {
                              $("#" + element).show(); 
                            },
                      };
      addToQueue (version, forqueue );
    },
    
    checkBNumber: function (bnumber, callback) {
      var post = aja()
        .method ('POST')
        .url (url([version, 'checkBNumber', bnumber]))
        .body ({})
        .on ('success', dq(callback) );
      addToQueue(version, post);
    },
    
    
    /*
    //////////////////////////////////////////////
    // COLLABORATORS
    collaborators: {
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'collaborators', 'get', username]))
          .body ({})
          .on ('success', dq(callback) );
        addToQueue(version, post);
      }
    },
    
    //////////////////////////////////////////////
    // FACULTY
    faculty: {
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'faculty', 'get', username]))
          .body ({})
          .on ('success', dq(callback) );
          
        addToQueue(version, post);
      },
      

      
      
    },
    
    //////////////////////////////////////////////
    // PROGRAMS
    programs: {
      getAll: function (callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'programs', 'getAll']))
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
          .url (url([version, 'projects', 'getPossibleDurations']))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'projects', 'get', username]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      getNarrative: function (username, path, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'projects', 'getNarrative', username, path]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      getIRB: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'projects', 'getIRB', username]))
          .body ({})
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      getAgencyAndServiceCommunity: function(username, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'projects', 'get', username]))
          .body ({ })
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
    },
    
    set: {
      create: function(username, body, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'set', 'create', username]))
          .body (body)
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      people: function(username, body, callback) {
        var post = aja()
          .method ('POST')
          .url (url([version, 'set', 'people', username]))
          .body (body)
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
    }
    */
  }

  return h;
};

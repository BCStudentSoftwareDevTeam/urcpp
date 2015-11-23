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
    constants: {
      alertEmail: "heggens@berea.edu"
    },
    
    next: function () {
      var sequence = {  "start.html"      : "/t/create.html",
                        "create.html"     : "/t/people.html",
                        "people.html"     : "/t/budget.html",
                        "budget.html"     : "/t/vitae.html",
                        "vitae.html"      : "/t/narrative.html",
                        "narrative.html"  : "/t/done.html"
                      };
      var current = document.location.href.match(/[^\/]+$/)[0];
      console.log("Current Page: " + current);
      return sequence[current];
    },
    
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

    
    //////////////////////////////////////////////
    // COLLABORATORS
    collaborators: {
      get: function (username, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'collaborators', 'get', username]))
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
          .url (url(['/urcpp', version, 'faculty', 'get', username]))
          .body ({})
          .on ('success', dq(callback) );
          
        addToQueue(version, post);
      },
      
      checkBNumber: function (bnumber, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'checkBNumber', bnumber]))
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
      create: function(username, body, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'set', 'start', username]))
          .body (body)
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
      people: function(username, body, callback) {
        var post = aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'set', 'people', username]))
          .body (body)
          .on ('success', dq(callback));
        addToQueue(version, post);
      },
      
    }
  }

  return h;
};

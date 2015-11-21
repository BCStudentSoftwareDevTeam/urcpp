/* global aja */

var urcpp = function (version) {
  
  var url = function (ls) { return ls.join('/'); };

  var h =  {

    //////////////////////////////////////////////
    // FACULTY
    faculty: {
      details: function (username, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'details', username]))
          .body ( { username: username })
          .on ('success', callback).go();
      },
      
      previousYearsFunded: function(username, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'faculty', 'previousYearsFunded', username]))
          .body ({ })
          .on ('success', callback).go();
      }
    },
    
    //////////////////////////////////////////////
    // PROGRAMS
    programs: {
      getAll: function (callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'programs', 'getAll']))
          .body ({})
          .on ('success', callback).go();
      }
    },
    
    //////////////////////////////////////////////
    // PROJECTS
    projects: {
      getPossibleDurations: function (callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getPossibleDurations']))
          .body ({})
          .on ('success', callback).go();
      },
      
      getProject: function (username, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getProject', username]))
          .body ({})
          .on ('success', callback).go();
      },
      
      getNarrative: function (username, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getNarrative', username]))
          .body ({})
          .on ('success', callback).go();
      },
      
      getIRB: function (username, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'projects', 'getIRB', username]))
          .body ({})
          .on ('success', callback).go();
      },
    },
    
    
    set: {
      start: function(username, body, callback) {
        aja()
          .method ('POST')
          .url (url(['/urcpp', version, 'set', 'start', username]))
          .body (body)
          .on ('success', callback).go();
      }
    }
  }

  return h;
};

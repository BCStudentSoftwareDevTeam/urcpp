// See both:
// * https://github.com/mattdesl/module-best-practices
// * https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/

var urcpp = function (version) {
  var h = {
    client: null,
    getter: null,
    
    init: function (version) {
      h.client = new $.RestClient('/urcpp/' + version + '/');
                                  
      // Lets have some more sensible names for things.
      h.client.addVerb ('p', "POST");
      h.client.addVerb ('g', "POST");
      // Establish all of our endpoints.
      h.client.add('get', { isSingle: true });
      h.client.add('set', { isSingle: true });
      h.getter = h.client.get;
      h.setter = h.client.set;
      
      h.getter.add('facultydetails', { stripTrailingSlash: true});
      h.client.show();

      
    },
    
    // All functions should take a single dictionary (object)
    // as an argument. It would be good if we used consistent
    // keys for those arguments. For the moment, I'm going
    // to use good commenting practice to make sure the 
    // programmer knows which keys to include...
    
    // PARAMS
    //  username: string
    //  data: dictionary
    // PURPOSE
    // Gets faculty details.
    facultydetails: function (params) {
      h.getter.get(params.username, params.data).done (params.done);
    }
  };

  h.init(version);

  return h;
}

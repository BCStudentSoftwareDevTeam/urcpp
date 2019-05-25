## What is Aja?

Aja is short for AJAX, which stands for *Asynchronous Javascript and XML*. AJAX is a term that is thrown around whenever we have a webpage that makes a request to a server and immediately continues doing other things. When the server finally gets around to sending a response, we handle it. This is the "asynchronous" part, because we don't pause and wait.

There are lots of ways to have JavaScript talk to a server, but we're going to use Aja. For example, inside of our JavaScript tags, we might write:

```javascript
var show = function (data) {
  console.log(data);
};

urcpp.getmeaning().done(show);
```

We have created a URCPP object that will "hide" or "wrap" all of our work with Aja. For example, this shows how we can call the "getmeaning()" method on the URCPP object, and when we are done, we can then call the "show" function with the resulting data. In this case, we can expect the number 42 to show up on the developer console in our browser.

Inside of the URCPP object, we might find the following code:

```javascript
getmeaning: function (fun) {
  aja()
    .method ('GET')
    .url (url(['/getmeaning']))
    .on ('success', fun).go();
};
```
The aja() method returns an object that we then invoke some member functions of. For example, we set the type of our interaction to GET, we set the URL we're going to talk to, and we define what to do if things are successful. Specifically, we say that we want to use the function called **fun** that the user passed in to us. (In this running example, it would mean we call the function **show** with one argument, which is the data that came back.)

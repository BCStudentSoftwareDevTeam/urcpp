# What is Flask?

Flask is a "web framework" written in Python. That means that we're developing the server-side in Python, and using a big library of code to make things easier.

## ReST

We are also implementing things as a RESTful API. (ReST stands for *Representational State Transfer*, and is a fancy way of saying "we send data back and forth between the client and server using HTTP.) This means that we are attaching functionality to URLs, and when our client (the web page) talks to our server, we will do one thing, and one thing only, in response to that request.

For example, if I wanted to write a REST handler that replied with the number 42, I would write the following in Flask:

```python
@app.route('/getmeaning', methods = ['GET', 'POST'])
def get_meaning ():
  return 42
```
The "route" defines what URL will trigger the subsequent function. In this case, if someone does an HTTP GET or POST to the URL http://server.edu/getmeaning, we will then return the number 42.

This would be a boring web page, but it is great if we have some JavaScript in our webpage that wants to know the meaning of life.

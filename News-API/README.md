NEWS-API key project in pyhton includes use of requests module,JSON module and time module, 

To Read/Speak the News,Speak function from pywin32 module is used. 

Speak function takes string type as argument.

requests.get() is used to get the JSON type format from the API-Key(link).

loads function will convert The JSON type to Dictionary Type.

Then we can pass the value pair of the dictionary as argumnet to Speak function.

time.sleep() is used to take a gap between two consecutive News headlines.

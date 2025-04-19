Framework Chosen
Fast API

Reasoning: Since this is a python specialsit position so i wanted to attempt it in python. Django would have been overkill for this small application and that left me with only 2 options , Flask and FastAPI Since FastAPI is considerably faster , I went with it.

Database chosen
MongoDB

Reasoning: NoSQl dbs are faster and I inteded to use the indexing of the mongo to optimize searching.

Special Adjustment for speed
I used the short url as the id for the collection so that lookup would be in O(1) time complexity and this also makes sure that the short url is unique otherwise it would throw an error.

Design pattern
Design Pattern used is Layered Architecture Pattern as the code is separated into layers and into an MVC like strucuture (But not exact MVC). This would ensure that code is easier to read and extend and even increase reusablity.

How to run
Make an env file in the backend folder and copy this (Or whatever host your mongo server is running on) "MONGO_URI=mongodb://localhost:27017"

Install requirement by this command "pip install -r requirements.txt"

In the backend folder, run this command "python app.py"

Go to the front end folder and run the index.html using the "live server" option in VS CODE.

Ignore the "file://" prefix in the shortned url, you only need the 6 letter code

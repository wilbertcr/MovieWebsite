# **Full Stack Web Developer**
# Project 1: Movie Trailer Website 

Description: "You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then serve this data as a web page allowing visitors to review their movies and watch the trailers."

As per the project, the content was to be collected manually and then arranged into a webpage.  

Instead of doing it that way, I used a wrapper library https://github.com/celiao/tmdbsimple/ to access https://www.themoviedb.org's database and get the content via their public API. That way, I don't decide on the movies that will be displayed, you, the user, picks his/her favorites. 

# Installation

All you need is python 2 or 3, I think it works on both. 

The user runs:

```$python entertainment_center.py```

The code asks the user for a series of movie titles like so:

```
Please enter the title of a movie, or "exit" to complete your selection.
Robocop
Please enter the title of a movie, or "exit" to complete your selection.
Lord of the rings
Please enter the title of a movie, or "exit" to complete your selection.
Love actually
Please enter the title of a movie, or "exit" to complete your selection.
Toy Story
Please enter the title of a movie, or "exit" to complete your selection.
Star Wars
Please enter the title of a movie, or "exit" to complete your selection.
exit
```

Then you should see something like this:

![alt tag](https://raw.githubusercontent.com/wilbertcr/MovieWebsite/master/Movie%20Trailer%20Screen%20Shot.PNG)

It then uses them to query www.themoviedb.org's database and get the story line, a link to the movie poster and a link to its trailer. Then it uses that to construct Movie objects. The movie objects are then placed on a list that is fed to fresh_tomatoes.py, which renders the website. 

#Dependencies:
https://github.com/celiao/tmdbsimple/

Code uses API from: 
https://www.themoviedb.org/documentation/api
**You will need to create an account to get the key, but it's free!**
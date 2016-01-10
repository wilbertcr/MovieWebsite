# MovieWebsite
The Movie Trailer Website project consists of server-side code to create a webpage displaying:

- The Movie Title
- The Story Line
- The Movie's Poster
- The Movie's Trailer

The code relies on wrapper library https://github.com/celiao/tmdbsimple/ to access https://www.themoviedb.org's API. 

The code asks the user for a series of movie titles and uses them to query www.themoviedb.org's database to get the story line, a link to the movie poster and a link to its trailer. Then it uses that to construct Movie objects. The movie objects are then placed on a list, which is fed to fresh_tomatoes.py so it can render the website. 

#Dependencies:
https://github.com/celiao/tmdbsimple/

Code uses API from:
https://www.themoviedb.org/documentation/api


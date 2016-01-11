# MovieWebsite
The Movie Trailer Website project consists of server-side code to create a webpage displaying:

- The Movie Title
- The Story Line
- The Movie's Poster
- The Movie's Trailer

The code relies on wrapper library https://github.com/celiao/tmdbsimple/ to access https://www.themoviedb.org's API. 

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

It then uses them to query www.themoviedb.org's database to get the story line, a link to the movie poster and a link to its trailer. Then it uses that to construct Movie objects. The movie objects are then placed on a list, which is fed to fresh_tomatoes.py which renders the website. 

#Dependencies:
https://github.com/celiao/tmdbsimple/

Code uses API from, you will need to create an account to get the key, but it's free!
https://www.themoviedb.org/documentation/api

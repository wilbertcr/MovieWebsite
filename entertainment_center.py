import fresh_tomatoes
import media
import tmdb_key
import tmdbsimple as tmdb

tmdb = tmdb_key.set_key(tmdb)

# Get Search Object
search = tmdb.Search()

# We need to get the base path for the movie posters.
# See http://docs.themoviedb.apiary.io/#reference/configuration/configuration/get
#  for information on what's going on here.
information = tmdb.Configuration().info()
images_info = information['images']
IMG_BASE_URL = images_info['secure_base_url']
sizes = images_info['backdrop_sizes']
IMG_SIZE = sizes[3]
POSTER_BASE_PATH = IMG_BASE_URL + IMG_SIZE

YOUTUBE_BASE_PATH = "https://www.youtube.com/watch?v="

# This list will hold the titles given by the user.
movies_titles = []

# Ask the user for the titles.
while True:
    movie = raw_input("Please enter the title of a movie, or \"exit\" to complete your selection.\n")
    if movie == "":
        print "Empty argument. Ignored"
    elif movie.lower() == "exit":
        break
    else:
        movies_titles.append(movie)

# This list will hold the movie instances.
movie_list = []

not_found = media.Movie("404: Not found",
                        "The 404 or Not Found error message is an HTTP standard response code indicating that the client was able to communicate with a given server, but the server could not find what was requested",
                        "https://image.tmdb.org/t/p/original/zPhsCyhmRLNl8Fbr8EUccXVGvtu.jpg",
                        "https://youtu.be/5TxnwlDn7w0")
# Here we query the database using the movie titles and get the other attributes we need for each title.
count = 0
# For each movie in the list
for movie in movies_titles:
    # Let's query the DB.
    response = search.movie(query=movie)

    # And let's use the first result to populate attributes.

    for s in response['results']:
        try:
            movie_id = s["id"]
            title = s["title"]
            overview = s["overview"]
            poster_path = POSTER_BASE_PATH + s["poster_path"]
            movies = tmdb.Movies(id=movie_id)
            trailers = movies.videos(id=movie_id)
            trailer = trailers["results"][0]
            youtube_path = "Test"
            youtube_path = YOUTUBE_BASE_PATH + trailer["key"]
            current_movie = media.Movie(title, overview, poster_path, youtube_path)
            movie_list.append(current_movie)
            count += 1
            break
        except:
            pass

# If we didn't get any usable results. Display the "error" movie :).
if count == 0:
    movie_list.append(not_found)

# Display the movies we found.
fresh_tomatoes.open_movies_page(movie_list)

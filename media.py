import webbrowser


# This code was pretty much given by the Lesson referenced by the course material.as

# Class declaration

class Movie:
    # Constructor
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        """

        :rtype: object
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open default browser's window and displays trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

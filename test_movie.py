from unittest import TestCase

import media


class TestMovie(TestCase):
    def test_movie(self):
        toy_story = media.Movie("Toy Story",
                                "A story of a boy and his toys that come to life.",
                                "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                                "https://www.youtube.com/watch?v=KYz2wyBy3kc")
        self.assertEqual(toy_story.title, "Toy Story", "Should be Toy Story")
        pass

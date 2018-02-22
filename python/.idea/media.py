#this is the parent class.
import webbrowser
class Movie():
    #this is the constructor. self is the instance of that variable.
    #in which case from toy story, self = toy_story.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
print(Movie.__name__ + "  " + Movie.__module__)
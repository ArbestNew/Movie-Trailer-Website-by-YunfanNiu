
class Movie():
    """A class to describe a movie, store its properties.
    """
    def __init__(self,movie_title,movie_story_line,poster_image,trailer_youtube,movie_year,movie_duration):
        #content will be render on the page
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.story_line = movie_story_line
        self.year = movie_year
        #content will be skip on the page
        self.duration = movie_duration
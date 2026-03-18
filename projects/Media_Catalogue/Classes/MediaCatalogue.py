from Classes.TVSeries import TVSeries
from Classes.Movie import Movie
from Errors.MediaError import MediaError

class MediaCatalogue:
    # """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        
        if series:
            result += '=== TV SERIES ===\n'
            for i, item in enumerate(series, 1):
                result += f'{i}. {item}\n'

        return result
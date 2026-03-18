from Classes.Movie import Movie

class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

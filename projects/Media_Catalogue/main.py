from Classes.MediaCatalogue import MediaCatalogue
from Classes.Movie import Movie
from Classes.TVSeries import TVSeries
from Errors.MediaError import MediaError
def main():
    catalogue = MediaCatalogue()

    try:
        movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
        movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
        catalogue.add(movie1)
        catalogue.add(movie2)

        series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
        series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
        catalogue.add(series1)
        catalogue.add(series2)

        print(catalogue)
    except ValueError as e:
        print(f'Validation Error: {e}')
    except MediaError as e:
        print(f'Media Error: {e}')
        print(f'Unable to add {e.obj}: {type(e.obj)}')

if __name__ == '__main__':
    main()
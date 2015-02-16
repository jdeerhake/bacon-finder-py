from actor import Actor
from movie import Movie
from performance import Performance

def format_data(str):
  return str.rstrip().split('|')

def get_actors():
  actor_data = open('data/actors.txt', 'r').readlines()
  actors = map(lambda data: Actor(data[0], data[1]), map(format_data, actor_data))
  return dict([(actor.id, actor) for actor in actors])

def get_movies():
  movie_data = open('data/movies.txt', 'r').readlines()
  movies = map(lambda data: Movie(data[0], data[1]), map(format_data, movie_data))
  return dict([(movie.id, movie) for movie in movies])

def get_performances():
  perf_data = open('data/movie-actors.txt', 'r').readlines()
  return map(lambda data: Performance(data[0], data[1]), map(format_data, perf_data))

movies = get_movies()
actors = get_actors()
performances = get_performances()


print actors[4].name
print movies[2].name
#print [actor.name for actor in get_actors()]
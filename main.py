from actor import Actor
from movie import Movie
from performance import Performance

def format_data(str):
  return str.rstrip().split('|')

def get_actors():
  actor_data = map(format_data, open('data/actors.txt', 'r').readlines())
  actors = map(lambda data: Actor(data[0], data[1]), actor_data)
  return dict([(actor.id, actor) for actor in actors])

def get_movies():
  movie_data = map(format_data, open('data/movies.txt', 'r').readlines())
  movies = map(lambda data: Movie(data[0], data[1]), movie_data)
  return dict([(movie.id, movie) for movie in movies])

def get_performances(movies, actors):
  perf_data = map(format_data, open('data/movie-actors.txt', 'r').readlines())
  perfs = map(lambda data: Performance(movies[int(data[0])], actors[int(data[1])]), perf_data)
  map(lambda perf: perf.actor.add_performance(perf), perfs)
  map(lambda perf: perf.movie.add_performance(perf), perfs)
  return perfs

movies = get_movies()
actors = get_actors()
performances = get_performances(movies, actors)


start = actors[4]
end = actors[63]


print start.worked_with(end)

# outut = start.name + ' costarred with '
# if start in end.costars():
#   output += end.name
# else
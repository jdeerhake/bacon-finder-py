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

def show_path(start, end):
  path = start.bfs_path(end)
  if path is None:
    print 'No connection between ' + start.name + ' and ' + end.name + '\n'
    return
  last = path.pop(0)
  output = last.name + '\n'
  for current in path:
    movie = current.worked_with_in(last)
    output += '  appeared in ' + movie.name + ' with\n' + current.name + '\n'
    last = current
  print output

def get_input():
  f = raw_input('First actor: ')
  s = raw_input('Second actor: ')
  print
  show_path(actors_by_name[f], actors_by_name[s])

movies = get_movies()
actors = get_actors()
actors_by_name = dict([(actor.name, actor) for actor in actors.values()])
performances = get_performances(movies, actors)

for actor in actors.values():
  kevin = actors_by_name['Kevin Bacon']
  path = actor.bfs_path(kevin)
  print actor.name + ': ' + str(len(path)) if path != None else 'no path'

# while 1:
#   get_input()
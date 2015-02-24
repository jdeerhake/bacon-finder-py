import sys
import data

def get_path_desc(start, end):
  print str(start.id) + " " + str(end.id)
  path = start.bfs_path(end)
  if path is None:
    return 'No connection between ' + start.name + ' and ' + end.name + '\n'
  last = path.pop(0)
  output = last.name + '\n'
  for current in path:
    movie = current.worked_with_in(last)
    output += '  appeared in ' + movie.name + ' with\n' + current.name + '\n'
    last = current
  return output

def get_separation_num(start, end):
  path = start.bfs_path(end)
  if path is None:
    return path
  else:
    return len(path) - 1

def get_input():
  f = raw_input('First actor: ')
  s = raw_input('Second actor: ')
  print
  print get_path_desc(actors_by_name[f], actors_by_name[s])

def benchmark(type):
  tests = list([
               [593, 11532, 2],
               [63, 4792, 8],
               [63, 63, 0],
               [63, 11486, 7],
               [63, 515, None],
               [7060, 4251, 10],
               [6205, 9029, 7],
               [647, 6205, 4],
               [408, 407, 1],
               [143, 10744, 5]
               ])

  for params in tests:
    actor1 = actors[params[0]]
    actor2 = actors[params[1]]
    expected_separation = params[2]
    fwd_separation = get_separation_num(actor1, actor2);
    rev_separation = get_separation_num(actor2, actor1);
    if fwd_separation != expected_separation:
      raise Exception("Expected " + actor1.name + " and " + actor2.name + " to have " + str(expected_separation) + " degrees of separation. Got: " + str(fwd_separation))
    elif rev_separation != expected_separation:
      raise Exception("Expected " + actor2.name + " and " + actor1.name + " to have " + str(expected_separation) + " degrees of separation. Got " + str(fwd_separation))
    else:
      [get_separation_num(actor1, actor2) for n in range(9)]
      [get_separation_num(actor2, actor1) for n in range(9)]

def get_all_separation(base_actor):
  print "separations for " + base_actor.name
  for actor in actors.values():
    sep = get_separation_num(actor, base_actor)
    print "\"" + actor.name + "\",\"" + str(sep) + "\""


movies = data.get_movies()
actors = data.get_actors()
actors_by_name = dict([(actor.name, actor) for actor in actors.values()])
performances = data.get_performances(movies, actors)


if sys.argv[1] == "benchmark":
  benchmark("short")
elif sys.argv[1] == "get_all":
  id = int(sys.argv[2])
  get_all_separation(actors[id])
else:
  while 1:
    get_input()
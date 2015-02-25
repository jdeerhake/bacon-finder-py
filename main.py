import sys
import data
import csv
import benchmark
import utils

def get_input():
  f = raw_input('First actor: ')
  s = raw_input('Second actor: ')
  print
  print utils.path_desc(actors_by_name[f], actors_by_name[s])

def tree_stats(actors):
  utils.print_csv_line([ "id", "name", "total nodes", "long path", "avg path" ])
  for actor in actors.values():
    sys.stderr.write(str(actor.id) + '\n')
    stats = actor.tree_stats()
    utils.print_csv_line([ actor.id, actor.name, stats['total_nodes'], stats['longest_path'], stats['average_path'] ])


movies = data.get_movies()
actors = data.get_actors()
actors_by_name = dict([(actor.name, actor) for actor in actors.values()])
performances = data.get_performances(movies, actors)


arg1 = sys.argv[1]
if arg1 == "benchmark":
  benchmark.short(actors)
elif arg1 == "list_all":
  name = sys.argv[2]
  utils.get_all_separations(actors_by_name[name], actors)
elif arg1 == "tree_stats":
  tree_stats(actors)
elif arg1 == "interactive":
  while 1:
    get_input()

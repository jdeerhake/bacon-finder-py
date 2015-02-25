def get_separation_num(start, end):
  path = start.find_link(end)
  if path is None:
    return path
  else:
    return len(path) - 1

def print_csv_line(info_list):
  print reduce(lambda cumul, data: cumul + '"' + str(data) + '",', info_list, "")

def path_desc(start, end):
  path = start.find_link(end)
  if path is None:
    return 'No connection between ' + start.name + ' and ' + end.name + '\n'
  last = path.pop(0)
  output = last.name + '\n'
  for current in path:
    movie = current.worked_with_in(last)
    output += '  appeared in ' + movie.name + ' with\n' + current.name + '\n'
    last = current
  return output

def get_all_separations(base_actor, actors):
  print_csv_line([ "Separations for " + base_actor.name + " (" + str(base_actor.id) + ")" ])
  for actor in actors.values():
    sep = get_separation_num(base_actor, actor)
    print_csv_line([ actor.id, actor.name, sep ])
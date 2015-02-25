class Actor:

  def __init__(self, id, name):
    self.name = name
    self.id = int(id)
    self.performances = []

  def add_performance(self, perf):
    self.performances.append(perf)

  def movies(self):
    return [perf.movie for perf in self.performances]

  def costars(self):
    return set(reduce(lambda x, y: x + y, [movie.actors() for movie in self.movies()]))

  def worked_with(self, actor):
    return actor in self.costars()

  def worked_with_in(self, actor):
    return next(movie for movie in self.movies() if movie.has_actor(actor))

  def find_link(self, actor):
    return self.__tree_paths(actor)

  def tree_stats(self):
    paths = self.__tree_paths(None)
    paths_lens = sorted([len(path) for path in paths])
    return {
      'total_nodes' : len(paths),
      'longest_path' : paths_lens[-1],
      'average_path' : round(sum(paths_lens) / float(len(paths_lens)), 3)
    }

  def __tree_paths(self, goal):
    if self == goal:
      return [self]
    seen = set([self])
    queue = [[self]]
    saved_paths = [[self]]
    while queue:
      path = queue.pop(0)
      actor = path[-1]
      unseen_actors = actor.costars() - seen
      if goal in unseen_actors:
        return path + [goal]
      seen.update(unseen_actors)
      paths = [path + [a] for a in unseen_actors]
      if goal is None:
        saved_paths.extend(paths)
      queue.extend(paths)
    if goal is None:
      return saved_paths
    else:
      return None
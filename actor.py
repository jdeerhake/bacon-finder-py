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

  def tree(self):
    seen = set()
    tree = dict()
    queue = [self]
    while queue:
      actor = queue.pop(0)
      if actor not in seen:
        seen.add(actor)
        tree[actor] = actor.costars() - seen
        queue.extend(tree[actor])
    return tree

  def bfs_path(self, goal):
    if self == goal:
      return [self]
    graph = self.tree()
    queue = [(self, [self])]
    while queue:
      (vertex, path) = queue.pop(0)
      for next in graph[vertex] - set(path):
        if next == goal:
          return path + [next]
        else:
          queue.append((next, path + [next]))
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
    return self.__bfs_path(actor)

  def __tree(self):
    seen = set()
    tree = dict()
    queue = [self]
    while queue:
      actor = queue.pop(0)
      if actor not in tree:
        seen.add(actor)
        unseen_actors = actor.costars() - seen
        tree[actor] = unseen_actors
        seen.update(unseen_actors)
        queue.extend(tree[actor])
    return tree

  def __bfs_path(self, goal):
    if self == goal:
      return [self]
    graph = self.__tree()
    queue = [(self, [self])]
    while queue:
      (vertex, path) = queue.pop(0)
      for next in graph[vertex] - set(path):
        if next == goal:
          return path + [next]
        else:
          queue.append((next, path + [next]))
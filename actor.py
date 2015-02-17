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
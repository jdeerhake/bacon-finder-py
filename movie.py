class Movie:

  def __init__(self, id, name):
    self.name = name
    self.id = int(id)
    self.performances = []

  def add_performance(self, perf):
    self.performances.append(perf)

  def actors(self):
    return [perf.actor for perf in self.performances]
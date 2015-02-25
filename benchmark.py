import utils

def short(actors):
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
    fwd_separation = utils.get_separation_num(actor1, actor2);
    rev_separation = utils.get_separation_num(actor2, actor1);
    if fwd_separation != expected_separation:
      raise Exception("Expected " + actor1.name + " and " + actor2.name + " to have " + str(expected_separation) + " degrees of separation. Got: " + str(fwd_separation))
    elif rev_separation != expected_separation:
      raise Exception("Expected " + actor2.name + " and " + actor1.name + " to have " + str(expected_separation) + " degrees of separation. Got " + str(fwd_separation))
    else:
      [utils.get_separation_num(actor1, actor2) for n in range(9)]
      [utils.get_separation_num(actor2, actor1) for n in range(9)]
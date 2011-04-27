def no_zero_range(end):
  """
  A range function, that that goes from 1 to end.


  >>> no_zero_range(0)
  []

  >>> no_zero_range(1)
  [1]

  >>> no_zero_range(3)
  [1, 2, 3]

  >>> no_zero_range(5)
  [1, 2, 3, 4, 5]
  """

  if end == 0:
    return []

  L = range(end)[1:]
  L.append(end)
  return L


def frange(start, end=None, inc=1.0):
  """
  A range function, that accept float increments. Differently of built-in
  range, this function include the end limit.


  >>> frange(3)
  [0.0, 1.0, 2.0, 3.0]

  >>> frange(2,5)
  [2.0, 3.0, 4.0, 5.0]

  >>> frange(0,1,0.2)
  [0.0, 0.20000000000000001, 0.40000000000000002, 0.60000000000000009, 0.80000000000000004, 1.0]

  >>> frange(1,None,0.2)
  [0.0, 0.20000000000000001, 0.40000000000000002, 0.60000000000000009, 0.80000000000000004, 1.0]
  """

  if end == None:
    end = start + 0.0
    start = 0.0

  L = []
  while 1:
    next = start + len(L) * inc
    if inc > 0 and next > end:
      break
    elif inc < 0 and next < end:
      break
    L.append(next)
  return L

if __name__ == "__main__":
  import doctest
  doctest.testmod()


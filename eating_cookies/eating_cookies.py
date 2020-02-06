#!/usr/bin/python

import sys

# Base case
# valid path returns 1


def eating_cookies(n, cache=None):
  # Base case
  # Valid path
  if n == 0:
    return 1
# invalid path returns -n
  elif n < 0:
    return 0
  # Check for cache
  elif cache and cache[n] > 0:
    return cache[n]

# recursive solution
  else:
      if not cache:
        cache = {i: 0 for i in range(n+1)} #{n: num_ways_to_eat}
      cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
      return cache[n]
        
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
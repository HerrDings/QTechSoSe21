#!/bin/python3
# quick and dirty, but it works :)

import random
import math

def euclid(a,b):
  if b == 0:
    return a
  if a == 0:
    return b
  if a > b:
    return euclid(a-b,b)
  return euclid(a,b-a)
  
def ourSimpleAlgorithm(N):
  # step a

  a = random.randrange(1,N) # yes, this is < N 

  # step b
  luckyshot = euclid(a,N)
  if luckyshot != 1:
    return luckyshot

  # step c
  # this is tricky b/c (a^x)%N does not have a overall-periodicity
  # but the periodicity decreases with increasing x. Thus this program
  # will identify the very first x for which the modulus becomes
  # relevant
  r = math.log(N)/math.log(a)
  # I do not belive that this is the right way, b/c it is very un-
  # likely to result in integers. Whatsoever, I have no better idea.

  # step d
  if r%2!=0:
    return ourSimpleAlgorithm(N)
  ar = math.pow(a,r/2)
  if a == -1%N:
    return ourSimpleAlgorithm(N)


  
 

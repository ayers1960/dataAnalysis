import numpy as np

def calculate(list):
  if len(list) !=  9:
    return "List must contain nine numbers."
  calculations = []
  x  = np.array(list).reshape([3,3])
  print(x)
  mean = [x.mean(axis=0),x.mean(axis=1),x.flatten().mean()]
  print(mean)




  return calculations

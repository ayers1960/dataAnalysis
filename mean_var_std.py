import numpy as np

def calculate(list):
  if len(list) !=  9:
    return "List must contain nine numbers."
  calculations = {}
  x  = np.array(list).reshape([3,3])
  print(x)
  mean     = [x.mean(axis=0).tolist(),x.mean(axis=1).tolist(),x.flatten().mean()]
  variance = [x.var(axis=0).tolist(),x.var(axis=1).tolist(),x.flatten().var()]
  std      = [x.std(axis=0).tolist(),x.std(axis=1).tolist(),x.flatten().std()]  
  max      = [x.max(axis=0).tolist(),x.max(axis=1).tolist(),x.flatten().max()]   
  min      = [x.min(axis=0).tolist(),x.min(axis=1).tolist(),x.flatten().min()]   
  sum      = [x.sum(axis=0).tolist(),x.sum(axis=1).tolist(),x.flatten().sum()]   
  calculations["mean"] = mean
  calculations["variance"] = variance
  calculations["std"] = std
  calculations["max"] = max
  calculations["min"] = min
  calculations["sum"] = sum
  return calculations

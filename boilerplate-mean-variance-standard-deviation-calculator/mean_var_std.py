import numpy as np
import pandas as pd

def calculate(list):
    
  try:
    arr = np.array([list[0:3],list[3:6], list[6:9]], dtype=float)
    list_mean = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
  
    list_var = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()]

    list_std = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std()]

    arr2 = np.array([list[0:3],list[3:6], list[6:9]], dtype=int)
    list_max = [arr2.max(axis=0).tolist(), arr2.max(axis=1).tolist(), arr2.max()]

    list_min = [arr2.min(axis=0).tolist(), arr2.min(axis=1).tolist(), arr2.min()]

    list_sum = [ arr2.sum(axis=0).tolist(), arr2.sum(axis=1).tolist(), arr2.sum()]

    calculations = {'mean':list_mean, 'variance':list_var, 'standard deviation':list_std, 'max':list_max, 'min':list_min, 'sum':list_sum}
  except ValueError:
    raise ValueError("List must contain nine numbers")  
  
  return calculations

import math

def compare(a,b,sigma=1.0):
    return 1-math.exp(-0.5*(pow((a-b)/sigma,2)))

import math
import heinrich.heinrichInteger as hInt

def gausCompareTwoValues(original, anonym, sigma = 1.0):
    if original == anonym:
        return 0.0
    else:
        return 1.0 - math.exp(-0.5*pow(((abs(anonym-original))/sigma),2.0))

def compare(a, b, sigma=1.0):
    day = gausCompareTwoValues(a.day, b.day)
    month = gausCompareTwoValues(a.month, b.month)
    year = hInt.compare(a.year, b.year)
    return (day+month+year)/3
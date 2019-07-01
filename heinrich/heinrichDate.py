import math
import heinrich.heinrichInteger as hInt


def gausCompareTwoValues(original, anonym, sigma):
    if original == anonym:
        return 0.0
    else:
        return 1.0 - math.exp(-0.5 * pow(((abs(anonym - original)) / sigma), 2.0))


def compare(a, b, sigmaDay, sigmaMonth):
    day = gausCompareTwoValues(a.day, b.day, sigmaDay)
    month = gausCompareTwoValues(a.month, b.month, sigmaMonth)
    year = hInt.compare(a.year, b.year)
    return (day + month + year) / 3

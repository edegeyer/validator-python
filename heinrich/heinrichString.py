import math
import heinrich
import re
import collections


def compareString(a, b, sigma):
    regexA = re.compile("\\d+")
    regexB = re.compile("\\D+")
    if regexA.match(a) and regexB.match(b):
        print("a and be are digit", a)
        return 0.0
    elif regexA.match(b) and regexB.match(a):
        print("a and be are digit 2", a)
        return 0.0
    regexA = re.compile("^\\d+[a-zA-Z][a-zA-Z\\d]*$")
    if regexA.match(a) and regexA.match(b):
        print("insurance number ", a)
        if len(a) == 12 and len(b) == 12:
            x = a[8,10] # dífferent to java (8,9) as end character is exclusive
            y = b[8,10]
            regexA = re.compile("[a-zA-Z]")
            if regexA.match(a) and regexA.match(b):
                return heinrich.heinrichInsurance.compare(a,b, sigma)
    regexA = re.compile("[A-z]+[0-9]$")
    if regexA.match(a) and regexA.match(b):
        print("string followed by number", a)
        return 0.0
    regexA = re.compile("[0-9 ]+")
    if regexA.match(a) and regexA.match(b):
        print("something with numbers ", regexA)
        return 0.0
    length = compareLength(a,b, sigma)
    if a.lower() in b.lower() or b.lower() in a.lower():
        content = 0.0
    else:
        content = compareContent(a, b, sigma)
    return 0.5 * (length + content)



def compareLength(a, b, sigma):
    length = abs(len(a) - len(b))
    return 1.0 - (math.exp(-0.5 * (math.pow(length/sigma, 2))))


def compareContent(a, b, sigma):
    order = compareOrder(a, b, sigma)
    distribution = compareDistribution(a, b, sigma)
    return 0.5 * (order + distribution)


def compareOrder(a, b, sigma):
    transpostions = getTranspositions(a, b)
    if transpostions.__len__() == 0:
        return 0.0
    sum = 0.0
    for i in transpostions:
        sum = sum + (1.0 - math.exp(-0.5 * math.pow(i / sigma, 2.0)))
    return sum * (1.0/transpostions.__len__())


def compareDistribution(a, b, sigma):
    distributions  = getDistribution(a,b)
    sum = 0
    for key in distributions:
        d = distributions.get(key)
        sum += 1.0 - math.exp(-0.5 * (math.pow(d / sigma, 2)))
    size = len(distributions)
    if size == 0:
        return sum
    return sum * (1.0 / size)



def getTranspositions(firstString, secondString):
    length = 0
    if len(firstString) > len(secondString):
        length = len(firstString)
        a = firstString
        b = secondString
    else:
        length = len(secondString)
        a = secondString
        b = firstString

    right = []
    left = []

    for i in range(length):
        right.append(findCharInStringRight(a[i], b, i))
        left.append(findCharInStringLeft(a[i], b, i))

    res = []
    for i in range(length):
        if right[i] > left[i] and right[i] > -1:
            res.append(right[i])
        elif left[i] > right[i] and left[i] > -1:
            res.append(right[i])
        elif left[i]>right[i] and left[i] > -1:
            res.append(right[i])
        elif left[i] == right[i] and left[i] == -1:
            res.append(-1)
        else:
            res.append(0)

    # TODO: hier Optimierungspotential, da gleich Schleife und unnötiges inkrementieren
    count = 0
    result = []
    for i in res:
        if i != -1:
            count += 1
            result.append(i)

    return result


def findCharInStringRight(x, a, pos):
    if pos >= len(a):
        pos = len(a)-1
    distance = 0
    for i in range(pos, a.__len__()):
        if a[i] == x:
            return distance
        distance += 1
    return -1

def findCharInStringLeft(x, a, pos):
    if pos >= len(a):
        pos = len(a)-1
    distance = 0
    for i in range(pos, -1, -1):
        if a[i] == x:
            return distance
        distance += 1
    return -1


def getDistribution(a, b):
    aMap = stringToHashMap(a)
    bMap = stringToHashMap(b)

    transpositions = {}
    total = set()
    for c in aMap:
        total.add(c)
    for c in bMap:
        total.add(c)
    for c in total:
        x = 0
        y = 0
        if aMap.get(c) is not None:
            x = aMap.get(c)
        if bMap.get(c) is not None:
            y= bMap.get(c)
        transpositions.update( {c : abs(x-y)} )
    return transpositions


def stringToHashMap(s):
    _s = s.lower()
    result = {}
    for c in _s:
        val = result.get(c)
        if val is not None:
            result[c] = val + 1
        else:
            result[c] = 1
    return collections.OrderedDict(sorted(result.items()))




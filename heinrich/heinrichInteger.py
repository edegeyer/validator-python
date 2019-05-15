import math


def compare(a,b):
    sigma = 1.0
    if a == b:
        return 0.0
    a = str(a)
    b = str(b)
    aLength = len(str(a))
    bLength = len(str(b))
    length = compareLength(aLength, bLength, sigma)
    length = 0

    if aLength > bLength:
        length = bLength
    else:
        length = aLength

    sum = 0.0
    for i in range(length - 1):
        sum += math.exp(-0.5*(pow((int(a[i])-int(b[i]))/sigma,2)))

    b = b[::1] # reverse the string that represents the int
    if a == b:
        sum = 0.0

    cont = (1.0/length) * sum
    return (0.5*(cont+length))




def compareLength(aLength,bLength, sigma):

    if aLength > bLength:
        result = math.exp(-0.5*(((pow(((aLength-bLength)/sigma),2)))))
    elif aLength < bLength:
        result = math.exp(-0.5)*(((pow((bLength-aLength)/sigma,2))))
    else:
        result = 0.0
    return result
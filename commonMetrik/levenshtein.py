

def levenshteinDistance(s1, s2):
    if s1 == s2:
        return  0
    elif len(s1) == 0:
        return 1 # is the normalized value of len(s2)/len(s2)
    elif len(s2) == 0:
        return 1
    v0 = [None] * (len(s1)+1)
    v1 = [None] * (len(s1)+1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s1)):
        v1[0] = i +1
        for j in range(len(s2)):
            cost = 0 if s1[i] == s2[j] else 1
            v1[j + 1]  = min(v1[j] + 1, v0[j+1] +1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    leven = v1[len(s2)]/ len(s2)
    # normalize by dividing with the string length (is the same length at this point
    return v1[len(s2)] / len(s2)

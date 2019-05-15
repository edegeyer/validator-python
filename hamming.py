

def hammingDistance(a, b):
    if isinstance(a, str):
        shortest = min(len(a), len(b))
        longest = max(len(a), len(b))
        result = 0.0

        #first: compare both strings (only the legnth of the shortest)

        for i in range(shortest):
            if(a[i] != b[i]):
                result += 1

        # both strings differ by the length difference, needs to be taken in consideration
        result += longest - shortest
        return result
    else:
        return -1;

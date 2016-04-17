    
def permute(permute_this, start, end):
    if start == end:
        print("A permutation: " + str(permute_this))
    else:
        temp = permute_this[start]
        for i in range(start, end, 1):
            permute_this[start] = permute_this[i]
            permute_this[i] = temp
            permute(permute_this, start+1, end)
            permute_this[i] = permute_this[start]
        permute_this[start] = temp

if __name__ == "__main__":
    permute_me = ['t', 'i', 'c']
    start = 0
    end = len(permute_me)
    permute(permute_me, start, end)
    
    

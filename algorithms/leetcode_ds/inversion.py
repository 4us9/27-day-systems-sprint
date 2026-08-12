#Calculating the number of inversions

#Pseudocode given from Roughgarden textbook
def CountInv(arr):
    n = len(arr) 
    
    #Used to check for out of bounds cases
    
    if n<=1:
        return arr, 0
    
    mid = n//2
    
    
    left, inv_left = CountInv(arr[:mid])
    right, inv_right = CountInv(arr[mid:])

    merged, inv_split = CountSplitInv(left, right)

    return merged, inv_left + inv_right + inv_split
        
def CountSplitInv(left, right):
    # left and right are sorted
    i = j = 0
    merged = []
    inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # left[i] > right[j] and i < j in the original array
            # all remaining elements in left form inversions with right[j]
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    # Append any leftovers
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count

def total_inversions(arr):
    _, inv = CountInv(arr)
    return inv

with open("IntegerArray.txt") as f:
    data = [int(line.strip()) for line in f]

print(total_inversions(data))
            
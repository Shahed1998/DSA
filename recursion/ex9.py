# ------------------------------ Question -----------------------------
# Write a recursive function called flatten
# which accepts an array of arrays and returns a new array with all values flattened.
# ------------------------------ Solution -----------------------------

def flatten(array, list = []):

    if len(array) == 0: return list

    elif type(array) == type([]): array = str(array)
    
    elif array[0] != '[' and array[0] != ',' and array[0] != ' ' and array[0] != ']':
        
        list.append(int(array[0])) 

    
    return flatten(array[1:], list)

print(flatten([1, [2, [3, 4], [[5]]]]))
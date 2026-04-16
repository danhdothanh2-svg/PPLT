def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def find_min(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# Test array
scores = [6.5, 8.0, 4.5, 9.5, 7.0]

print("Max value:", find_max(scores))
print("Min value:", find_min(scores))
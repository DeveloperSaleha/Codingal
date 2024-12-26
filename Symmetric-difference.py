def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}

set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}

symmetric_diff_a = find_symmetric_difference(set1_a, set2_a)
symmetric_diff_b = find_symmetric_difference(set1_b, set2_b)

print(f"Symmetric Difference for Example A: {symmetric_diff_a}")
print(f"Symmetric Difference for Example B: {symmetric_diff_b}")

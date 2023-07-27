# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

sp = [1, 1, 2, 0, -1, 3, 4, 4]
diff_numbers = []
for i in sp:
    if i not in diff_numbers:
        diff_numbers.append(i)
print(f" Различных чисел: {len(diff_numbers)} ")

#print(len(set(sp)))
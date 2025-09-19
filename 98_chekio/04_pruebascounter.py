from collections import Counter

# Counting elements in a list
my_list = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
counts = Counter(my_list)
print(counts)

# Counting characters in a string
my_string = "hello world"
char_counts = Counter(my_string)
print(char_counts)

# Accessing counts
print(counts[2])  # Output: 4
print(counts[9])  # Output: 0 (for a non-existent key)

# Finding most common elements
print(counts.most_common(2))

# Updating the counter
counts.update([1, 5, 5, 6])
print(counts)
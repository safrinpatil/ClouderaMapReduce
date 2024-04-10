#!/usr/bin/env python

import sys

# Initialize a dictionary to store the count of each candidate
candidate_counts = {}

# Iterate through each line in the input
for line in sys.stdin:
    # Trim leading/trailing whitespace and split the line into words
    words = line.strip().split()
    # Iterate through each word in the line
    for word in words:
        # Increment the count of the candidate in the dictionary
        candidate_counts[word] = candidate_counts.get(word, 0) + 1

# Output the candidate counts
for candidate, count in candidate_counts.items():
    print(f"{candidate}\t{count}")

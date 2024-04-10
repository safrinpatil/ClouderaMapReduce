#!/usr/bin/env python

import sys

# Initialize a dictionary to store the total count of each candidate
candidate_counts = {}

# Iterate through each line in the input
for line in sys.stdin:
    # Split the line into candidate and count
    candidate, count = line.strip().split('\t')
    # Convert count to an integer
    count = int(count)
    # Increment the total count of the candidate in the dictionary
    candidate_counts[candidate] = candidate_counts.get(candidate, 0) + count

# Output the total counts for each candidate
for candidate, count in candidate_counts.items():
    print(f"{candidate}\t{count}")

# -*- coding: utf-8 -*-
"""random.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PP0jVdrJCV9dwJAFb5GJx_zT-Oc1WUXw
"""

import random

# Define the constants for the pattern lengths
PATTERN_LENGTH = 5
T_PATTERN_LENGTH = 6

def simulate_coin_flips(num_flips, num_tables):
    for _ in range(num_tables):
        table = []
        mirror_pattern_length = 0
        longest_mirror_pattern = 0
        t_pattern_length = 0
        longest_t_pattern = 0
        total_flips = 0 # The total number of flips until a pattern forms or breaks
        num_patterns = 0 # The number of patterns formed or broken
        total_t_flips = 0 # The total number of flips until a TTTTTT pattern forms or breaks
        num_t_patterns = 0 # The number of TTTTTT patterns formed or broken

        for _ in range(num_flips):
            flip = random.choice(["H", "T"])
            table.append(flip)

            # Check if the last flip matches the previous one
            if len(table) > 1 and table[-1] == table[-2]:
                # Increase the mirror pattern length
                mirror_pattern_length += 1
                # Increase the TTTTTT pattern length if the flip is T
                if flip == "T":
                    t_pattern_length += 1
                else:
                    # Reset the TTTTTT pattern length if the flip is H
                    t_pattern_length = 0
            else:
                # Reset the mirror pattern length
                mirror_pattern_length = 1
                # Reset the TTTTTT pattern length
                t_pattern_length = 0

            # Check if the mirror pattern length is equal to the pattern length
            if mirror_pattern_length == PATTERN_LENGTH:
                # Update the longest mirror pattern
                longest_mirror_pattern = PATTERN_LENGTH
                # Reset the mirror pattern length
                mirror_pattern_length = 0
                # Update the total flips and the number of patterns
                total_flips += PATTERN_LENGTH
                num_patterns += 1
            # Check if the mirror pattern is broken by the opposite flip
            elif mirror_pattern_length == PATTERN_LENGTH - 1 and len(table) >= 2 * PATTERN_LENGTH and table[-1] != table[-2 * PATTERN_LENGTH]:
                # Update the longest mirror pattern
                longest_mirror_pattern = max(longest_mirror_pattern, mirror_pattern_length)
                # Reset the mirror pattern length
                mirror_pattern_length = 1
                # Update the total flips and the number of patterns
                total_flips += 2 * PATTERN_LENGTH - 1
                num_patterns += 1

            # Check if the TTTTTT pattern length is equal to the T pattern length
            if t_pattern_length == T_PATTERN_LENGTH:
                # Update the longest TTTTTT pattern
                longest_t_pattern = T_PATTERN_LENGTH
                # Reset the TTTTTT pattern length
                t_pattern_length = 0
                # Update the total T flips and the number of T patterns
                total_t_flips += T_PATTERN_LENGTH
                num_t_patterns += 1
            # Check if the TTTTTT pattern is broken by the opposite flip
            elif t_pattern_length == T_PATTERN_LENGTH - 1 and len(table) >= 2 * T_PATTERN_LENGTH and table[-1] != table[-2 * T_PATTERN_LENGTH]:
                # Update the longest TTTTTT pattern
                longest_t_pattern = max(longest_t_pattern, t_pattern_length)
                # Reset the TTTTTT pattern length
                t_pattern_length = 0
                # Update the total T flips and the number of T patterns
                total_t_flips += 2 * T_PATTERN_LENGTH - 1
                num_t_patterns += 1

        print("".join(table))
        print(f"Longest Mirror Pattern: {longest_mirror_pattern}")
        # Calculate the average length of a coin flips until a mirror pattern forms or breaks
        if num_patterns > 0:
            average_flips = total_flips / num_patterns
            print(f"Average Length of a Coin Flips Until a Mirror Pattern Forms or Breaks: {average_flips}")
        else:
            print("No Mirror Pattern Found")
        print(f"Longest TTTTTT Pattern: {longest_t_pattern}")
        # Calculate the average length of a coin flips until a TTTTTT pattern forms or breaks
        if num_t_patterns > 0:
            average_t_flips = total_t_flips / num_t_patterns
            print(f"Average Length of a Coin Flips Until a TTTTTT Pattern Forms or Breaks: {average_t_flips}")
        else:
            print("No TTTTTT Pattern Found")
        print()

# Taking user input
num_flips = int(input("How many coin flips? "))
num_tables = int(input("How many tables? "))

# Running the simulation
simulate_coin_flips(num_flips, num_tables)

# Sort Tuples by Sum of Elements
# You are given a list of tuples, where each tuple contains exactly two integers.
# Write a function that sorts this list in ascending order based on the sum of the integers in each tuple and returns the sorted list.

"""Day 1 submission - Susheel"""

def sort_by_tuple_sum(Ist: list[tuple]) -> list[tuple]:
    """sorts a list of tuples, based on the sum of each tuple"""
    sorted_list=sorted(Ist, key=lambda a:a[0]+a[1])
    return sorted_list



t1=[(3, 1), (2, 2), (5, -1), (0, 0)]
t2=[(7, 3), (1, 2), (4, 5), (0, 1)]
t3=[(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]
print("Test Case 1:", sort_by_tuple_sum(t1))
print("Test Case 2:", sort_by_tuple_sum(t2))
print("Test Case 3:", sort_by_tuple_sum(t3))
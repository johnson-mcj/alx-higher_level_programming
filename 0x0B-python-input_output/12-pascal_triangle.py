#!/usr/bin/python3
"""
Defines the pascal_triangle function that returns the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n

    Args:
        n (int): Number of rows in the triangle

    Returns:
        list: List of lists representing Pascal's triangle

    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle

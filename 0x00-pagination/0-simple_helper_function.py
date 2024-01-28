#!/usr/bin/env python3
"""0-simple_helper_function.py module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the range of indexes to start from and end.
    Args:
        page: page number
        page_size: number of items per page
    Return: a tuple of start and end indexes.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

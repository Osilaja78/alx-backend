#!/usr/bin/env python3
"""1-simple_pagination.py module"""

import csv
import math
from typing import Tuple, List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct pages to index and returns the right
        amount of dataset.
        """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dict containing the following:
            page_size, page, data,
            next_page, prev_page,
            total_pages.
        """

        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        len_dataset = len(self.__dataset)
        total_pages = math.ceil(len_dataset / page_size)

        next_page = page + 1 if end < len_dataset else None
        prev_page = page - 1 if start > 0 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

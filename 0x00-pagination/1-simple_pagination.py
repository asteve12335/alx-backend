#!/usr/bin/env python3
"""
A module containing a function named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.

    Args:
        page: The page number to return results for.
        page_size: The number of results to return per page.

    Returns:
        A tuple of size two containing a start index and an end index.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        A method that takes two integer arguments page with default value 1
        and page_size with default value 10.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]
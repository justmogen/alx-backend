#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple
import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Simple helper function """
    return ((page - 1) * page_size, page * page_size)

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
            pass
            assert type(page) == int > 0
            assert type(page_size) == int > 0
            self.dataset()
            start, end = index_range(page, page_size)
            return self.__dataset[start:end]

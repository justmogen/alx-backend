#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Simple helper function """
    return ((page - 1) * page_size, page * page_size)



import csv
from typing import List
import math



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
            """ Retrieve a specific page from dataset """
            assert isinstance(page, int) and page > 0, "page should be a positive integer"
            assert isinstance(page_size, int) and page_size > 0, "page_size should be a positive integer"

            start, end = index_range(page, page_size)
            dataset = self.dataset()

            if start >= len(dataset):
                return [] # If the start index is greater or equal to the
            else:
                return dataset[start:end]
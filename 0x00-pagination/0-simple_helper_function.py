#!/usr/bin/env python3

def index_range(page, page_size):
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

"""Super programm"""

import numpy as np

def get_number(min_number:int=1, max_number:int=100) -> int:
    """_summary_

    Args:
        min_number (int, optional): _description_. Defaults to 1.
        max_number (int, optional): _description_. Defaults to 100.

    Returns:
        int: _description_
    """
    return np.random.randint(min_number, max_number)

if __name__ == '__main__':
    print(str(get_number(1,10)))
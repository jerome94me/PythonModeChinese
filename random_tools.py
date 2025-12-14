import random
from typing import List, Tuple, Any, Union

def 隨機抽取整數(最小值: int, 最大值: int) -> int:
    """
    min 是最小值 max 是最大值。將回傳隨機數字(整數)。

    Args:
        最小值 (int): 隨機範圍的下限 (包含此值)。
        最大值 (int): 隨機範圍的上限 (包含此值)。

    Returns:
        int: 落在 [最小值, 最大值] 區間內的隨機整數。
    """
    # random.randint(a, b) 包含 a 和 b
    return random.randint(a=最小值, b=最大值)

def 隨機抽取小數(最小值: Union[int, float], 最大值: Union[int, float]) -> float:
    """
    min 是最小值 max 是最大值。將回傳隨機數字(浮點數)。

    Args:
        最小值 (Union[int, float]): 隨機範圍的下限。
        最大值 (Union[int, float]): 隨機範圍的上限。

    Returns:
        float: 落在 [最小值, 最大值] 區間內的隨機浮點數。
    """
    # random.uniform(a, b) 包含 a，不包含 b (但通常視為包含)
    return random.uniform(最小值, 最大值) 

def 隨機選多個列表項目(datalist: Union[List, Tuple], 抽幾個: int) -> List:
    """
    datalist 是要抽取的列表或元組，抽幾個是要抽取的數量。
    
    Args:
        datalist (Union[List, Tuple]): 欲抽取的來源列表或元組。
        抽幾個 (int): 欲不重複抽取的項目數量。

    Returns:
        List: 包含隨機抽取項目的新列表。
    """
    return random.sample(datalist, 抽幾個)

def 隨機選單個列表項目(datalist: Union[List, Tuple]) -> Any:
    """
    datalist 是要抽取的列表或元組。將回傳單一個抽取的項目。
    
    Args:
        datalist (Union[List, Tuple]): 欲抽取的來源列表或元組。

    Returns:
        Any: 隨機選中的單一個項目。
    """
    return random.choice(datalist)

def 隨機洗牌(datalist: Union[List, Tuple]) -> List:
    """
    datalist 是要洗牌的列表或元組。將回傳一個列表，裡面是洗牌後的項目。
    
    Args:
        datalist (Union[List, Tuple]): 欲打亂順序的來源列表或元組。

    Returns:
        List: 包含打亂順序後項目的新列表。
    """
    # random.shuffle() 只能作用於 list，因此先複製一份
    shuffled_list = list(datalist) 
    random.shuffle(shuffled_list)
    return shuffled_list
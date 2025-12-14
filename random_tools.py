import random
from typing import List, Tuple, Any, Union
def 隨機抽取整數(min:int, max:int) -> int:
    """min是最小值 max是最大值。將回傳隨機數字(整數)"""
    return random.randint(a=min, b=max)

def 隨機抽取小數(min:Union[int, float], max:Union[int, float]) -> float:
    """min是最小值 max是最大值。將回傳隨機數字(浮點樹)"""
    return random.uniform(min, max) 

def 隨機選多個列表項目(datalist:Union[List, Tuple], 抽幾個:int) -> List:
    """datalist是要抽取的列表或元組 抽幾個是要抽取的數量"""
    return random.sample(datalist, 抽幾個)

def 隨機選單個列表項目(datalist:Union[List, Tuple]) -> Any:
    """datalist是要抽取的列表或元組。將回傳單一個抽取的項目"""
    return random.choice(datalist)

def 隨機洗牌(datalist:Union[List, Tuple]) -> List:
    """datalist是要洗牌的列表或元組。將回傳一個列表，裡面是洗牌後的項目"""
    shuffled_list = list(datalist)
    random.shuffle(shuffled_list)
    return shuffled_list
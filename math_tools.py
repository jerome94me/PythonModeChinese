# 數字操作_工具箱_f.py (f 代表 function)
import math
import numpy as np
from typing import List, Union

# =========================
# 1️⃣ 數字操作
# =========================
def 加(x: float, y: float) -> float:
    return x + y

def 減(x: float, y: float) -> float:
    return x - y

def 乘(x: float, y: float) -> float:
    return x * y

def 除(x: float, y: float) -> float:
    return x / y

def 判斷偶數(n: int) -> bool:
    return n % 2 == 0

def 判斷奇數(n: int) -> bool:
    return n % 2 != 0

def π() -> float:
    return math.pi

def 自然常數() -> float:
    return math.e

def 無條件捨去(n: float) -> int:
    return math.floor(n)

def 無條件進位(n: float) -> int:
    return math.ceil(n)

def 最大公因數(x: int, y: int) -> int:
    return math.gcd(x, y)

def 最小公倍數(x: int, y: int) -> int:
    return math.lcm(x, y)

def 次方(x: float, y: float) -> float:
    return x ** y

def 開根號(x: float) -> float:
    return math.sqrt(x)

def 產生連續數字(開始:int, 結束:int) -> np.ndarray:
    """產生一個包含開始和結束的連續數字列表 (使用 numpy)"""
    return np.arange(開始, 結束 + 1)
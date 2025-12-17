# 數字操作_工具箱_f.py (f 代表 function)
import math
import numpy as np
from typing import List, Union
import mpmath
from mpmath import mp
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

def 獲取圓周率(獲取到幾位數:int = 5) -> float | int | None:
    """
    獲取到幾位數預設值為5
    但我會限制不能獲取超過500
    """
    if 獲取到幾位數 >= 500:
        pass
    elif 獲取到幾位數 <= 1:
        pass
    else:
        mp.dps = 獲取到幾位數
        return mp.pi

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
def 生成斐波那契(數量: int) -> list:
    """
    生成長度為 n 的斐波那契數列清單。
    """
    if 數量 <= 0:
        return []
    elif 數量 == 1:
        return [0]
    
    # 初始化前兩個數字
    數列 = [0, 1]
    
    # 從第三個數字開始計算 (索引為 2)
    while len(數列) < 數量:
        下一個數字 = 數列[-1] + 數列[-2]
        數列.append(下一個數字)
        
    return 數列
from typing import List, Union

def 計算多個數字(方法: str, 數字: Union[List, tuple]):
    """
    方法要是 + - * / // 裡面的
    """
    列表長度 = len(數字)
    方法列表 = ["+", "-", "*", "/", "//"]
    
    if 列表長度 == 0:
        return 0
    
    if 方法 in 方法列表:
        # 設定第一個數字為初始結果
        結果 = 數字[0]
        
        # 從第二個數字開始進行運算
        for i in range(1, 列表長度):
            if 方法 == "+":
                結果 += 數字[i]
            elif 方法 == "-":
                結果 -= 數字[i]
            elif 方法 == "*":
                結果 *= 數字[i]
            elif 方法 == "/":
                if 數字[i] == 0:
                    return "錯誤：除數不能為零"
                結果 /= 數字[i]
            elif 方法 == "//":
                if 數字[i] == 0:
                    return "錯誤：除數不能為零"
                結果 //= 數字[i]
        
        return 結果
    else:
        return "錯誤：不支援的運算方法"

# 其他_工具箱_f.py
import random
import time
import turtle
from rich.progress import track
from typing import List, Tuple, Any, Union
# 請注意：此庫在非 Windows 系統上可能報錯，語音功能為選擇性
try:
    import win32com.client 
except ImportError:
    win32com = None

# =========================
# 8️⃣ 隨機 & 其他工具
# =========================

# --- 隨機工具 ---


# --- 其他工具 ---
def 唸出文字(text:str) -> None:
    """可以唸出文字 (Windows SAPI)"""
    if win32com:
        try:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(text)
        except Exception as e:
            print(f"唸出文字失敗 (Windows SAPI): {e}")
    else:
        print("未偵測到 win32com 庫，無法執行語音功能。")
    return

def show_progress(items: list, description: str = "處理中"):
    """使用 rich 庫顯示進度條"""
    for i in track(items, description=description):
        time.sleep(0.1)  # 模擬處理時間
from typing import Any

def 檢測變數類型(var: Any) -> str:
    """
    檢測變數的資料類型並回傳格式化後的字串。

    此函數接收任意變數，並回傳其類型字串，但移除了 "<class '" 和 "'>" 部分，
    使輸出更為簡潔。例如，整數會回傳 'int' 而不是 '<class 'int'>'。

    Args:
        var (Any): 要檢測類型的變數。

    Returns:
        str: 變數的類型名稱字串（例如：'str', 'int', 'list'）。
    """
    # 獲取類型字串，例如："<class 'str'>"
    type_var = str(type(var))
    
    # 由於 type(var) 格式固定為 "<class 'type_name'>"，
    # 移除 'class' 只是移除其中一部分，最佳方法是使用切片或更精確的替換。
    # 更簡潔且常見的做法是使用 __name__ 屬性，或直接用切片移除開頭和結尾的字元。
    
    # 方法一：使用 __name__ (最推薦，但會回傳 'type' 而非 'str')
    # return type(var).__name__ 
    
    # 方法二：使用 replace 移除 'class'，然後移除 '< ' 和 '>' 
    #         （如果只想延續您原來的做法，但更完整）
    
    # 1. 移除 "<class '"
    result = type_var.replace("<class '", "")
    # 2. 移除尾部的 "'>"
    result = result.replace("'>", "")
    
    return result

# --- 測試 ---

# --- 烏龜繪圖 (需要特別處理狀態) ---
# 由於 turtle 需要維護一個內部狀態 (t.Turtle() 物件)，
# 將其轉為純函式會非常複雜且不直覺，因此我會將其函式化，
# 但請注意，這些函式通常需要在同一繪圖環境下調用。

_TURTLE_INSTANCE = None

def _取得烏龜實例(顏色="green", 速度=5, 筆粗=2):
    global _TURTLE_INSTANCE
    if _TURTLE_INSTANCE is None:
        _TURTLE_INSTANCE = turtle.Turtle()
        _TURTLE_INSTANCE.shape("turtle")
        _TURTLE_INSTANCE.color(顏色)
        _TURTLE_INSTANCE.speed(速度)
        _TURTLE_INSTANCE.pensize(筆粗)
    return _TURTLE_INSTANCE

def 烏龜_前進(距離, 顏色="green", 速度=5, 筆粗=2):
    _取得烏龜實例(顏色, 速度, 筆粗).forward(距離)

def 烏龜_左轉(角度, 顏色="green", 速度=5, 筆粗=2):
    _取得烏龜實例(顏色, 速度, 筆粗).left(角度)

def 烏龜_完成():
    """保持畫布開啟直到手動關閉"""
    turtle.done()

# 為了簡潔，我只保留了幾個烏龜範例函式。如果需要，您可以依此模式將所有烏龜功能轉換。
if __name__ == "__main__":
    print(f"{檢測變數類型('Hello')}")
    print(f"{檢測變數類型(123)}")
    print(f"{檢測變數類型([1, 2])}")
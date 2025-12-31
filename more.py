# 其他_工具箱_f.py
import random
import time
import turtle
import playsound
from rich.progress import track
from typing import List, Tuple, Any, Union
# 請注意：此庫在非 Windows 系統上可能報錯，語音功能為選擇性
try:
    import win32com.client 
except ImportError:
    win32com = None



# --- 其他工具 ---
def 唸出文字(文字:str) -> None:
    """可以唸出文字 (Windows SAPI)"""
    if win32com:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(文字)

    return
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

def 播放mp3(path:str) -> None:
    """
    透過playsound來撥放音樂
    path是mp3路徑
    """
    import os
    if not os.path.exists(path):
        pass
    else:
        playsound.playsound(path)

from Console import 視覺化工具
from Console import 控制台
import sounddevice as sd
from scipy.io.wavfile import write
console = 控制台()
show = 視覺化工具(console)
fs = 44100
def 錄音(self, 秒數: int, 檔名: str = "record.wav"):
    import sounddevice as sd
    from scipy.io.wavfile import write
        
    fs = 44100
    # 配合你的「視覺化工具」顯示載入動畫
    with console.視覺.載入中(f"[bold red]🔴 錄音中... ({秒數}秒)"):
        錄音數據 = sd.rec(int(秒數 * fs), samplerate=fs, channels=2)
        sd.wait()   
    write(檔名, fs, 錄音數據)
    console.日誌(f"✅ 錄音完成：{檔名}")
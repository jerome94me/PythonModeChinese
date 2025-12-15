# 文字操作_工具箱_f.py

from deep_translator import GoogleTranslator
from typing import List

# 語言對照表（作為全域變數或函式內建）
LANGUAGES_DICT = {
    '英語': 'en', '中文（簡體）': 'zh-CN', '中文（繁體）': 'zh-TW', 
    '西班牙語': 'es', '法語': 'fr', '德語': 'de', '日語': 'ja', 
    '韓語': 'ko', '俄語': 'ru', '葡萄牙語': 'pt', '義大利語': 'it', 
    '阿拉伯語': 'ar', '印地語': 'hi', '泰語': 'th', '越南語': 'vi'
}
    
# =========================
# 2️⃣ 文字操作（含翻譯）
# =========================
def 重複(要重複的文字:str, 次數:int):
    return 要重複的文字*次數
def 全大寫(text: str) -> str:
    return text.upper()

def 全小寫(text: str) -> str:
    return text.lower()

def 首字母大寫(text: str) -> str:
    return text.capitalize()

def 字數(text: str) -> int:
    return len(text)

def 每個單字前面都大寫(text:str) :
    return text.title()

def 單詞數(text: str) -> int:
    return len(text.split())

def 替換文字(變數:str, x:str, y:str) -> str:
    """
    將字串中的 x 替換為 y
    """
    return 變數.replace(x, y)
def 搜尋(text: str, 關鍵字: str) -> int:
    return text.find(關鍵字)

def 大小寫對調(text:str):
    """
    顧名思義
    """
    return text.swapcase()
def 計算字串在變數裡出現的次數(var:str, text:str, start:int, end: int) -> int:
    """
    計算某段文字在字串中出現的次數 ( start、end 為範圍，可不填 )
    """
    if not start and not end:
        return var.count(text)
    else:
        return var.count(text,start,end)
        
def 替換(text: str, 舊字: str, 新字: str) -> str:
    return text.replace(舊字, 新字)

def 切割(text: str, 分隔符: str = " ") -> List[str]:
    return text.split(分隔符)

def 合併(列表: List[str], 分隔符: str = " ") -> str:
    return 分隔符.join(列表)

def 字串中是否存在某段文字(var, text) -> bool:
    """
    判斷var是否存在text，如果有回傳True，沒有就回傳False
    """
    if var in text:
        return True
    else:
        return False
def 是否都是英文和數字(var:str) -> bool:
    """
    判斷字串中是否都是英文字母或數字 ( 不能包含空白或符號 )
    回傳 True 或 False
    """
    if var.isalnum() == True:
        return True
    else:
        return False

def 是否都是英文(var:str) -> bool:
    """
    判斷字串中是否都是英文字母或數字 
    ( 不能包含空白或符號 )
    回傳 True 或 False
    """
    if var.isalpha() == True:
        return True
    else:
        return False
def 是否都是小寫(var: str) -> bool:
    """
    判斷字串中是否所有字元都是小寫英文字母。
    ( 忽略非字母字元，例如數字或符號 )
    回傳 True 或 False
    """
    if var.islower() == True:
        return True
    else:
        return False

def 是否都是大寫(var: str) -> bool:
    """
    判斷字串中是否所有字元都是大寫英文字母。
    ( 忽略非字母字元，例如數字或符號 )
    回傳 True 或 False
    """
    if var.isupper() == True:
        return True
    else:
        return False

def 是否都是數字(var: str) -> bool:
    """
    判斷字串中是否所有字元都是數字 (0-9)。
    ( 不能包含小數點、負號、或空白 )
    回傳 True 或 False
    """
    if var.isdigit() == True:
        return True
    else:
        return False

def 是否每個單字字首大寫(var:str) -> bool:
    return var.istitle()
def 翻譯(text: str, 起始語言: str = "auto", 目標語言: str = "zh-TW") -> str:
    """單一文字翻譯"""
    try:
        return GoogleTranslator(source=起始語言, target=目標語言).translate(text)
    except Exception as e:
        return f"翻譯失敗：{e}"

def 批量翻譯(文字列表: List[str], 起始語言: str = "auto", 目標語言: str = "zh-TW") -> List[str]:
    """批量文字翻譯"""
    result = []
    for t in 文字列表:
        try:
            result.append(GoogleTranslator(source=起始語言, target=目標語言).translate(t))
        except Exception as e:
            result.append(f"翻譯失敗：{e}")
    return result
# U can test in here
if __name__ == "__main__":
    pass
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
def 全大寫(text: str) -> str:
    return text.upper()

def 全小寫(text: str) -> str:
    return text.lower()

def 首字母大寫(text: str) -> str:
    return text.capitalize()

def 字數(text: str) -> int:
    return len(text)

def 單詞數(text: str) -> int:
    return len(text.split())

def 搜尋(text: str, 關鍵字: str) -> int:
    return text.find(關鍵字)

def 替換(text: str, 舊字: str, 新字: str) -> str:
    return text.replace(舊字, 新字)

def 切割(text: str, 分隔符: str = " ") -> List[str]:
    return text.split(分隔符)

def 合併(列表: List[str], 分隔符: str = " ") -> str:
    return 分隔符.join(列表)

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
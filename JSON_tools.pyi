import json
from typing import TextIO, Dict, List, Union, Optional, Any

"""
使用此模組需先使用 open(JSON檔路徑)
例如:a = open(json.json, mode="r")
然後函式內的檔案就使用a
就是這樣
"""
def 讀取並轉換(檔案: TextIO) -> Dict:
    """
    讀取本機 JSON 檔案，並轉換為 Python 的字典 dict 型別
    對照表:
        Json            python
        object 物件 -> dict 字典
        arrays 陣列 -> list 清單
        string 字串 -> str 字串
        number 數字 -> int 或 float 數字
        true        -> True 布林值
        false       -> False 布林值
        null        -> None 空值
    """
    return json.load(檔案)

def 轉換並寫入(檔案: TextIO, 資料: Union[Dict, List], 縮排: Optional[int]=None) -> None:
    """
    將 Python 的字典 dict 或清單 list 型別轉換為 JSON 格式，並寫入本機檔案
    Args:
        檔案 (TextIO): 需以 'w' 或 'a' 模式開啟的檔案物件。
        資料 (Union[Dict, List]): 要寫入 JSON 檔案的 Python 資料結構 (字典或清單)。
        縮排 (Optional[int]): 寫入 JSON 檔案時使用的縮排空格數。如果為 None，則不縮排 (輸出會在一行)。
    """
    # 執行 json.dump 將 Python 物件序列化並寫入檔案
    json.dump(資料, 檔案, indent=縮排, ensure_ascii=False)


def 字串轉物件(json_字串: str) -> Union[Dict, List]:
    """
    將 JSON 格式的字串轉換為 Python 的字典或清單物件
    Args:
        json_字串 (str): JSON 格式的字串。
    Returns:
        Union[Dict, List]: 轉換後的 Python 物件 (通常是字典或清單)。
    """
    # 執行 json.loads (load string)
    return json.loads(json_字串)


def 物件轉字串(資料: Union[Dict, List], 縮排: Optional[int]=None) -> str:
    """
    將 Python 的字典 dict 或清單 list 型別轉換為 JSON 格式的字串
    Args:
        資料 (Union[Dict, List]): 要轉換的 Python 資料結構 (字典或清單)。
        縮排 (Optional[int]): 輸出 JSON 字串時使用的縮排空格數。如果為 None，則輸出最緊湊的字串。
    Returns:
        str: JSON 格式的字串。
    """
    # 執行 json.dumps (dump string)
    return json.dumps(資料, indent=縮排, ensure_ascii=False)
def 寫入(資料: TextIO, json_字串: str) -> None:
    """
    將 JSON 格式的字串寫入本機檔案
    Args:
        資料 (TextIO): 需以 'w' 或 'a' 模式開啟的檔案物件。
        json_字串 (str): 要寫入檔案的 JSON 格式字串。
    """
    # 執行寫入操作
    資料.write(json_字串)
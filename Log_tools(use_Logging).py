import logging
import sys
from typing import Optional, Union, TextIO

# --- 日誌等級定義 (方便參考) ---
# DEBUG: 10
# INFO: 20
# WARNING: 30
# ERROR: 40
# CRITICAL: 50

# --- 主要設置函式 ---

def 初始化日誌系統(
    日誌名稱: str = "應用程式日誌", 
    日誌等級: int = logging.INFO, 
    檔案路徑: Optional[str] = None, 
    檔案模式: str = 'a',
    控制台輸出: bool = True
) -> logging.Logger:
    """
    配置並取得一個日誌記錄器 (Logger)。

    Args:
        日誌名稱 (str): 日誌記錄器的名稱。
        日誌等級 (int): 要記錄的最低等級 (例如 logging.DEBUG, logging.INFO)。
        檔案路徑 (Optional[str]): 如果提供，日誌將輸出到此檔案。
        檔案模式 (str): 寫入檔案的模式 ('a' 為追加，'w' 為覆蓋)。
        控制台輸出 (bool): 是否同時輸出到標準輸出 (控制台)。

    Returns:
        logging.Logger: 配置好的日誌記錄器物件。
    """
    # 創建日誌記錄器
    記錄器 = logging.getLogger(日誌名稱)
    記錄器.setLevel(日誌等級)

    # 避免重複添加 Handler
    if not 記錄器.handlers:
        # 定義格式化器 (Formatter)
        # 格式說明: 時間 - 等級 - 記錄器名稱 - 訊息
        格式化器 = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 1. 添加控制台輸出 (Console Handler)
        if 控制台輸出:
            控制台處理器 = logging.StreamHandler(sys.stdout)
            控制台處理器.setFormatter(格式化器)
            記錄器.addHandler(控制台處理器)

        # 2. 添加檔案輸出 (File Handler)
        if 檔案路徑:
            檔案處理器 = logging.FileHandler(檔案路徑, mode=檔案模式, encoding='utf-8')
            檔案處理器.setFormatter(格式化器)
            記錄器.addHandler(檔案處理器)

    return 記錄器

# --- 簡化日誌記錄函式 ---

def 取得記錄器(名稱: str = "應用程式日誌") -> logging.Logger:
    """
    依名稱取得已存在的日誌記錄器物件。
    """
    return logging.getLogger(名稱)

def 寫入除錯(記錄器: logging.Logger, 訊息: str) -> None:
    """
    記錄除錯 (DEBUG) 等級的訊息 (最低等級，用於開發除錯)。
    """
    記錄器.debug(訊息)

def 寫入資訊(記錄器: logging.Logger, 訊息: str) -> None:
    """
    記錄資訊 (INFO) 等級的訊息 (一般流程訊息)。
    """
    記錄器.info(訊息)

def 寫入警告(記錄器: logging.Logger, 訊息: str) -> None:
    """
    記錄警告 (WARNING) 等級的訊息 (非致命問題，但需要注意)。
    """
    記錄器.warning(訊息)

def 寫入錯誤(記錄器: logging.Logger, 訊息: str) -> None:
    """
    記錄錯誤 (ERROR) 等級的訊息 (嚴重的問題，程式功能受損)。
    """
    記錄器.error(訊息)

def 寫入致命錯誤(記錄器: logging.Logger, 訊息: str) -> None:
    """
    記錄致命錯誤 (CRITICAL) 等級的訊息 (最嚴重的錯誤，程式可能無法繼續執行)。
    """
    記錄器.critical(訊息)

def 記錄例外(記錄器: logging.Logger, 訊息: str = "發生例外/錯誤") -> None:
    """
    記錄例外資訊，並包含完整的堆疊追蹤 (Stack Trace)。
    請在 except 區塊中呼叫此函式。
    """
    記錄器.exception(訊息)

# --- 範例用法 (假設檔案名為 logging_zh.py) ---
"""
if __name__ == '__main__':
    # 1. 初始化日誌系統 (將 INFO 等級以上的日誌輸出到控制台和 app.log 檔案)
    主記錄器 = 初始化日誌系統(
        日誌名稱="主程序", 
        日誌等級=logging.DEBUG, # 設定最低記錄等級為 DEBUG
        檔案路徑="app.log",
        控制台輸出=True
    )

    # 2. 使用不同的等級記錄訊息
    寫入除錯(主記錄器, "這是一條只有在 DEBUG 等級才會輸出的訊息。")
    寫入資訊(主記錄器, "程序開始啟動。")
    
    # 3. 取得另一個記錄器 (會沿用主記錄器的設置)
    子記錄器 = 取得記錄器(名稱="資料庫連接")
    寫入警告(子記錄器, "資料庫連接超時，將嘗試重連。")
    
    # 4. 記錄例外
    try:
        結果 = 1 / 0
    except ZeroDivisionError:
        記錄例外(主記錄器, "執行除法運算時發生例外")
        
    寫入致命錯誤(主記錄器, "應用程式即將關閉。")
"""
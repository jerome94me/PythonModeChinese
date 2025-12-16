import threading
from typing import Callable, Any, Tuple, Dict, Optional, List, Set

# --- 核心類別：執行緒 (Thread) ---

class 執行緒:
    """
    執行緒類別：用於創建和管理一個獨立的執行緒。
    它包裝了 threading.Thread 的主要功能。
    """
    def __init__(self, 目標函數: Callable[..., Any], 參數: Tuple[Any, ...] = (), 
                關鍵字參數: Optional[Dict[str, Any]] = None, 名稱: Optional[str] = None):
        """
        初始化一個執行緒物件。

        Args:
            目標函數 (Callable): 執行緒啟動時要執行的函式或方法。
            參數 (Tuple): 傳遞給目標函數的位置參數 (例如: (arg1, arg2))。
            關鍵字參數 (Optional[Dict]): 傳遞給目標函數的關鍵字參數 (例如: {'key': value})。
            名稱 (Optional[str]): 給執行緒一個名稱，方便除錯。
        """
        if 關鍵字參數 is None:
            關鍵字參數 = {}
            
        self._thread = threading.Thread(
            target=目標函數, 
            args=參數, 
            kwargs=關鍵字參數, 
            name=名稱
        )

    def 啟動(self) -> None:
        """
        開始執行緒的活動。它會呼叫目標函數。
        """
        self._thread.start()

    def 等待完成(self, 超時秒數: Optional[float] = None) -> None:
        """
        阻塞當前執行緒的執行，直到此執行緒終止為止。

        Args:
            超時秒數 (Optional[float]): 如果給定，將最多等待這麼多秒。
        """
        self._thread.join(timeout=超時秒數)

    def 取得名稱(self) -> str:
        """
        回傳此執行緒的名稱。
        """
        return self._thread.name

    def 是否存活(self) -> bool:
        """
        檢查執行緒是否仍在活動（已啟動且尚未終止）。
        """
        return self._thread.is_alive()

# --- 常用工具函式 ---

def 取得當前執行緒() -> threading.Thread:
    """
    回傳當前正在執行此函式的原始 threading.Thread 物件。
    """
    return threading.current_thread()

def 執行緒休眠(秒數: float) -> None:
    """
    使呼叫此函式的執行緒暫停執行指定秒數。
    Args:
        秒數 (float): 執行緒暫停的秒數。
    """
    import time
    time.sleep(秒數)

def 取得所有活動執行緒() -> List[threading.Thread]:
    """
    回傳當前所有正在活動（已經啟動且尚未結束）的原始 threading.Thread 物件列表。
    """
    return threading.enumerate()
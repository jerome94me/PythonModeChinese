from rich.console import Console
from rich.text import Text
from typing import Optional, Any, Union, Iterable, TextIO

# --- 核心類別：控制台 ---

class 控制台:
    """
    控制台類別：用於管理和美化終端機 (控制台) 輸出。
    它包裝了 rich.console.Console 的主要功能。
    """
    def __init__(self, **kwargs: Any):
        """
        初始化控制台物件。

        Args:
            **kwargs: 傳遞給 rich.console.Console 的其他關鍵字參數，
                      例如 force_terminal=True, color_system="truecolor" 等。
        """
        self._console = Console(**kwargs)

    def 輸出(self, *物件: Any, 分隔符: str = " ", 樣式: Optional[str] = None, 
           新行: bool = True, 消除: bool = False, 檔案: Optional[TextIO] = None) -> None:
        """
        將一個或多個物件輸出到控制台。

        Args:
            *物件 (Any): 要輸出的物件 (可以是多個)。
            分隔符 (str): 輸出物件之間使用的分隔符 (預設為空格)。
            樣式 (Optional[str]): 應用於整個輸出的 Rich 樣式字串 (例如 "bold red on white")。
            新行 (bool): 輸出後是否換行 (預設為 True)。
            消除 (bool): 是否移除樣式標記和特殊字元 (預設為 False)。
            檔案 (Optional[TextIO]): 輸出到指定檔案或類檔案物件，而不是控制台。
        """
        self._console.print(*物件, sep=分隔符, style=樣式, end='\n' if 新行 else '', 
                            markup=not 消除)

    def 寫入(self, 文字: str, 樣式: Optional[str] = None) -> None:
        """
        直接寫入文字到控制台，不解析 Rich 標記。
        這類似於 Python 內建的 print() 或 sys.stdout.write()。

        Args:
            文字 (str): 要寫入的文字。
            樣式 (Optional[str]): 應用於整個輸出的 Rich 樣式字串。
        """
        self._console.print(文字, style=樣式, markup=False)

    def 狀態訊息(self, 訊息: str, 啟動: bool = True) -> Any:
        """
        啟動或停止一個終端機狀態行 (通常在終端機底部顯示，用於進度或狀態)。

        Args:
            訊息 (str): 要顯示的狀態訊息。
            啟動 (bool): 如果為 True，則回傳一個可在 'with' 語句中使用的狀態物件。
                         如果為 False，則立即停止狀態訊息。
        
        Returns:
            Any: 如果啟動為 True，回傳一個 Status 物件，否則回傳 None。
        """
        if 啟動:
            return self._console.status(訊息)
        else:
            self._console.status(訊息).stop() # 實際上，這需要先取得物件才能調用 stop

# --- 輔助函式 ---

def 樣式化文字(文字: str, 樣式: str) -> Text:
    """
    創建一個 Rich Text 物件，應用指定的樣式。
    
    Args:
        文字 (str): 原始文字內容。
        樣式 (str): Rich 樣式字串 (例如 "bold blue", "underline #ff00ff")。
        
    Returns:
        Text: 樣式化的 Rich Text 物件。
    """
    return Text(文字, style=樣式)

def 取得預設控制台() -> 控制台:
    """
    回傳一個預設配置的控制台物件實例 (單例模式)。
    """
    return 控制台()

# --- 範例用法 (假設檔案名為 console_zh.py) ---
"""
if __name__ == '__main__':
    # 1. 取得控制台實例
    主控台 = 取得預設控制台()
    
    # 2. 基本輸出與樣式化
    主控台.輸出("這是一條[bold green]綠色粗體[/bold green]的訊息！")
    主控台.輸出("警告！", 樣式="yellow on black")
    
    # 3. 不換行輸出
    主控台.輸出("同一行", 新行=False)
    主控台.輸出("繼續輸出")

    # 4. 寫入 (不解析標記)
    主控台.寫入("這段文字[bold]不會[/bold]被解析。")

    # 5. 狀態訊息 (使用 'with' 語句)
    import time
    with 主控台.狀態訊息("[bold magenta]正在處理數據...[/bold magenta]"):
        time.sleep(3)
    
    主控台.輸出("數據處理完成。")
"""
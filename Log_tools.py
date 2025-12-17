import logging
from typing import *

def 基本設置(log檔案名: str, 格式: str, 模式: str = "a", 等級: int = logging.INFO, 字符編碼:str = "UTF-8"):
    """
    進行 log 操作之前所需的動作
    """
    logging.basicConfig(
        filename=log檔案名,
        filemode=模式,
        format=格式,
        level=等級,          # 設定最低輸出的層級
        encoding=字符編碼     # 強制使用 utf-8 避免 Windows 上出現亂碼
    )
class Write:
    """
    如需開始寫log
    請透過此class
    """
    def 一般訊息(訊息:str) -> None:
        logging.info(msg=訊息)
        return None
    def 警告訊息(訊息:str) -> None:
        logging.warning(msg=訊息)
        return None
    def 錯誤訊息(訊息:str) -> None:
        logging.error(msg=訊息)
        return None
    def 除錯訊息(訊息:str) -> None:
        logging.debug(msg=訊息)
        return None
    def 致命訊息(訊息:str) -> None:
        logging.critical(msg=訊息)
        return None
    

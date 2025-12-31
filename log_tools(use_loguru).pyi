import os
from loguru import logger

class LogManager:
    """
    自定義日誌管理類別，封裝 Loguru 的常用功能。
    """
    def __init__(self, log_dir="logs", log_name="app.log"):
        # 建立日誌目錄
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        self.log_path = os.path.join(log_dir, log_name)
        self.配置loguru的配置()

    def 配置loguru的配置(self):
        """
        配置 Loguru 的寫入規則
        """
        # 先移除預設的控制台輸出（如果需要自定義的話）
        # logger.remove() 
        
        # 添加檔案寫入規則
        logger.add(
            self.log_path,
            rotation="500 MB",     # 滿 500MB 自動換檔
            retention="10 days",   # 只保留最近 10 天
            compression="zip",     # 舊檔案自動壓縮成 zip
            level="INFO",          # 設定寫入檔案的最低等級為 INFO
            encoding="utf-8",      # 確保中文不亂碼
            enqueue=True           # 非同步寫入，效能更好
        )

    def info(self, message):
        """記錄一般資訊"""
        logger.info(message)

    def warning(self, message):
        """記錄警告資訊"""
        logger.warning(message)

    def error(self, message):
        """記錄錯誤資訊"""
        logger.error(message)

    def debug(self, message):
        """記錄除錯資訊"""
        logger.debug(message)


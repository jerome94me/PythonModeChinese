import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Email通知器:
    def __init__(self, smtp伺服器: str, 帳號: str, 密碼: str, 埠號: int = 587):
        """
        初始化 Email 設定 (預設使用 TLS 587 埠號)
        """
        self.server_host = smtp伺服器
        self.user = 帳號
        self.password = 密碼
        self.port = 埠號

    def 發送(self, 收件者: str, 主旨: str, 內容: str, 格式: str = "plain") -> bool:
        """
        發送電子郵件
        :param 格式: "plain" 為純文字, "html" 為網頁格式
        """
        # 建立郵件物件
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = 收件者
        msg['Subject'] = Header(主旨, 'utf-8').encode()

        # 附加內文
        msg.attach(MIMEText(內容, 格式, 'utf-8'))

        try:
            # 建立 SMTP 連線
            server = smtplib.SMTP(self.server_host, self.port)
            server.starttls()  # 啟用安全傳輸
            server.login(self.user, self.password)
            
            # 發送郵件
            server.sendmail(self.user, [收件者], msg.as_string())
            server.quit()
            
            logging.info(f"Email 成功發送至 {收件者}")
            return True
        except Exception as e:
            logging.exception(f"Email 發送失敗: {e}")
            return False


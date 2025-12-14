# 檔案操作_工具箱_f.py
import os
import csv
from typing import List

# =========================
# 5️⃣ 檔案操作（原本的）
# =========================
def 取得當前工作目錄() -> str:
    """取得當前工作目錄"""
    return os.getcwd()

def 切換工作目錄(目錄: str) -> None:
    """切換工作目錄"""
    return os.chdir(目錄)

def 列出資料夾項目(路徑: str) -> list[str]:
    """列出資料夾項目"""
    return os.listdir(path=路徑)

def 讀檔(路徑: str) -> str:
    with open(路徑, "r", encoding="utf-8") as f:
        return f.read()

def 寫檔(路徑: str, 內容: str):
    with open(路徑, "w", encoding="utf-8") as f:
        f.write(內容)

def 讀CSV(路徑: str) -> List[List]:
    with open(路徑, newline="", encoding="utf-8") as csvfile:
        return list(csv.reader(csvfile))

def 寫CSV(路徑: str, 資料: List[List]):
    with open(路徑, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(資料)

def 批量替換(資料夾: str, 舊字: str, 新字: str):
    for 檔案 in os.listdir(資料夾):
        路徑 = os.path.join(資料夾, 檔案)
        if os.path.isfile(路徑):
            try:
                with open(路徑, "r", encoding="utf-8") as f:
                    內容 = f.read()
                
                新內容 = 內容.replace(舊字, 新字)
                
                with open(路徑, "w", encoding="utf-8") as f:
                    f.write(新內容)
            except Exception as e:
                print(f"處理檔案 {路徑} 失敗: {e}")

def 計算路徑字數(路徑: str) -> int:
    with open(路徑, "r", encoding="utf-8") as f:
        return len(f.read())



# =========================
# 🆕 加入 30 個 os 常用指令（method）
# =========================

def 建立資料夾(路徑: str):
    return os.mkdir(路徑)

def 建立多層資料夾(路徑: str):
    return os.makedirs(路徑)

def 刪除空資料夾(路徑: str):
    return os.rmdir(路徑)

def 刪除多層資料夾(路徑: str):
    return os.removedirs(路徑)

def 路徑是否存在(路徑: str) -> bool:
    return os.path.exists(路徑)

def 是否為檔案(路徑: str) -> bool:
    return os.path.isfile(路徑)

def 是否為資料夾(路徑: str) -> bool:
    return os.path.isdir(路徑)

def 取得絕對路徑(路徑: str) -> str:
    return os.path.abspath(路徑)

def 路徑合併(*args) -> str:
    return os.path.join(*args)

def 分離路徑(路徑: str) -> tuple:
    return os.path.split(路徑)

def 分離副檔名(路徑: str) -> tuple:
    return os.path.splitext(路徑)

def 取得檔案大小(路徑: str) -> int:
    return os.path.getsize(路徑)

def 取得環境變數(名稱: str):
    return os.getenv(名稱)

def 設定環境變數(名稱: str, 值: str):
    os.environ[名稱] = 值
    return 值

def 執行系統指令(指令: str) -> int:
    return os.system(指令)

def 取得使用者名稱() -> str:
    return os.getlogin()

def 取得CPU核心數():
    return os.cpu_count()

def 修改檔名(舊: str, 新: str):
    return os.rename(舊, 新)

def 刪除檔案(路徑: str):
    return os.remove(路徑)

def 取得最後修改時間(路徑: str) -> float:
    return os.path.getmtime(路徑)

def 取得建立時間(路徑: str) -> float:
    return os.path.getctime(路徑)

def 建立符號連結(來源: str, 連結名: str):
    return os.symlink(來源, 連結名)

def 取得程式所在目錄() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def 修改檔案權限(路徑: str, 權限: int):
    return os.chmod(路徑, 權限)

def 取得進程ID() -> int:
    return os.getpid()

def 取得父進程ID() -> int:
    return os.getppid()

def 遍歷資料夾(路徑: str):
    for root, dirs, files in os.walk(路徑):
        return {"路徑": root, "資料夾": dirs, "檔案": files}

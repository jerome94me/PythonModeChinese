import os
import csv
from typing import List, Union, Tuple, Dict, Any


def 取得當前工作目錄() -> str:
    """
    取得 Python 腳本目前執行的工作目錄 (Current Working Directory, CWD)。

    Returns:
        str: 當前工作目錄的路徑字串。
    """
    return os.getcwd()

def 切換工作目錄(目錄: str) -> None:
    """
    將當前工作目錄切換到指定的路徑。

    Args:
        目錄 (str): 欲切換到的新目錄路徑。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    os.chdir(目錄)

def 列出資料夾項目(路徑: str) -> list[str]:
    """
    列出指定路徑下所有檔案和資料夾的名稱。

    Args:
        路徑 (str): 欲列出項目的資料夾路徑。

    Returns:
        list[str]: 包含該目錄下所有項目名稱的列表。
    """
    return os.listdir(path=路徑)

def 讀檔(路徑: str) -> str:
    """
    以 UTF-8 編碼讀取指定路徑的檔案內容。

    Args:
        路徑 (str): 欲讀取檔案的完整路徑。

    Returns:
        str: 檔案的全部內容字串。
    """
    with open(路徑, "r", encoding="utf-8") as f:
        return f.read()

def 寫檔(路徑: str, 內容: str) -> None:
    """
    以 UTF-8 編碼將內容寫入指定檔案。如果檔案存在則覆蓋。

    Args:
        路徑 (str): 欲寫入或創建檔案的完整路徑。
        內容 (str): 欲寫入檔案的內容字串。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    with open(路徑, "w", encoding="utf-8") as f:
        f.write(內容)

def 讀CSV(路徑: str) -> List[List[str]]:
    """
    以 UTF-8 編碼讀取指定路徑的 CSV 檔案，並回傳為巢狀列表。

    Args:
        路徑 (str): 欲讀取 CSV 檔案的完整路徑。

    Returns:
        List[List[str]]: 巢狀列表，每個內部列表代表 CSV 中的一行數據 (元素為字串)。
    """
    with open(路徑, newline="", encoding="utf-8") as csvfile:
        return list(csv.reader(csvfile))

def 寫CSV(路徑: str, 資料: List[List[Any]]) -> None:
    """
    以 UTF-8 編碼將巢狀列表寫入指定的 CSV 檔案。如果檔案存在則覆蓋。

    Args:
        路徑 (str): 欲寫入或創建 CSV 檔案的完整路徑。
        資料 (List[List[Any]]): 巢狀列表，每行數據是一個內部列表。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    with open(路徑, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(資料)

def 批量替換(資料夾: str, 舊字: str, 新字: str) -> None:
    """
    遍歷指定資料夾中的所有檔案，將檔案內容中的舊字串替換為新字串，並寫回檔案。
    
    Args:
        資料夾 (str): 欲處理檔案所在的目錄路徑。
        舊字 (str): 欲被替換的目標字串。
        新字 (str): 用於替換的新字串。
    
    Returns:
        None: 此函數沒有回傳值。
    """
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
                # 友善的錯誤提示
                print(f"處理檔案 {路徑} 失敗: {e}") 

def 計算路徑字數(路徑: str) -> int:
    """
    計算指定路徑檔案中的字元數量 (字數)。

    Args:
        路徑 (str): 欲計算字數的檔案完整路徑。

    Returns:
        int: 檔案內容的字元總數。
    """
    with open(路徑, "r", encoding="utf-8") as f:
        return len(f.read())


# =========================
# 🆕 加入 os 常用指令（method） & os.path 擴充功能
# =========================

def 建立資料夾(路徑: str) -> None:
    """
    在指定路徑建立單層資料夾。如果目錄已存在，會拋出 FileExistsError。

    Args:
        路徑 (str): 欲建立的資料夾路徑。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    os.mkdir(路徑)

def 建立多層資料夾(路徑: str) -> None:
    """
    建立多層巢狀資料夾。如果中間或最終目錄已存在，不會拋出錯誤 (除非指定 exist_ok=False)。

    Args:
        路徑 (str): 欲建立的資料夾路徑 (例如: 'a/b/c')。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    os.makedirs(路徑)

def 刪除空資料夾(路徑: str) -> None:
    """
    刪除指定的**空**資料夾。如果資料夾不為空，會拋出 OSError。

    Args:
        路徑 (str): 欲刪除的資料夾路徑。

    Returns:
        None: 此函數沒有回傳值。
    """
    os.rmdir(路徑)

def 刪除多層資料夾(路徑: str) -> None:
    """
    遞迴地刪除路徑中的空資料夾。如果路徑中有檔案，則停止刪除。

    Args:
        路徑 (str): 欲刪除的資料夾路徑。
    
    Returns:
        None: 此函數沒有回傳值。
    """
    os.removedirs(路徑)

def 路徑是否存在(路徑: str) -> bool:
    """
    檢查指定路徑是否存在（檔案或資料夾）。

    Args:
        路徑 (str): 欲檢查的路徑。

    Returns:
        bool: 如果路徑存在則為 True，否則為 False。
    """
    return os.path.exists(路徑)

def 是否為檔案(路徑: str) -> bool:
    """
    檢查指定路徑是否為一個常規檔案 (Regular File)。

    Args:
        路徑 (str): 欲檢查的路徑。

    Returns:
        bool: 如果是檔案則為 True，否則為 False。
    """
    return os.path.isfile(路徑)

def 是否為資料夾(路徑: str) -> bool:
    """
    檢查指定路徑是否為一個目錄 (資料夾)。

    Args:
        路徑 (str): 欲檢查的路徑。

    Returns:
        bool: 如果是資料夾則為 True，否則為 False。
    """
    return os.path.isdir(路徑)

def 是否為符號連結(路徑: str) -> bool:
    """
    檢查指定路徑是否為一個符號連結 (Symbolic Link)。

    Args:
        路徑 (str): 欲檢查的路徑。

    Returns:
        bool: 如果是符號連結則為 True，否則為 False。
    """
    return os.path.islink(路徑) # 新增

def 標準化路徑(路徑: str) -> str:
    """
    標準化路徑，消除重複的斜線、處理 '.' 和 '..' 等相對路徑表示。

    Args:
        路徑 (str): 欲標準化的路徑。

    Returns:
        str: 標準化後的路徑字串。
    """
    return os.path.normpath(路徑) # 新增

def 取得絕對路徑(路徑: str) -> str:
    """
    將相對路徑轉換為完整的絕對路徑。

    Args:
        路徑 (str): 欲轉換的路徑。

    Returns:
        str: 該路徑的絕對路徑字串。
    """
    return os.path.abspath(路徑)

def 取得路徑中的檔名(路徑: str) -> str:
    """
    從完整路徑中提取出檔名部分 (包含副檔名)。

    Args:
        路徑 (str): 欲處理的完整路徑。

    Returns:
        str: 檔名部分。
    """
    return os.path.basename(路徑) # 新增

def 取得路徑中的目錄(路徑: str) -> str:
    """
    從完整路徑中提取出目錄部分 (不含檔名)。

    Args:
        路徑 (str): 欲處理的完整路徑。

    Returns:
        str: 目錄路徑。
    """
    return os.path.dirname(路徑) # 新增

def 路徑合併(*args: str) -> str:
    """
    智慧地合併一個或多個路徑組成部分，確保在不同作業系統下使用正確的分隔符。

    Args:
        *args (str): 任意數量的路徑組成部分。

    Returns:
        str: 合併後的路徑字串。
    """
    return os.path.join(*args)

def 分離路徑(路徑: str) -> Tuple[str, str]:
    """
    將路徑分離為目錄部分和檔名部分。

    Args:
        路徑 (str): 欲分離的路徑。

    Returns:
        tuple: (目錄路徑, 檔名) 的元組。
    """
    return os.path.split(路徑)

def 分離副檔名(路徑: str) -> Tuple[str, str]:
    """
    將路徑分離為主檔名（不含副檔名）和副檔名部分。

    Args:
        路徑 (str): 欲分離的路徑。

    Returns:
        tuple: (主檔名部分, 副檔名部分) 的元組。
    """
    return os.path.splitext(路徑)

def 取得檔案大小(路徑: str) -> int:
    """
    取得指定檔案的大小（位元組數）。

    Args:
        路徑 (str): 欲取得大小的檔案路徑。

    Returns:
        int: 檔案大小（位元組）。
    """
    return os.path.getsize(路徑)

def 取得環境變數(名稱: str) -> Union[str, None]:
    """
    取得指定環境變數的值。

    Args:
        名稱 (str): 環境變數的名稱。

    Returns:
        Union[str, None]: 環境變數的值字串，如果變數不存在則為 None。
    """
    return os.getenv(名稱)

def 設定環境變數(名稱: str, 值: str) -> str:
    """
    設定或修改一個環境變數的值。

    Args:
        名稱 (str): 欲設定的環境變數名稱。
        值 (str): 欲設定的值。

    Returns:
        str: 設定後的值 (即傳入的 '值')。
    """
    os.environ[名稱] = 值
    return 值

def 執行系統指令(指令: str) -> int:
    """
    在子 shell 中執行指定的作業系統指令。

    Args:
        指令 (str): 欲執行的系統指令字串。

    Returns:
        int: 系統指令的退出狀態碼（0 通常表示成功）。
    """
    return os.system(指令)

def 取得使用者名稱() -> str:
    """
    取得當前登入的使用者名稱。

    Returns:
        str: 當前使用者名稱字串。
    """
    return os.getlogin()

def 取得CPU核心數() -> Union[int, None]:
    """
    取得系統中的 CPU 核心數量（邏輯或實體核心，取決於作業系統）。

    Returns:
        int: CPU 核心數。
    """
    return os.cpu_count()

def 修改檔名(舊: str, 新: str) -> None:
    """
    將檔案或資料夾從舊名稱重命名為新名稱。

    Args:
        舊 (str): 舊的檔案或資料夾路徑/名稱。
        新 (str): 新的檔案或資料夾路徑/名稱。

    Returns:
        None: 此函數沒有回傳值。
    """
    os.rename(舊, 新)

def 刪除檔案(路徑: str) -> None:
    """
    刪除指定路徑的檔案。如果路徑是目錄，會拋出 IsADirectoryError。

    Args:
        路徑 (str): 欲刪除的檔案路徑。

    Returns:
        None: 此函數沒有回傳值。
    """
    os.remove(路徑)

def 取得最後修改時間(路徑: str) -> float:
    """
    取得檔案或資料夾的最後修改時間（時間戳記，自 Epoch 以來的秒數）。

    Args:
        路徑 (str): 欲查詢的路徑。

    Returns:
        float: 最後修改時間的時間戳記。
    """
    return os.path.getmtime(路徑)

def 取得建立時間(路徑: str) -> float:
    """
    取得檔案或資料夾的建立時間（時間戳記，自 Epoch 以來的秒數）。
    
    注意：在某些作業系統上（如 Linux），這可能回傳最後一次 'metadata' 改變的時間。

    Args:
        路徑 (str): 欲查詢的路徑。

    Returns:
        float: 建立時間的時間戳記。
    """
    return os.path.getctime(路徑)

def 建立符號連結(來源: str, 連結名: str) -> None:
    """
    為指定的來源路徑創建一個符號連結（Symbolic Link）。

    Args:
        來源 (str): 實際檔案或目錄的原始路徑。
        連結名 (str): 欲創建的符號連結名稱/路徑。

    Returns:
        None: 此函數沒有回傳值。
    """
    os.symlink(來源, 連結名)

def 取得程式所在目錄() -> str:
    """
    取得當前 Python 腳本檔案所在的目錄路徑。
    
    注意：此函數依賴於 `__file__` 變數，在某些執行環境（如互動式 shell）中可能不適用。

    Returns:
        str: 腳本所在的絕對目錄路徑。
    """
    # 這是標準的寫法，但需要確保 __file__ 變數存在
    return os.path.dirname(os.path.abspath(__file__))

def 修改檔案權限(路徑: str, 權限: int) -> None:
    """
    變更指定路徑的檔案或資料夾的權限模式 (Mode)。
    
    權限通常是一個八進位數，例如 0o777 (完全開放)。

    Args:
        路徑 (str): 欲修改權限的路徑。
        權限 (int): 新的權限模式，使用八進位表示 (如 0o755)。

    Returns:
        None: 此函數沒有回傳值。
    """
    os.chmod(路徑, 權限)

def 取得進程ID() -> int:
    """
    取得當前 Python 腳本進程 (Process) 的唯一識別碼 (ID)。

    Returns:
        int: 當前進程的 PID。
    """
    return os.getpid()

def 取得父進程ID() -> int:
    """
    取得啟動當前 Python 腳本的父進程 (Parent Process) 的 ID。

    Returns:
        int: 父進程的 PPID。
    """
    return os.getppid()

def 遍歷資料夾(路徑: str) -> Union[Dict[str, Union[str, List[str]]], None]:
    """
    遞迴遍歷指定目錄下的所有目錄和檔案（類似 os.walk 的單次迭代）。
    
    注意：此函數只回傳 os.walk 在**第一個**層級迭代的結果。

    Args:
        路徑 (str): 欲開始遍歷的根目錄路徑。

    Returns:
        Dict[str, Union[str, List[str]]]: 包含 '路徑' (根目錄)、'資料夾' (當前層級目錄列表) 和 '檔案' (當前層級檔案列表) 的字典。
    """
    for root, dirs, files in os.walk(路徑):
        return {"路徑": root, "資料夾": dirs, "檔案": files}
def 創建zip(zip名: str, 要加入的內容: list) -> None:
    """
    創建一個 .zip 檔案，並將 '要加入的內容' 列表中的所有檔案添加到其中。

    Args:
        zip名 (str): 要創建的 zip 檔案的名稱 (例如: 'archive.zip')。
        要加入的內容 (list): 包含要壓縮的檔案路徑的列表。
    """
    import zipfile
    
    # 使用 'w' 模式 (寫入) 打開 zip 檔案
    # 'with' 語句確保檔案在操作完成後會被正確關閉
    with zipfile.ZipFile(file=zip名, mode="w") as zf:
        # 遍歷 '要加入的內容' 列表中的每個檔案路徑
        for 檔案路徑 in 要加入的內容:
            try:
                zf.write(檔案路徑)
            except FileNotFoundError:
                pass
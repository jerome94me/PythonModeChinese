from typing import Union, Tuple, List, ItemsView, Iterable
from tkinter import filedialog
from tkinter import Misc

# 1. 選擇目錄 (askdirectory)
def 選擇目錄(
    標題: str,
    起始目錄: str,
    父視窗: Union[Misc, None] = None
) -> Union[str, None]:
    """
    [askdirectory] 開啟「選擇目錄」視窗，讓使用者選擇一個資料夾的路徑。

    Returns:
        Union[str, None]: 選擇的目錄路徑 (str)，如果使用者取消則回傳 None。
    """
    路徑 = filedialog.askdirectory(title=標題, initialdir=起始目錄, parent=父視窗)
    return 路徑 if 路徑 else None


# 2. 開啟單個檔案 (askopenfilename)
def 開啟單個檔案(
    標題: str,
    起始目錄: str,
    檔案類型: Iterable[Tuple[str, Union[str, List[str], Tuple[str, ...]]]], 
    父視窗: Union[Misc, None] = None
) -> Union[str, None]:
    """
    [askopenfilename] 開啟「開啟舊檔」視窗，讓使用者選擇單個檔案的路徑。

    Returns:
        Union[str, None]: 選擇的檔案路徑 (str)，如果使用者取消則回傳 None。
    """
    路徑 = filedialog.askopenfilename(title=標題, initialdir=起始目錄, filetypes=檔案類型, parent=父視窗)
    return 路徑 if 路徑 else None


# 3. 開啟多個檔案 (askopenfilenames)
def 開啟多個檔案(
    標題: str,
    起始目錄: str,
    檔案類型: Iterable[Tuple[str, Union[str, List[str], Tuple[str, ...]]]], 
    父視窗: Union[Misc, None] = None
) -> Tuple:
    """
    [askopenfilenames] 開啟「開啟舊檔」視窗，讓使用者選擇多個檔案的路徑。

    Returns:
        Union[Tuple[str, ...], None]: 選擇的檔案路徑元組 (Tuple[str, ...])，如果使用者取消則回傳 None。
    """
    路徑元組 = filedialog.askopenfilenames(title=標題, initialdir=起始目錄, filetypes=檔案類型, parent=父視窗)
    # askopenfilenames 取消時回傳空元組 ()
    return tuple(路徑元組)

# 4. 另存新檔 (asksaveasfilename)
def 另存新檔(
    標題: str,
    起始目錄: str,
    檔案類型: Iterable[Tuple[str, Union[str, List[str], Tuple[str, ...]]]],
    預設副檔名: str = "",
    父視窗: Union[Misc, None] = None
) -> Union[str, None]:
    """
    [asksaveasfilename] 開啟「另存新檔」視窗，讓使用者指定儲存路徑。

    Returns:
        Union[str, None]: 使用者指定儲存的路徑 (str)，如果使用者取消則回傳 None。
    """
    路徑 = filedialog.asksaveasfilename(
        title=標題,
        initialdir=起始目錄,
        filetypes=檔案類型,
        defaultextension=預設副檔名,
        parent=父視窗
    )
    return 路徑 if 路徑 else None


# 5. 開啟單個檔案物件 (askopenfile)

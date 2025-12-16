from rich.console import Console
from rich.traceback import install
from typing import Optional, Any, TextIO


class 控制台:
    """
    控制台類別：用於管理和美化終端機 (控制台) 輸出。
    """

    def __init__(
        self,
        啟用美化除錯: bool = True,
        顯示區域變數: bool = True,
        最大框架數: int = 100,
        **kwargs: Any
    ):
        """
        Args:
            啟用美化除錯: 是否啟用 Rich Traceback
            顯示區域變數: traceback 中顯示區域變數
            最大框架數: traceback 顯示的最大呼叫層數
            **kwargs: 傳給 rich.console.Console
        """
        self._console = Console(**kwargs)

        # ✅ 安裝 Rich 美化 traceback
        if 啟用美化除錯:
            install(
                console=self._console,
                show_locals=顯示區域變數,
                max_frames=最大框架數
            )

    def 輸出(
        self,
        *物件: Any,
        分隔符: str = " ",
        樣式: Optional[str] = None,
        新行: bool = True,
        消除: bool = False,
        檔案: Optional[TextIO] = None
    ) -> None:
        self._console.print(
            *物件,
            sep=分隔符,
            style=樣式,
            end="\n" if 新行 else "",
            markup=not 消除
        )

    def 寫入(self, 文字: str, 樣式: Optional[str] = None) -> None:
        self._console.print(文字, style=樣式, markup=False)

    def 帶有時間的log(
        self,
        *物件: Any,
        分隔符: str = " ",
        樣式: Optional[str] = None,
        表情符號: bool = True,
        標記: bool = True,
        高亮: bool = True,
        顯示區域變數: bool = False
    ) -> None:
        self._console.log(
            *物件,
            sep=分隔符,
            style=樣式,
            emoji=表情符號,
            markup=標記,
            highlight=高亮,
            log_locals=顯示區域變數
        )

    # ✅ 新增：安全執行（自動顯示美化錯誤）
    def 安全執行(self, 函式, *args, **kwargs):
        """
        執行函式並自動捕捉例外，錯誤會用 Rich Traceback 顯示
        """
        try:
            return 函式(*args, **kwargs)
        except Exception as e:
            self._console.print("[bold red]發生例外錯誤[/bold red]")
            raise  # 重新拋出，讓 Rich Traceback 接手

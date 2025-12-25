import os
import time
from typing import Any, List, Optional, Union, Dict
from rich.console import Console
from rich.progress import *
from rich.columns import Columns
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.tree import Tree
from rich.layout import Layout
from rich.syntax import Syntax
from rich.rule import Rule
from rich.prompt import Prompt
from rich.traceback import install as install_traceback
from rich.pretty import Pretty

# ==========================================
# 1. 核心排版引擎 (Core Layout)
# ==========================================
class 排版引擎:
    def __init__(self, console: Console):
        self._console = console

    def 分隔線(self, 標題: str = "", 樣式: str = "bold blue"):
        self._console.print(Rule(標題, style=樣式))

    def 渲染並排(self, 內容列表: List[Any], 標題: str = ""):
        面板列表 = [Panel(str(c), title=f"{標題} {i+1}", expand=True) for i, c in enumerate(內容列表)]
        self._console.print(Columns(面板列表))

    def 建立標準佈局(self) -> Layout:
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3),
        )
        layout["main"].split_row(
            Layout(name="side", size=30),
            Layout(name="body")
        )
        return layout

# ==========================================
# 2. 視覺化工具 (Visualization - 含動態進度)
# ==========================================
class 視覺化工具:
    def __init__(self, console: Console):
        self._console = console

    def 渲染樹(self, 節點資料: Dict[str, Any], 標題: str = "Root"):
        def 建立樹(目前樹: Tree, 資料: Any):
            if isinstance(資料, dict):
                for k, v in 資料.items():
                    分支 = 目前樹.add(f"[bold cyan]{k}[/]")
                    建立樹(分支, v)
            elif isinstance(資料, list):
                for 項 in 資料: 建立樹(目前樹, 項)
            else:
                目前樹.add(str(資料))
        
        新樹 = Tree(f"[bold yellow]{標題}[/]")
        建立樹(新樹, 節點資料)
        self._console.print(新樹)

    def 自動表格(self, 資料: Union[Dict, List[Dict]], 標題: str = ""):
        table = Table(title=標題)
        if isinstance(資料, dict):
            table.add_column("項目", style="cyan")
            table.add_column("數值", style="magenta")
            for k, v in 資料.items(): table.add_row(str(k), str(v))
        elif isinstance(資料, list) and len(資料) > 0:
            for k in 資料[0].keys(): table.add_column(k)
            for item in 資料: table.add_row(*[str(item.get(k, "")) for k in 資料[0].keys()])
        self._console.print(table)

    def 渲染代碼(self, 代碼: str, 語言: str = "python"):
        self._console.print(Syntax(代碼, 語言, line_numbers=True, theme="monokai"))

    def 載入中(self, 訊息: str = "處理中...", 動畫類型: str = "dots"):
        """旋轉等待動畫"""
        return self._console.status(訊息, spinner=動畫類型)

    def 建立進度條(self) -> Progress:
        """建立高級進度條物件"""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=self._console
        )

# ==========================================
# 3. 主控制中心 (The Master Controller)
# ==========================================
class 控制台:
    def __init__(self, 美化錯誤: bool = True, 紀錄模式: bool = True):
        self._console = Console(record=紀錄模式)
        
        # 初始化子類別
        self.排版 = 排版引擎(self._console)
        self.視覺 = 視覺化工具(self._console)

        if 美化錯誤:
            install_traceback(console=self._console, show_locals=True)

    def 輸出(self, *物件: Any, 樣式: Optional[str] = None):
        for 項 in 物件:
            if isinstance(項, (dict, list, tuple)):
                self._console.print(Pretty(項, expand_all=True))
            else:
                self._console.print(項, style=樣式)

    def 日誌(self, 文字: str):
        self._console.log(文字)

    def 詢問(self, 問題: str, 選項: Optional[List[str]] = None, 預設值: Any = None):
        """基礎互動功能，直接放在主類別"""
        return Prompt.ask(問題, choices=選項, default=預設值, console=self._console)

    def 安全執行(self, 函式: Any, *參數: Any, **參數組: Any):
        try:
            return 函式(*參數, **參數組)
        except Exception:
            self._console.print_exception(show_locals=True)
            return None

    def 匯出結果(self, 檔名: str = "output.html"):
        self._console.save_html(檔名)

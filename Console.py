import time
import rich
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.progress import track, Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn
from rich.traceback import install
from rich import print as rprint # 使用 rich.print 讓輸出自動格式化

# 初始化 Console
# 這將是所有輸出的主要目標
console = Console()

class 美化錯誤:
    """
    Rich Traceback 設置類別。
    用於美化 Python 的錯誤追蹤回溯輸出。
    """
    def __init__(self):
        # 使用 install() 替換系統預設的 traceback 處理器
        install(
            show_locals=True,      # 在每個堆棧幀中顯示區域變數
            suppress=[rich],       # 隱藏 Rich 函式庫內部的追蹤框架
            console=console        # 使用我們定義的 console 實例
        )
        # console.print("[bold yellow]Rich Traceback 已安裝。[/bold yellow]")

    def demonstrate_traceback(self):
        """
        故意觸發一個錯誤來展示 Rich 追蹤回溯的效果。
        """
        console.print("\n" + "="*20 + " [bold red]Rich Traceback 示範[/bold red] " + "="*20)
        console.print("[yellow]即將嘗試一個除以零的操作，請查看美化後的錯誤輸出。[/yellow]")
        
        # 故意引發錯誤
        def calculate(a, b):
            local_var_x = 100
            result = a / b
            return result

        try:
            calculate(10, 0)
        except Exception:
            # 雖然 install() 已經處理了未捕獲的異常，
            # 但這裡我們手動展示如何列印捕獲到的異常 (效果相同)
            console.print_exception(
                show_locals=True, 
                word_wrap=True,
                max_frames=5 # 最多顯示 5 個堆棧幀
            )

class 表格:
    """
    Rich Table 創建和展示類別。
    """
    def demonstrate_table(self):
        console.print("\n" + "="*20 + " [bold blue]Rich Table 示範[/bold blue] " + "="*20)
        
        table = Table(
            title="終端機軟體功能比較", 
            show_header=True, 
            header_style="bold magenta", 
            border_style="cyan"
        )

        # 添加欄位 (Columns)
        table.add_column("功能名稱", style="dim", width=12)
        table.add_column("Rich", style="green", justify="center")
        table.add_column("標準庫", style="red", justify="center")
        table.add_column("備註", style="white")

        # 添加行 (Rows)
        table.add_row("富文本", "✅", "❌", "內建顏色和樣式解析")
        table.add_row("進度條", "⭐⭐⭐", "❌", "支持多任務和 ETA")
        table.add_row("追蹤回溯", "✅", "❌", "可程式碼高亮，隱藏無用框架")
        table.add_row("Markdown", "✅", "❌", "直接渲染 Markdown")
        
        # 輸出表格
        console.print(table)


class 樹狀圖:
    """
    Rich Tree 樹狀結構展示類別。
    """
    def demonstrate_tree(self):
        console.print("\n" + "="*20 + " [bold green]Rich Tree 示範[/bold green] " + "="*20)
        
        # 創建根節點
        file_tree = Tree(
            "[bold white]專案結構/[/bold white]",
            guide_style="bright_blue"
        )

        # 添加子節點
        app_branch = file_tree.add("[bold yellow]app/[/bold yellow]")
        
        # 巢狀子節點
        config_branch = app_branch.add("[bold magenta]config/[/bold magenta]")
        config_branch.add("config.ini")
        config_branch.add("[red]secret.key[/red] ([italic]忽略此檔案[/italic])")
        
        app_branch.add("main.py ([green]主要邏輯[/green])")
        app_branch.add("utils.py")

        # 另一個分支
        doc_branch = file_tree.add("[bold cyan]docs/[/bold cyan]")
        doc_branch.add("README.md")
        doc_branch.add("CHANGELOG.txt")
        
        # 輸出樹狀結構
        console.print(file_tree)


class 進度條:
    """
    Rich Progress 進度條管理類別。
    展示單一任務和多任務進度條。
    """
    def demonstrate_progress(self):
        console.print("\n" + "="*20 + " [bold magenta]Rich Progress 示範[/bold magenta] " + "="*20)

        # 1. 簡單進度條 (使用 track 輔助函數)
        console.print("[yellow]1. 簡單任務進度 (使用 track):[/yellow]")
        for _ in track(range(50), description="[green]資料下載中...[/green]"):
            time.sleep(0.01)

        # 2. 多任務進度條 (使用 Progress 類別)
        console.print("\n[yellow]2. 多任務並行進度:[/yellow]")
        
        # 定義進度條的列佈局
        progress = Progress(
            "{task.description}",  # 任務名稱
            SpinnerColumn(),       # 旋轉動畫
            BarColumn(),           # 進度條
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), # 百分比
            TimeRemainingColumn(), # 剩餘時間
            console=console
        )

        with progress:
            # 定義三個並行的任務
            task1 = progress.add_task("[red]處理檔案 A[/red]", total=300)
            task2 = progress.add_task("[cyan]連接伺服器[/cyan]", total=100)
            task3 = progress.add_task("[green]任務 B 預處理[/green]", total=500)

            while not progress.finished:
                # 每個任務以不同的速度推進
                if not progress.finished:
                    progress.update(task1, advance=0.5)
                if not progress.finished:
                    progress.update(task2, advance=0.2)
                if not progress.finished:
                    progress.update(task3, advance=1)
                
                time.sleep(0.005)


class 控制台:
    """
    Rich Console 和基本功能的展示類別。
    展示 log, print 和 Panel。
    """
    def demonstrate_console(self):
        console.print("\n" + "="*20 + " [bold cyan]Rich Console 核心示範[/bold cyan] " + "="*20)

        # 1. console.print (富文本輸出)
        console.print(
            "這是一個[bold underline magenta]重要的訊息[/bold underline magenta]，",
            "它包含了[italic yellow]多個樣式[/italic yellow]的片段。"
        )

        # 2. console.log (帶有時間戳的日誌)
        console.log("程序開始運行...")
        time.sleep(0.1)
        
        # 輸出 Python 物件
        data = {"status": "OK", "count": 120}
        console.log("配置數據已加載:", data)
        
        console.log("[bold green]操作成功完成。[/bold green]")
        
        # 3. Panel (面板)
        from rich.panel import Panel
        console.print(
            Panel(
                "[bold white]版本資訊：V1.2.3\n作者：[link=https://example.com]AI 助手[/link][/bold white]",
                title="[red]系統警告[/red]",
                subtitle="運行狀態：[green]正常[/green]",
                border_style="red"
            )
        )



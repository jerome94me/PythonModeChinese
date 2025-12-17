import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import yt_dlp
from typing import Tuple, List, Union

class 基本操作:    
    def 讀取影像(圖片路徑: str) -> np.ndarray:
        """
        讀取圖片，如果路徑含有中文，建議使用 numpy decode 的方式讀取，
        這裡暫時使用標準 cv2.imread
        """
        img = cv2.imread(圖片路徑)
        if img is None:
            raise ValueError(f"無法讀取影像，請檢查路徑: {圖片路徑}")
        return img

    def 顯示圖片(
            讀取過的影像: np.ndarray,
            視窗標題: str = "Image", 
            等待時間或是按鍵: int = 0
    ):
        """
        顯示圖片視窗
        :param 等待時間或是按鍵: 0 代表無限等待，直到按下任意鍵；輸入數字代表毫秒(ms)
        """
        cv2.imshow(視窗標題, 讀取過的影像)
        cv2.waitKey(等待時間或是按鍵)
        cv2.destroyAllWindows()

    def 取得長寬與色版數量(讀取過的影像: np.ndarray) -> Tuple[int, int, int]:
        """
        回傳元組: (寬度 Width, 高度 Height, 色版數量 Channels)
        注意：OpenCV 原生 shape 是 (高, 寬, 色版)
        """
        高, 寬, 色版 = 讀取過的影像.shape
        return (寬, 高, 色版)

    def 取得像素總數(讀取過的影像: np.ndarray) -> int:
        return 讀取過的影像.size
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from typing import List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from typing import List, Tuple, Union

class 圖表:
    # --- 基礎設定 ---
    @staticmethod
    def 設定中文字型():
        """
        設定 Matplotlib 的中文字型，避免亂碼。
        """
        import platform
        system = platform.system()
        if system == "Windows":
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
        elif system == "Darwin": # Mac
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        else:
            plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    # --- 折線圖 (含動畫選項) ---
    @staticmethod
    def 繪製折線圖(x數據: List, y數據: List, 標題: str = "折線圖", 動畫: bool = False):
        fig, ax = plt.subplots()
        ax.set_title(標題)
        ax.set_xlabel("X 軸")
        ax.set_ylabel("Y 軸")
        ax.grid(True)

        if 動畫:
            # 初始化一條空的線
            line, = ax.plot([], [], marker='o', lw=2)
            # 設定座標軸範圍，避免動畫跳動
            ax.set_xlim(min(x數據) - 0.5, max(x數據) + 0.5)
            ax.set_ylim(min(y數據) * 0.8, max(y數據) * 1.2)

            def update(frame):
                # 每一幀增加一個數據點
                line.set_data(x數據[:frame], y數據[:frame])
                return line,

            # frames 設定為數據長度+1，interval 為速度(毫秒)
            ani = animation.FuncAnimation(fig, update, frames=len(x數據) + 1, interval=300, repeat=False)
            plt.show()
        else:
            # 一般靜態繪製
            ax.plot(x數據, y數據, marker='o')
            plt.show()

    # --- 長條圖 / 長度圖 (含動畫選項) ---
    @staticmethod
    def 繪製長條圖(類別名稱: List[str], 數值: List, 標題: str = "長條圖", 動畫: bool = False):
        fig, ax = plt.subplots()
        
        if 動畫:
            def update(frame):
                ax.clear() # 清除前一幀
                ax.set_title(標題)
                # 計算當前高度：數值 * (當前幀 / 總幀數)，模擬生長效果
                ratios = np.linspace(0, 1, 30) 
                current_heights = [v * ratios[frame] for v in 數值]
                
                ax.bar(類別名稱, current_heights, color='skyblue')
                ax.set_ylim(0, max(數值) * 1.1) # 固定 Y 軸上限

            ani = animation.FuncAnimation(fig, update, frames=30, interval=40, repeat=False)
            plt.show()
        else:
            # 一般靜態繪製
            ax.bar(類別名稱, 數值, color='skyblue')
            ax.set_title(標題)
            plt.show()
import yt_dlp
import os

import yt_dlp
import os
from typing import List, Union, Dict, Any

class YouTubeTools:
    """
    YouTube 綜合工具組：支援影片/音樂下載、資訊抓取、章節獲取與搜尋。
    """

    # --- 1. 基礎影片下載 ---
    @staticmethod
    def 下載影片(url: str, 畫質: Union[int, str] = '1080', 儲存子目錄: str = "") -> Dict[str, str]:
        format_str = "bestvideo+bestaudio/best" if 畫質 == 'best' else f"bestvideo[height<={畫質}]+bestaudio/best"
        目標路徑 = os.path.join(os.getcwd(), 儲存子目錄, '%(title)s.%(ext)s')
        
        ydl_options = {
            "format": format_str,
            'outtmpl': 目標路徑,
            'merge_output_format': 'mp4',
            'quiet': True,
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}}, # 減少 JS 報錯
        }
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([url])
                return {"狀態": "成功", "訊息": "影片下載完成", "路徑": 目標路徑}
        except Exception as e:
            return {"狀態": "失敗", "訊息": str(e)}

    # --- 2. 僅下載音樂 (MP3) ---
    @staticmethod
    def 下載音樂(url: str, 儲存子目錄: str = "music") -> Dict[str, str]:
        目標路徑 = os.path.join(os.getcwd(), 儲存子目錄, '%(title)s.%(ext)s')
        ydl_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 目標路徑,
            'quiet': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([url])
                return {"狀態": "成功", "訊息": "音樂下載完成"}
        except Exception as e:
            return {"狀態": "失敗", "訊息": str(e)}

    # --- 3. 獲取詳細資訊 (不下載) ---
    @staticmethod
    def 獲取資訊(url: str) -> Dict[str, Any]:
        ydl_options = {'quiet': True}
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    "狀態": "成功",
                    "標題": info.get('title'),
                    "觀看數": info.get('view_count'),
                    "按讚數": info.get('like_count'),
                    "時長_秒": info.get('duration'),
                    "上傳日期": info.get('upload_date'),
                    "解析度": f"{info.get('width')}x{info.get('height')}",
                    "頻道": info.get('uploader'),
                    "縮圖網址": info.get('thumbnail')
                }
        except Exception as e:
            return {"狀態": "失敗", "錯誤訊息": str(e)}

    # --- 4. 獲取影片章節 ---
    @staticmethod
    def 獲取章節(url: str) -> Dict[str, Any]:
        ydl_options = {'quiet': True}
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(url, download=False)
                chapters = info.get('chapters')
                if chapters:
                    return {"狀態": "成功", "章節數量": len(chapters), "內容": chapters}
                return {"狀態": "成功", "訊息": "此影片沒有章節資訊", "內容": []}
        except Exception as e:
            return {"狀態": "失敗", "錯誤訊息": str(e)}

    # --- 5. 下載縮圖 ---
    @staticmethod
    def 下載縮圖(url: str, 儲存子目錄: str = "thumbnails") -> Dict[str, str]:
        目標路徑 = os.path.join(os.getcwd(), 儲存子目錄, '%(title)s.%(ext)s')
        ydl_options = {
            'writethumbnail': True,
            'skip_download': True,
            'outtmpl': 目標路徑,
            'quiet': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([url])
                return {"狀態": "成功", "訊息": "縮圖下載完成"}
        except Exception as e:
            return {"狀態": "失敗", "訊息": str(e)}

    # --- 6. 關鍵字搜尋 ---
    @staticmethod
    def 搜尋(關鍵字: str, 數量: int = 1) -> Dict[str, Any]:
        """ 搜尋關鍵字並回傳第一個結果的資訊 """
        url = f"ytsearch{數量}:{關鍵字}"
        ydl_options = {'quiet': True}
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(url, download=False)
                # 取得搜尋結果列表的第一個
                first_video = info['entries'][0]
                return {
                    "狀態": "成功",
                    "標題": first_video.get('title'),
                    "網址": first_video.get('webpage_url'),
                    "觀看數": first_video.get('view_count')
                }
        except Exception as e:
            return {"狀態": "失敗", "錯誤訊息": str(e)}
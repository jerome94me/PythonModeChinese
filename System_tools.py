from typing import Any, Dict, Union
import psutil

class NotALaptopError(Exception):
    """當在非筆電環境要求電池資訊時觸發"""
    pass

class 硬件監控:
    def __init__(self, 是筆電: bool = False) -> None:
        self.is_laptop = 是筆電

    def 獲取CPU使用率(self, 取樣區間: Union[int, float, None] = 0.5) -> float:
        """獲取 CPU 使用率百分比"""
        return psutil.cpu_percent(取樣區間)

    def 取得記憶體資訊(self, 轉字典: bool = True) -> Union[Dict[str, Any], Any]:
        """取得記憶體狀態 (total, available, percent, used, free)"""
        mem = psutil.virtual_memory()
        return mem._asdict() if 轉字典 else mem

    def 取得硬碟資訊(self, 路徑: str = "/", 轉字典: bool = True) -> Union[Dict[str, Any], Any]:
        """取得指定路徑的硬碟空間"""
        disk = psutil.disk_usage(路徑)
        return disk._asdict() if 轉字典 else disk

    def 取得電池資訊(self) -> Any:
        """取得電池剩餘電量與充電狀態"""
        battery = psutil.sensors_battery()
        if self.is_laptop and battery:
            return battery._asdict()
        elif not self.is_laptop:
            # 這裡就是你自訂的紅牌！
            raise NotALaptopError("❌ 錯誤：這台電腦被設定為『非筆電』，無法獲取電池資訊。")
        else:
            return "偵測不到電池"
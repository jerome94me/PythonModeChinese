

from datetime import datetime, date, timedelta



def 取得當前完整時間() -> datetime:
    """
    獲取包含日期、時間、秒數及微秒的完整 datetime 物件 (本地時間)。
    
    回傳:
        datetime: 包含當前日期與時間的物件。
    """
    return datetime.now()

def 取得當前日期() -> date:
    """
    僅獲取包含年、月、日的 date 物件。
    
    回傳:
        date: 包含當前日期的物件。
    """
    return date.today()

def 格式化當前時間(格式字串: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    獲取當前時間並將其格式化為指定格式的字串。
    
    參數:
        格式字串 (str): 用於格式化的字串代碼，預設為 '年-月-日 時:分:秒'。
                        常用的代碼有: %Y(年), %m(月), %d(日), %H(時), %M(分), %S(秒)。
    
    回傳:
        str: 格式化後的日期時間字串。
    """
    current_dt = datetime.now()
    return current_dt.strftime(格式字串)







def 計算兩個時間差(dt_end: datetime, dt_start: datetime) -> timedelta:
    """
    計算兩個 datetime 物件之間的時間差 (timedelta)。
    
    參數:
        dt_end (datetime): 結束時間。
        dt_start (datetime): 開始時間。
        
    回傳:
        timedelta: 兩個時間之間的差異物件。
    """
    return dt_end - dt_start

def 比較日期前後(dt1: datetime, dt2: datetime) -> str:
    """
    比較兩個日期時間物件的先後順序。
    
    回傳:
        str: 描述兩個日期時間關係的字串。
    """
    if dt1 > dt2:
        return f"{dt1} 在 {dt2} 之後"
    elif dt1 < dt2:
        return f"{dt1} 在 {dt2} 之前"
    else:
        return f"{dt1} 與 {dt2} 相同"

def 字串轉換為時間(日期時間字串: str, 格式字串: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    將指定格式的日期時間字串轉換為 datetime 物件 (strptime)。
    
    參數:
        日期時間字串 (str): 欲轉換的字串。
        格式字串 (str): 字串對應的格式。
        
    回傳:
        datetime: 轉換後的 datetime 物件。
    """
    return datetime.strptime(日期時間字串, 格式字串)



def 檢查是否為閏年(年份: int) -> bool:
    """
    檢查給定的年份是否為閏年。
    
    回傳:
        bool: 如果是閏年，回傳 True。
    """
    # 閏年條件: 能被 4 整除，但不能被 100 整除，或者能被 400 整除。
    return (年份 % 4 == 0 and 年份 % 100 != 0) or (年份 % 400 == 0)





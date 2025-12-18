import pillow
from barcode import EAN13
from barcode.writer import ImageWriter


class BarCode:
    """
    產生條碼用的類別
    註：
    - EAN13 只能使用「12 位數字」
    - 第 13 位檢查碼會自動產生
    """

    def _檢查輸入(self, num: str):
        if not num.isdigit():
            return "錯誤：條碼只能包含數字"
        if len(num) != 12:
            return "錯誤：EAN13 需要 12 位數字"
        return None

    def 產生(self, num: str, filename: str = "BarCode_Output"):
        """
        產生條碼並儲存成 SVG
        """
        error = self._檢查輸入(num)
        if error:
            return error

        barcode = EAN13(num)
        barcode.save(filename)

    def 產生並儲存成JPG(self, num: str, filename: str = "BarCode_Output"):
        """
        產生條碼並儲存成 JPG
        """
        error = self._檢查輸入(num)
        if error:
            return error

        barcode = EAN13(num, writer=ImageWriter())
        barcode.save(filename)


if __name__ == "__main__":
    bc = BarCode()
    bc.產生並儲存成JPG("123456789012", "file")

from openpyxl import Workbook
from openpyxl.drawing.image import Image

# 創建 Workbook
wb = Workbook()
ws = wb.active

# 插入圖片
img_path = "images/『午夜の待ち合わせ』_12.jpg"  # 圖片路徑
img = Image(img_path)

# 將圖片插入到指定儲存格
ws.add_image(img, 'C1')

# 儲存 Excel 檔案
wb.save("output_with_images.xlsx")

from openpyxl import Workbook

# 創建新的 Excel 工作簿
wb = Workbook()
ws1 = wb.active

# 調整所有行高
for row in range(2, ws1.max_row + 1):
    ws1.row_dimensions[row].height = 250  # 設置每一行的高度

# 調整所有列寬
for col in ws1.columns:
    max_length = 0
    col_letter = col[0].column_letter  # 獲取列字母
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2  # 可依據具體需求調整
    ws1.column_dimensions[col_letter].width = adjusted_width

wb.save("Pixiv_resized.xlsx")

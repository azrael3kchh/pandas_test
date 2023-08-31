
import pandas as pd
import numpy as np

# 創建隨機數據
data = np.random.rand(4, 5)  # 生成4行5列的隨機數

# 創建資料框
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

# 輸出資料框
print(df)

def add_column_dataframe(data, index, content):
    """
    新增欄位以及內容
    data，以data_frame格式
    index，str格式
    content，str格式
    """
    try:
        # 新增一個名為 'index' 的欄位，其值為變數 'content'
        data[str(index)] = str(content)
        print(data.to_string())
    except FileNotFoundError:
        print("找不到文件")
    except Exception as error:
        print("發生錯誤:", str(error))

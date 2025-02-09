import pandas as pd
import json

# 读取JSON文件内容
with open(r"E:\3DModels\ABC\result_csgtree\test_results_with_err.json", 'r') as f:
    data = json.load(f)

# 创建一个空的DataFrame，用于存储数据
df = pd.DataFrame(columns=['File', 'Entity Count', 'Hausdorff Error', 'Runtime', 'Volumetric Error'])

# 遍历JSON数据，将每个文件的信息添加到DataFrame中
for file, info in data.items():
    df.loc[len(df)] = [file, info['entity_count'], info['hausdorff_error'], info['runtime'], info['volumetric_error']]

# 将DataFrame保存到Excel文件中
df.to_excel('test_results.xlsx', index=False)
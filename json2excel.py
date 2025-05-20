import pandas as pd
import json

file_path = r"E:\3DModels\ABC\step_siggraph_new"
# 读取JSON文件内容
with open(file_path + r"\test_results.json", 'r') as f:
    data = json.load(f)

# 创建一个空的DataFrame，用于存储数据
df = pd.DataFrame(columns=['File', "face_count", 'Entity Count', 'Hausdorff Error', 'Runtime', 'Volumetric Error'])

# 遍历JSON数据，将每个文件的信息添加到DataFrame中
for file, info in data.items():
    df.loc[len(df)] = [file, info["face_count"], info['entity_count'], info['hausdorff_error'], info['runtime'], info['volumetric_error']]

# 将DataFrame保存到Excel文件中
df.to_excel(file_path + r'\test_results_face_count.xlsx', index=False)
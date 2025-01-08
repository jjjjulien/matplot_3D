import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel表格（假设文件名为 'data.xlsx'，请修改为实际文件名）
file_path = r"C:\Users\Julien\Desktop\Paper\SIGGRAPH2025\figure_plot\test_results.xlsx"  # 请将此路径替换为实际的文件路径
df = pd.read_excel(file_path)

# 提取数据列
entity_count = df['Entity Count']
hausdorff_error = df['Hausdorff Error']
volumetric_error = df['Volumetric Error']
average_runtime = df['Average Runtime']

# 设置字体大小
font_title = 16  # 标题字体大小
font_label = 14  # 坐标轴标签字体大小
font_ticks = 12  # 刻度字体大小
font_text = 12  # 条形文本的字体大小

# 绘制 Entity Count 直方图
plt.figure(figsize=(8, 6))
sns.histplot(entity_count, kde=False, bins=10, color='blue', edgecolor='black')
plt.title('Entity Count Distribution', fontsize=font_title)
plt.xlabel('Entity Count', fontsize=font_label)
plt.ylabel('Frequency', fontsize=font_label)

# 添加数量标签
for p in plt.gca().patches:
    plt.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.2,
             f'{int(p.get_height())}', ha='center', va='bottom', fontsize=font_text, color='black')

# 设置刻度字体大小
plt.xticks(fontsize=font_ticks)
plt.yticks(fontsize=font_ticks)

plt.tight_layout()
plt.show()

# 绘制 Hausdorff Error 直方图
plt.figure(figsize=(8, 6))
sns.histplot(hausdorff_error, kde=False, bins=10, color='green', edgecolor='black')
plt.title('Hausdorff Error Distribution', fontsize=font_title)
plt.xlabel('Hausdorff Error', fontsize=font_label)
plt.ylabel('Frequency', fontsize=font_label)

# 添加数量标签
for p in plt.gca().patches:
    plt.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.2,
             f'{int(p.get_height())}', ha='center', va='bottom', fontsize=font_text, color='black')

# 设置刻度字体大小
plt.xticks(fontsize=font_ticks)
plt.yticks(fontsize=font_ticks)

plt.tight_layout()
plt.show()

# 绘制 Volumetric Error 直方图
plt.figure(figsize=(8, 6))
sns.histplot(volumetric_error, kde=False, bins=10, color='orange', edgecolor='black')
plt.title('Volumetric Error Distribution', fontsize=font_title)
plt.xlabel('Volumetric Error', fontsize=font_label)
plt.ylabel('Frequency', fontsize=font_label)

# 添加数量标签
for p in plt.gca().patches:
    plt.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.2,
             f'{int(p.get_height())}', ha='center', va='bottom', fontsize=font_text, color='black')

# 设置刻度字体大小
plt.xticks(fontsize=font_ticks)
plt.yticks(fontsize=font_ticks)

plt.tight_layout()
plt.show()

# 绘制 Average Runtime 直方图
plt.figure(figsize=(8, 6))
sns.histplot(average_runtime, kde=False, bins=10, color='red', edgecolor='black')
plt.title('Average Runtime Distribution', fontsize=font_title)
plt.xlabel('Average Runtime (seconds)', fontsize=font_label)
plt.ylabel('Frequency', fontsize=font_label)

# 添加数量标签
for p in plt.gca().patches:
    plt.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.2,
             f'{int(p.get_height())}', ha='center', va='bottom', fontsize=font_text, color='black')

# 设置刻度字体大小
plt.xticks(fontsize=font_ticks)
plt.yticks(fontsize=font_ticks)

plt.tight_layout()
plt.show()

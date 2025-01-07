import json
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 20

# 读取JSON文件内容
with open('test_results.json', 'r') as f:
    data = json.load(f)

entity_counts = []
runtimes = []
vol_err = []

# 从JSON数据中提取实体数量和运行时间
for key, value in data.items():
    entity_counts.append(value['entity_count'])
    runtimes.append(value['runtime'])
    vol_err.append(value['VolumetricError'])

# 设置符合英文论文审美的颜色（这里示例使用一组较淡雅的颜色，可按需调整）
colors_bar = ['#589FF3']
colors_boundary = '#DCDCDC'


fig = plt.figure(1)
# 去掉边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
x_ticks = range(1, len(entity_counts) + 1)
# 添加横向的线，设置 zorder 较低
for i in range(0, 70, 10):
    plt.axhline(y=i, color=colors_boundary, linestyle='-', zorder=1)
# 绘制柱状图，设置 zorder 较高
plt.bar(x_ticks, entity_counts, color=colors_bar, zorder=2)
# 设置标签
plt.xlabel('Example ID')
plt.ylabel('Number of nodes in solution')
plt.xticks(x_ticks)
# 给整个图像添加边框
fig.patch.set_edgecolor(colors_boundary)  # 设置边框颜色
fig.patch.set_linewidth(3)        # 设置边框宽度


# 绘制测试模型和运行时间的关系图（柱状图示例）
fig = plt.figure(2)
# 去掉边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
x_ticks = range(1, len(runtimes) + 1)
# 添加横向的线，设置 zorder 较低
for i in range(0, 1001, 200):
    plt.axhline(y=i, color=colors_boundary, linestyle='-', zorder=1)
# 绘制柱状图，设置 zorder 较高
plt.bar(x_ticks, runtimes, color=colors_bar)
plt.xlabel('Example ID')
plt.ylabel('Runtime in millisecond')
plt.xticks(x_ticks)
# 给整个图像添加边框
fig.patch.set_edgecolor(colors_boundary)  # 设置边框颜色
fig.patch.set_linewidth(3)        # 设置边框宽度

fig = plt.figure(3)
# 去掉边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
x_ticks = range(1, len(vol_err) + 1)
# 添加横向的线，设置 zorder 较低
for i in [0, 0.5, 1.0, 1.5, 2.0]:
    plt.axhline(y=i, color=colors_boundary, linestyle='-', zorder=1)
# 绘制柱状图，设置 zorder 较高
plt.bar(x_ticks, vol_err, color=colors_bar, zorder=2)
# 设置标签
plt.xlabel('Example ID')
plt.ylabel('Relative reconstruction error')
plt.xticks(x_ticks)
# 给整个图像添加边框
fig.patch.set_edgecolor(colors_boundary)  # 设置边框颜色
fig.patch.set_linewidth(3)        # 设置边框宽度

plt.show()
# 计算hexagon数列的前五个值

# 创建一个列表来存储数列中的值
hexagons = []

# 循环计算前五个数列值
for n in range(1, 6):
    # 计算第n个hexagon数列值并将其添加到列表中
    hexagon = 2 * n * (2 * n - 1)
    hexagons.append(hexagon)

# 输出数列的前五个值
print("The first five values of the hexagon sequence are:")
for hexagon in hexagons:
    print(hexagon)

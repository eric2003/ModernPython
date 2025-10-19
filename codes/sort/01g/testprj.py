# 定义原始数组和目标数组  
original_array = [10, 20, 5, 8, 25]  
target_array = [25, 8, 20, 10, 5]  

# 初始化 index_map  
index_map = []  

# 遍历目标数组，查找每个元素在原始数组中的索引  
for item in target_array:  
    index = original_array.index(item)  
    index_map.append(index)  

print("index_map:", index_map)  
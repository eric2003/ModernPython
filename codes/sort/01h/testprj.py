# 定义原始数组和目标数组  
original_array = [10, 20, 5, 8, 25]  
target_array = [25, 8, 20, 10, 5]  

# 创建一个字典来存储原始数组的索引  
index_dict = {value: index for index, value in enumerate(original_array)}  

# 使用字典来构建 index_map  
index_map = [index_dict[item] for item in target_array]  

print("index_map:", index_map) 
import numpy as np  

# 初始化两个数组  
original_array = np.array([10, 20, 5, 8, 25])  
index_map = [4, 3, 1, 0, 2]  

# 直接使用 NumPy 数组的索引  
result_array = original_array[index_map]  

print("result_array:", result_array) 
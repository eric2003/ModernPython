original_array = [10, 20, 5, 8, 25]  
target_array = [25, 8, 20, 10, 5]  
index_map = [4, 3, 1, 0, 2]  

# 使用列表推导来重排 original_array  
result_array = [original_array[i] for i in index_map]  

print("original_array:", original_array)
print("target_array:", target_array)
print("index_map:", index_map)
print("result_array:", result_array) 

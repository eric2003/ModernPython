# 原始数组  
original_array = [10, 20, 5, 8, 25]  
original_array1 = [100, 200, 50, 80, 250]  


# 目标数组  
target_array = [25, 8, 20, 10, 5]  

# 创建一个排序map  
sort_map = {value: index for index, value in enumerate(target_array)}  

# 使用排序map对原始数组进行排序  
sorted_array = sorted(original_array, key=lambda x: sort_map[x])  
sorted_array1 = sorted(original_array1, key=lambda x: sort_map[ original_array[original_array1.index(x)] ])  

print(sorted_array) 
print(sorted_array1) 
print(sort_map)  

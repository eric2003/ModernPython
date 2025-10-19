def get_sorted_indices(arr1, arr2):
    sort_map = {value: index for index, value in enumerate(arr2)}
    sorted_indices = []
    for element in arr2:  
        index = sort_map[element] 
        sorted_indices.append(index)
    return sorted_indices
        
# 原始数组  
original_array = [10, 20, 5, 8, 25]  

# 目标数组  
target_array = [25, 8, 20, 10, 5]  

# 创建一个排序map  
sort_map = {value: index for index, value in enumerate(target_array)}  

# 使用排序map对原始数组进行排序  
sorted_array = sorted(original_array, key=lambda x: sort_map[x])  

sorted_indices = get_sorted_indices(original_array, target_array)

print(original_array)
print(sorted_array)
print(sort_map)
print(sorted_indices) 

import csv  

# 要写入的数据  
data = [  
    ['姓名', '年龄', '城市'],  
    ['张三', 28, '北京'],  
    ['李四', 34, '上海'],  
    ['王五', 25, '广州']  
]  

# 将数据写入CSV文件  
with open('output.csv', 'w', newline='', encoding='utf-8') as file:  
    writer = csv.writer(file, delimiter=' ')  
    writer.writerows(data)  
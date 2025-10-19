import csv

with open('example.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # 假设文件的第一行是标题行  
    headers = next(reader)  
    # 文件的列数等于标题行的元素个数  
    num_columns = len(headers)  
    print(f'列数: {num_columns}')
    mylist = []
    for i in range(num_columns):
        c = []
        mylist.append(c)

    icount = 0
    for row in reader:
        for i in range(num_columns):
            mylist[i].append(row[i])
        icount += 1
        
print("icount=",icount)
print("mylist=",mylist)
num_rows = len(mylist)
print("num_rows=",num_rows)
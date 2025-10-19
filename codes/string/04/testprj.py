filepath = 'example.txt'
with open(filepath, 'r', encoding='UTF-8') as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1




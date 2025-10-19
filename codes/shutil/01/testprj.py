import os
import shutil

# 获取当前目录
current_directory = os.getcwd()
print(f"current_directory= {current_directory}")

# 遍历当前目录下的所有子目录
for root, dirs, files in os.walk(current_directory):
    for directory in dirs:
        if directory == "build":
            build_directory = os.path.join(root, directory)
            print(f"Deleting contents of {build_directory}")
            # 删除子目录中的所有内容
            shutil.rmtree(build_directory)

print("Deletion complete")

input()
import os
import shutil


def delete_build_directories(root_dir):
    print(f'root_dir {root_dir}')
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            if dirname == 'build':
                print(f'dirpath {dirpath} dirname {dirname}')
                build_dir = os.path.join(dirpath, dirname)
                print(f'build_dir {build_dir}')
                #shutil.rmtree(build_dir)
                #print(f'Deleted {build_dir}')
                try:
                    shutil.rmtree(build_dir)
                    print(f'Deleted {build_dir}')
                except OSError as e:
                    if e.errno == 13:
                        print(f'Permission denied: {build_dir}')
                    elif e.errno == 16:
                        print(f'Directory not empty: {build_dir}')
                    else:
                        print(f'Error deleting {build_dir}: {e}')                

# 获取当前目录
current_directory = os.getcwd()
print(f"current_directory= {current_directory}")

# 调用函数并传入要删除目录的根目录
delete_build_directories(current_directory)
input()
import os
import shutil

def remove_git_folder(path):
    os.system(f'rd /s /q {path}')

def delete_build_directories(root_dir):
    print(f'root_dir {root_dir}')
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            if dirname == 'build':
                print(f'dirpath {dirpath} dirname {dirname}')
                build_dir = os.path.join(dirpath, dirname)
                print(f'build_dir {build_dir}')
                try:
                    shutil.rmtree(build_dir)
                    print(f'Deleted {build_dir}')
                except OSError as e:
                    if e.errno == 13:
                        print(f'Permission denied: {build_dir}')
                        remove_git_folder(build_dir)
                    elif e.errno == 16:
                        print(f'Directory not empty: {build_dir}')
                    else:
                        print(f'Error deleting {build_dir}: {e}')                

def my_function():
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
        
def cmd_delete_directories():
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    dirname = sys.argv[1]
    delete_build_directories(dirname)

cmd_delete_directories()
input()
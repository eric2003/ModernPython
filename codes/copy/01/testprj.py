class Mesh:
    def __init__(self):
        self.nx = 40

class MyClass:
    def __init__(self, mesh):
        self.mesh = mesh

# 创建 Mesh 类的实例
mesh = Mesh()

# 创建 MyClass 类的实例
my_class_instance = MyClass(mesh)

# 检测 mesh 和 my_class_instance.mesh 是否指向同一个对象
print(mesh is my_class_instance.mesh)  # 输出: True

# 修改 Mesh 实例的属性，观察影响
mesh.nx = 50
print(my_class_instance.mesh.nx)  # 输出: 50，表明 my_class_instance.mesh 和 mesh 是同一个对象
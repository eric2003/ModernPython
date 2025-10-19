from jinja2 import Environment, FileSystemLoader  

# 创建 Jinja2 环境  
env = Environment(loader=FileSystemLoader('templates'))  

# 加载模板  
template = env.get_template('my_template.html')  

# 要传递给模板的数据  
data = {  
    'name': 'Alice',  
    'age': 30,  
    'hobbies': ['阅读', '旅行', '烹饪']  
}  

# 渲染模板  
rendered = template.render(data)  

# 打印渲染后的 HTML 内容  
print(rendered)  
import flet as ft

def main(page: ft.Page):
    # 设置窗口标题
    page.title = "Finance App Test"
    # 在页面加一行字
    page.add(ft.Text("Hello! 你的财务 App 启动成功了。"))

# 启动应用
ft.run(main)
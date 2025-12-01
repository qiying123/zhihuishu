from DrissionPage import WebPage

#menu_url选择作业菜单的url
menu_url=""
#url是考试页面的url
url=''

def run():
    # 1. 启动浏览器
    # DrissionPage 默认会打开一个浏览器窗口，方便调试

    page = WebPage()

    # 2. 访问页面
    page.get(menu_url)
    # page.get(url)

    """目录页点击所有作业，爬取每个作业的所有题目"""
    start_button=page.eles('.themeBg')
    for i in start_button:
        i.click()
        tab = page.latest_tab
        tab.wait.eles_loaded('.el-button el-button--primary is-plain')
        top_div = tab.eles('.subject_describe dynamic-fonts')
        for j in top_div:
            number=j.before(5).text+j.before(3).text
            answers = j.after(2)
            inner_host = j.child()
            shadow_host = inner_host.child()
            try :
                text = shadow_host.shadow_root.child().text
            except:
                text = shadow_host.shadow_root.inner_html
            print(number)
            print(text)
            print(answers.text)
            with open('zuoye.txt', 'a', encoding='utf-8') as f:
                f.write(number)
                f.write(text)
                f.write(answers.text+'\n')

def kaoshi():
    # 1. 启动浏览器
    # DrissionPage 默认会打开一个浏览器窗口，方便调试

    page = WebPage()

    # 2. 访问页面
    page.get(url)

    """进入考试页面，爬取考试的所有题目"""

    tab = page.latest_tab
    tab.wait.eles_loaded('.el-button el-button--primary is-plain')
    top_div = tab.eles('.subject_describe dynamic-fonts')
    for j in top_div:
        number = j.before(5).text + j.before(3).text
        answers = j.after(2)
        inner_host = j.child()
        shadow_host = inner_host.child()
        try:
            text = shadow_host.shadow_root.child().text
        except:
            text = shadow_host.shadow_root.inner_html
        print(number)
        print(text)
        print(answers.text)
        with open('kaoshi.txt', 'a', encoding='utf-8') as f:
            f.write(number)
            f.write(text)
            f.write(answers.text + '\n')


    # # 退出时关闭浏览器
    # page.quit()


if __name__ == '__main__':
    print("第一次执行没有账号信息，会打开智慧树界面，登录自己账号")
    print("然后中断程序，再次运行一遍即可")
    if menu_url :
        run()
    elif url:
        kaoshi()
    else:
        print("请输入目录页的url或者考试页的url")
from asyncio import timeout
from traceback import print_tb

from DrissionPage import WebPage
import time

from numba.core.cgutils import if_zero

baseurl="https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList/doexamination/363131/5j9Ap1G9/yL91JWbw/1000009235/625"
url='https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList/dohomework/363131/wVnj2Y6M/eddQ9BJe/1000009235/625/0'

def run():
    # 1. 启动浏览器
    # DrissionPage 默认会打开一个浏览器窗口，方便调试
    # 结束时想自动关闭浏览器，可以设置 auto_close=True
    page = WebPage()

    # 2. 访问页面
    # page.get(baseurl)
    # page.get( url)

    tab = page.latest_tab
    # tab.wait.eles_loaded('.el-button el-button--primary is-plain')
    div = tab.eles('.subject_describe')

    for i in div:
        cards=i.afters('@@data-v-189f8b67=@@class=examPaper_subject mt20')
        shadow=i.child().child()
        text=shadow.shadow_root.children()
        for j in text:
            print(j.text)
        for k in cards[:5]:
            print(k.text)

    #
    # # 退出时关闭浏览器
    # page.quit()


if __name__ == '__main__':
    run()
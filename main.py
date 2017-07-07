import webbrowser
from application import app
import threading
import time
from urllib import request

port = 5000  # 端口号
index_url = 'http://127.0.0.1:%d' % port  # 首页地址


def open_browser():
    print('服务启动中...')
    while True:
        # 每秒钟检测一次
        time.sleep(1)
        try:
            request.urlopen(url=index_url)
            break
        except Exception as e:
            print(e)

    print('服务启动完成 !')
    # 服务启动完成后打开浏览器
    webbrowser.open(index_url)

threading.Thread(target=open_browser).start()
# 启动服务器
app.run(host="0.0.0.0", port=port)

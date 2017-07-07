import os
from application import app
from flask import request, render_template

import json
from PyInstaller.__main__ import run


# 首页
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# 编译
@app.route("/compile.do", methods=['POST'])
def compile():
    try:
        main_path = request.values.get('mainPath', '')
        name = request.values.get('name', '')
        is_single = request.values.get('isSingle', '0')
        is_console = request.values.get('isConsole', '0')
        icon = request.values.get('icon', '')
        package = request.values.get('package', '')
        add_data = request.values.get('addData', '')
        add_binary = request.values.get('addBinary', '')
        hidden_import = request.values.get('hiddenImport', '')
        additional_hooks_dir = request.values.get('additionalHooksDir', '')
        out_path = request.values.get('outPath', '')
        # version = request.values.get('version', '')

        # 打包参数
        opts = [main_path]
        if name:
            opts.append('-n')
            opts.append(name)
        if '1' == is_single:
            opts.append('-F')
        if '1' == is_console:
            opts.append('-c')
        if icon:
            opts.append('-i')
            opts.append(icon)
        if package:
            args = package.split('|')
            for data in args:
                opts.append('-p')
                opts.append(data)
        if add_data:
            args = add_data.split('|')
            for data in args:
                opts.append('--add-data')  # <SRC;DEST or SRC:DEST>
                opts.append(data)
        if add_binary:
            args = add_binary.split('|')
            for data in args:
                opts.append('--add-binary')  # <SRC;DEST or SRC:DEST>
                opts.append(data)
        if hidden_import:
            args = hidden_import.split('|')
            for data in args:
                opts.append('--hidden-import')
                opts.append(data)
        if additional_hooks_dir:
            args = additional_hooks_dir.split('|')
            for data in args:
                opts.append('--additional-hooks-dir')
                opts.append(data)
        if out_path:
            opts.append('--distpath')
            opts.append(os.path.join(out_path, 'output'))
            opts.append('--workpath')
            opts.append(os.path.join(out_path, 'temp'))
            opts.append('--specpath')
            opts.append(os.path.join(out_path, 'spec'))

        # 调用pyinstaller的编译打包方法
        run(opts)
        return json.dumps(obj={'code': 200, 'message': '&nbsp;&nbsp;打包成功!'}, ensure_ascii=False)
    except Exception as e:
        return json.dumps(obj={'code': 300, 'message': '打包失败！<br>失败信息：' + str(e)}, ensure_ascii=False)


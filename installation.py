# 导库
import os
import time
import datetime
import sys
import re
import json
import requests
# from alive_progress import alive_bar


# 做主函数
def main():
    packages_install = input('请输入您想要安装的Python包: ')
    print('您想要安装的Python包是: ', packages_install)
    check_packages(packages_install)
    install_packages(packages_install)


# 做检查包函数
def check_packages(packages_install):
    print("开始检查是否有安装该Python包")
    command_result = os.popen("pip list | findstr " + packages_install)
    # 测试变量类型
    # 这样子指令的结果没法判断
    if command_result == packages_install:
        print("在该台主机上已经安装了" + packages_install)
        sys.exit()
    else:
        print("开始启动安装程序" + "安装您想要的" + packages_install)
        print("------------------------------------------------------------------------------------------------------------------------------")
    #print(type(command_result))
    username = os.getlogin()
    with open("packages_log.txt", "w") as file:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                       #datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(username + " 于北京时间 " + current_time + " 安装了 " + packages_install)


# 做安装包函数
def install_packages(packages_install):
    # proxy_pool =
    # domain_pool = []
    # 定义镜像源 地址池子 Python数据类型:dictionary
    # 策略: 切换镜像源地址
    # mirrors_pool = {
    #     'tsinghua': {
    #         'domain': 'pypi.tuna.tsinghua.edu.cn',
    #         'tsinghua_link': 'https://pypi.tuna.tsinghua.edu.cn/simple'
    #     },
    #     'douban': {
    #         'domain': 'pypi.douban.com',
    #         'douban_link': 'http://pypi.douban.com/simple/'
    #     },
    #     'aliyun': {
    #         'domain': 'mirrors.aliyun.com',
    #         'aliyun_link': 'http://mirrors.aliyun.com/pypi/simple/'
    #     }
    #     # '': {
    #     #     'domain': ''
    #     #     '_link': ''
    #     # }
    # }

    # 备用字典2 根据使用需求进行切换
    mirrors_pool = {
        "pypi.tuna.tsinghua.edu.cn":{"https://pypi.tuna.tsinghua.edu.cn/simple"},"pypi.douban.com":{"http://pypi.douban.com/simple/"},"mirrors.aliyun.com":{"http://mirrors.aliyun.com/pypi/simple/"}
    }

    # convert_result = dict*(mirrors_pool)
    # mirrors_result = json.dumps(convert_result)
    # with open("mirrors_links.txt","w") as file2:
    #     file2.write(mirrors_result)
    #     file2.close()
    # 做一个条件判断的语句出来,如果读取字典当中的url_link访问失败,return error，切换成另外一个url_link
    #print(mirrors_pool)

    for value_result in mirrors_pool.values():
        print(value_result)
    for key_result in mirrors_pool.keys():
        print(key_result)


    final_result = []
        for
    install_command = os.system('pip install -i ' + packages_install +  + ' --trusted-host ' + )
    #做一个安装进度条的函数出来
    # 伪代码
    response = requests.get('')
    download_time = requests.get('content-length')
    for i in

main()




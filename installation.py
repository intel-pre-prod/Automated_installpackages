import os
import time
import datetime
import sys
import re
import json
import requests


def main():
    start = time.perf_counter()  # Start counter time
    packages_install = input('Plz enter the Python package you want to install: ')
    print('The Python package you want to install is: ', packages_install)
    check_packages(packages_install)
    install_packages(packages_install)
    end = time.perf_counter()  # End counter time
    runtime = end - start  # Running time =  End counter time - Start counter time
    counter_process(runtime)


def check_packages(packages_install):
    print("Start to check whether the Python package is installed")
    command_result = os.system("pip list" + " | findstr " + packages_install)
    if command_result == packages_install: # Not full completed function
        print(packages_install + " has been installed on this host")
        sys.exit()
    else:
        print("Start to setup " + packages_install + " you want to installed in this laptop")
        print("------------------------------------------------------------------------------------------------------------------------------")
    username = os.getlogin()
    with open("packages_log.txt", "w") as file:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(username + " downloaded the " + packages_install + " at Current time: " + current_time)


def install_packages(packages_install):
    # mirrors_pool Python data type:dictionary
    # You can change the Proxypool key and value by your own decision
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

    # backup dictionary: according to the requirement to change
    mirrors_pool = {"pypi.tuna.tsinghua.edu.cn": "https://pypi.tuna.tsinghua.edu.cn/simple",
                    "pypi.douban.com": "http://pypi.douban.com/simple/",
                    "mirrors.aliyun.com": "http://mirrors.aliyun.com/pypi/simple/"}


    with open("mirrors_links.txt","w") as file2:
        file2.write(str(mirrors_pool))
        file2.close()


    # if
    #     os.system('pip install -i ' + packages_install + mirrors_pool["pypi.tuna.tsinghua.edu.cn"] + ' --trusted-host ' )
    # elif
    #     os.system('pip install -i ' + packages_install + mirrors_pool["link1"] + ' --trusted-host ' )
    # elif
    #     os.system('pip install -i ' + packages_install + mirrors_pool["link1"] + ' --trusted-host ' )



def counter_process(runtime):
    scale = 100
    print("Start downloading the python packages".center(scale // 2, "-"))
    for i in range(scale + 1):
        conuter1 = ">" * i
        counter2 = "-" * (scale - i)
        counter3 = (i / scale) * 100
        print("\r{:^3.0f}%[{}>{}]{:.2f}s".format(counter3, conuter1, counter2, runtime), end="")
        time.sleep(0.1)

    print("\n" + "All the job is done,lucky so much".center(scale // 2, "-"))


main()




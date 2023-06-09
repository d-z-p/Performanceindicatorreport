# -*- coding: GB2312 -*-
import os
import os.path
import time
import glob

# 删除已有测试cmd脚本
path = "D:\\PyCharm\\monkeyTest-master\\"
for file in glob.glob(os.path.join(path, '*.cmd')):
    os.remove(file)

os.system("cls")  # os.system("cls")具有清屏功能
rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
#print(rt)
n = len(rt) - 2
print("当前已连接待测手机数为：" + str(n))
aw = input("是否要开始你的monkey测试，请输入(y or n): ")
run_time =time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

if aw == 'y':
    print("monkey测试即将开始....")
    #count = input("请输入你要进行的monkey测试次数: ")
    #testmodel = input("请输入你是要进行单次测试还是多次连续测试，请输入(1-代表单次测试，2-代表多次连续测试): ")
    ds = range(n)
    for i in range(n):
        nPos = rt[i + 1].index("\t")
        #print(nPos)
        dev = rt[i + 1][:nPos]
        #print(dev)
        promodel = os.popen("adb -s " + dev + ' shell cat /system/build.prop | find "ro.product.model="').readlines()  # 获取手机型号
        modelname = promodel[0]  # 从list中取出第一个值
        model = modelname[17:].strip('\r\n')
        proname = os.popen("adb -s " + dev + ' shell cat /system/build.prop | find "ro.product.brand="').readlines()  # 获取手机名称
        roname = proname[0]
        name = roname[17:].strip('\r\n')
        packagename = os.popen("adb -s " + dev + ' shell pm list packages | find "com.baidu.homework"').readlines() #获取package包名
        package = packagename[0]
        pk = package[8:].strip('\r\n')
        if pk == 'com.baidu.homework':
            """filedir = os.path.exists("D:\\PyCharm\\monkeyTest-master\\")
            if filedir:
                print("File Exist,go on testing!")
            else:
                os.mkdir("D:\\PyCharm\\monkeyTest-master\\")"""
            devicedir = os.path.exists("D:\\PyCharm\\monkeyTest-master\\" + name + '-' + model + '-' + dev)
            if devicedir:
                print("File Exist, go on testing!")
            else:
                os.mkdir("D:\\PyCharm\\monkeyTest-master\\" + name + '-' + model + '-' + dev)  # 按设备ID生成日志目录文件夹
            wl = open("D:\\PyCharm\\monkeyTest-master\\" + name + '-' + model + '-' + dev + '-logcat' + '.cmd', 'w')
            wl.write('adb -s ' + dev + ' logcat' + ' > D:\\PyCharm\\monkeyTest-master\\' + '"' + name + '-' + model + '-' + dev + '"' + '\\'+ run_time + '_logcat.txt\n' )
            #wl.write(' > D:\\PyCharm\\monkeyTest-master\\' + '"' + name + '-' + model + '-' + dev + '"' + '\\logcat.txt\n')
            wl.close()
            #if testmodel == '1':
            wd = open("D:\\PyCharm\\monkeyTest-master\\" + name + '-' + model + '-' + dev + '-device' + '.cmd', 'w')
            wd.write(
                'adb -s ' + dev + ' shell monkey -p com.quvideo.slideplus -s 200 --throttle 500 --ignore-crashes --ignore-timeouts --pct-touch 45 --pct-trackball 15 --pct-appswitch 10 --pct-syskeys 10 --pct-motion 20 -v -v 1000 ')  # 选择设备执行monkey
            wd.write('> D:\\PyCharm\\monkeyTest-master\\' + '"' + name + '-' + model + '-' + dev + '"' + '\\' + run_time + '_monkey.txt\n')
            wd.write('测试完成，请查看日志文件~')
            wd.close()
            """elif testmodel == '2':
                wd = open("D:\\PyCharm\\monkeyTest-master\\" + name + '-' + model + '-' + dev + '-device' + '.cmd', 'w')
                wd.write(':loop')
                wd.write('\nset /a num+=1')
                wd.write('\nif "%num%"=="4" goto end')
                wd.write(
                    '\nadb -s ' + dev + ' shell monkey -p com.quvideo.slideplus -s 200 --throttle 500 --ignore-crashes --ignore-timeouts --pct-touch 45 --pct-trackball 15 --pct-appswitch 10 --pct-syskeys 10 --pct-motion 20 -v -v 1000 ')  # 选择设备执行monkey
                wd.write('> D:\\PyCharm\\monkeyTest-master\\' + '"' + name + '-' + model + '-' + dev + '"' + '\\monkey.txt\n')
                wd.write('@echo 测试成功完成，请查看日志文件~')
                wd.write('\nadb -s ' + dev + ' shell am force-stop ' + pk)
                wd.write('\n@ping -n 15 127.1 >nul')
                wd.write('\ngoto loop')
                wd.write('\n:end')
                wd.close()"""
        else:
            print("待测手机" + name + '-' + model + "未安装小影记")

    # 执行上述生成的cmd脚本path='E:\\monkey_test\\'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) == True:
            if file.find('.cmd') > 0:
                os.system('start ' + os.path.join(path, '"' + file + '"'))  # dos命令中文件名如果有空格，需加上双引号
                time.sleep(1)
elif aw == 'n':
    print('用户主动放弃测试，测试结束！')
else:
    print("测试结束，输入非法，请重新输入y or n！")
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

try:
    import requests
except ImportError:
    pipmain(['install', 'requests'])

pipmain(['install', 'PySocks'])

try:
    import json
except ImportError:
    pipmain(['install', 'json'])

from utils import *

startfile = str(input("需要翻译的文件名(同一目录,带文件名后缀,例如.txt):"))
endfile = str(input("翻译后输出文件名(带文件名后缀,例如.txt):"))

insof = open(startfile, 'r', encoding='utf-8')
outof = open(endfile, 'w')

proxy = input("本地代理端口(为空则不使用代理):")
proxies = {
    'http': 'socks5://127.0.0.1:' + proxy,
    'https': 'socks5://127.0.0.1:' + proxy
}
sentence_num = int(input("一次翻译行数(数字):"))
lang_str = input("翻译语言(在zh,jp,en,fr,ru,ko,pt,it,es中选择至少2项,用逗号分隔,可重复,按顺序翻译):")
lang = lang_str.split(',')

translate_sentence = 0
translated_num = 0
while True:
    translate_sentence += 1
    t=0
    x=''
    while t<=sentence_num:
        x+=insof.readline()
        t+=1
    if not x:
        break
    x = translater(translate_sentence,translated_num,lang,proxy, proxies,x)
    x = translater(-1,-1,['zh'],proxy, proxies,x)
    print(x, file=outof)
print('翻译完成')
insof.close()
outof.close()
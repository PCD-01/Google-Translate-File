import requests
import json
import os
import time

def found_lang(lang):
    o = 0
    while o<len(lang):
        if (lang[o] == 'zh'):
            lang[o] = 'zh-CN'
        elif (lang[o] == 'jp'):
            lang[o] = 'ja'
        elif (lang[o] == 'en'):
            lang[o] = 'en'
        elif (lang[o] == 'ko'):
            lang[o] = 'ko'
        elif (lang[o] == 'fr'):
            lang[o] = 'fr'
        elif (lang[o] == 'es'):
            lang[o] = 'es'
        elif (lang[o] == 'ru'):
            lang[o] = 'ru'
        elif (lang[o] == 'pt'):
            lang[o] = 'pt'
        elif (lang[o] == 'it'):
            lang[o] = 'it'
        o += 1
    return lang

def translater(translate_sentence,translated_num,lang,proxy,proxies,sentence):
    lang = found_lang(lang)
    o = 0
    retn = ''
    while o<len(lang):
        if translate_sentence != -1 and translated_num != -1:
            print('第' + str(translate_sentence) + '段,正在翻译第' + str(translated_num + 1) + '次')
        else:
            print("正在翻译为中文")
        time.sleep(1)
        if (proxy):
            rqs = requests.post(
                'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl='+lang[o]+'&q=' + sentence,
                proxies=proxies
                )
        else:
            rqs = requests.post(
                'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl='+lang[o]+'&q=' + sentence
                )
        try:
            data = json.loads(rqs.text)
        except:
            print("已被谷歌判断滥用接口,请更换代理")
            os.system('pause')
            exit()
        if (data[0]):
            l = len(data[0])
            i = 0
            retn = ''
            while i < l:
                retn += str(data[0][i][0])
                i += 1
        translated_num += 1
        o += 1
        sentence = retn
    return sentence
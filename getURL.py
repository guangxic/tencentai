import time
import hashlib as hl
import requests
import json

APP_ID = '1106310666'
APP_KEY = 'pEwQBbXOVOz4ed89'
ENCODE_UTF8 = 'utf-8'
ENCODE_GBK = 'gbk'

if __name__ == '__main__':
    randomStr = '20e3408a79'
    text = '原告凌××为与被告张××民间借贷纠纷一案，于2009年2月4日向本院起诉。本院于同日受理后，依法由审判员孙涛独任审理，于2009年2月27日公开开庭进行了审理。原告凌××的委托代理人沈××到庭参加诉讼。被告张××经本院合法传唤，无正当理由拒不到庭。本案现已审理终结。'
    utf = text.encode(ENCODE_GBK)
    text = str(utf)[2:-1].replace('\\x', '%').upper()
    unix_time = int(time.time())

    strT = 'app_id=' + APP_ID + '&nonce_str=' + randomStr + '&text=' + text + '&time_stamp=' + str(unix_time)
    strS = strT + '&app_key=' + APP_KEY

    m = hl.md5()
    m.update(strS.encode('utf-8'))
    md5 = m.hexdigest().upper()

    request = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos?' + 'app_id=' + APP_ID + '&time_stamp=' \
              + str(unix_time) + '&nonce_str=' + randomStr + '&sign=' + md5 + '&text=' + text

    r = requests.get(request)
    data = json.loads(r.text)

    print(r.text)
    print(data["word"])

import time
import hashlib as hl
import requests
import json

APP_ID = '1106310666'
APP_KEY = 'pEwQBbXOVOz4ed89'
ENCODE_UTF8 = 'utf-8'
ENCODE_GBK = 'gbk'
RANDOM_STR = '20e3408a79'


def pos_url(sentence):
	encoded_sentence = sentence.encode(ENCODE_GBK)
	sentence = str(encoded_sentence)[2:-1].replace('\\x', '%').upper()
	unix_time = int(time.time())

	strT = 'app_id=' + APP_ID + '&nonce_str=' + RANDOM_STR + '&text=' + sentence \
	       + '&time_stamp=' + str(unix_time)
	strS = strT + '&app_key=' + APP_KEY

	m = hl.md5()
	m.update(strS.encode('utf-8'))
	md5 = m.hexdigest().upper()

	request = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos?' + \
	          'app_id=' + APP_ID + \
	          '&time_stamp=' + str(unix_time) + \
	          '&nonce_str=' + RANDOM_STR + \
	          '&sign=' + md5 + \
	          '&text=' + text
	return request


if __name__ == '__main__':
	text = u'原告凌××为与被告张××民间借贷纠纷一案，于2009年2月4日向本院起诉。本院于同日受理后，依法由审判员孙涛独任审理，于2009年2月27日公开开庭进行了审理。原告凌××的委托代理人沈××到庭参加诉讼。被告张××经本院合法传唤，无正当理由拒不到庭。本案现已审理终结。'

	url = pos_url(text)
	print(url)
	r = requests.get(pos_url(text))
	data = json.loads(r.text)

	# print(r.text)
	print(data)

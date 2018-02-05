import requests
import json
import time
import os

def tap(x,y):
	exec_str = 'adb shell input tap '+x+' '+y
	os.system(exec_str)

def select(key):
	if key == 0:
		tap('520','789')
	elif key == 1:
		tap('520','973')
	else:
		tap('520','1164')

def get_answer():
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5903',
	    'X-Requested-With':'com.sogou.activity.src',
	    'Referer':'http://nb.sa.sogou.com/'
	}
	response = requests.get("http://140.143.49.31/api/ans2?key=xigua&wdcallback=jQuery32101581228769459042_1516202689109&_=1516202689167", headers=headers)
	# print(response.text)

	text = response.text
	text = text.replace('jQuery32101581228769459042_1516202689109(','')
	text = text[:-1]

	answer = json.loads(text)
	answer = answer['result']
	# print(answer)
	res = json.loads(answer[-1])
	print(res['answers'])
	print(res['result'])
	last_answer = open('xg_answer.log',encoding='utf-8').read()
	if last_answer == res['result']:
		time.sleep(1)
	else:
		# 操作手机点击正确答案
		try:
			key = res['answers'].index(res['result'])
		except BaseException:
			key = 2
		select(key)
		# 保存最后一个答案
		open('xg_answer.log','w',encoding='utf-8').write(res['result'])

while True:
	get_answer()

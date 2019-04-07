#_*_ coding:UTF-8 _*_ 
# @author: zdl 
# 百度云语音合成Demo，实现对本地文本的语音合成。 
# 需安装好python-SDK，待合成文本不超过1024个字节 
# 合成成功返回audio.mp3 否则返回错误代码 
# 导入AipSpeech AipSpeech是语音识别的Python SDK客户端 
from aip import AipSpeech 
import os 

''' 你的APPID AK SK 参数在申请的百度云语音服务的控制台查看''' 
APP_ID = '15602205' 
API_KEY = 'ame658dpFXSmEGLhqGV89D8B' 
SECRET_KEY = 'MvGmfIiDsujTwNfX5XkpMHueodYwSuAL' 

# 新建一个AipSpeech 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY) 

# 将本地文件进行语音合成 
def tts(filename): 
	f = open(filename,'r') 
	command = f.read() 
	if len(command) != 0: 
		word = command 
	f.close() 
	result = client.synthesis(word,'zh',1, { 'vol': 5,'per':0, }) 
	# 合成正确返回audio.mp3，错误则返回dict 
	if not isinstance(result, dict): 
		with open('audio.mp3', 'wb') as f: 
			f.write(result) 
		f.close() 
		print ('tts successful') 

def tts2(command):  
	word = command 
	result = client.synthesis(word,'zh',1, { 'vol': 5,'per':0, }) 
	# 合成正确返回facename.mp3，错误则返回dict 
	if not isinstance(result, dict): 
		with open('/home/pi/Desktop/ASR/pangbai/%s.mp3' %(command), 'wb') as f: 
			f.write(result) 
		f.close() 
		print ('tts2 successful') 

def tts3(command):  
	word = command 
	result = client.synthesis(word,'zh',1, { 'vol': 5,'per':0, }) 
	# 合成正确返回facename.mp3，错误则返回dict 
	if not isinstance(result, dict): 
		with open('/home/pi/Desktop/ASR/tuling/tuling.mp3', 'wb') as f: 
			f.write(result) 
		f.close() 
		print ('tts3 successful') 

def tts4(command,i):  
	word = command 
	result = client.synthesis(word,'zh',1, { 'vol': 5,'per':0, }) 
	# 合成正确返回facename.mp3，错误则返回dict 
	if not isinstance(result, dict): 
		with open('/home/pi/Desktop/ASR/facename/%d.mp3' % (i), 'wb') as f: 
			f.write(result) 
		f.close() 
		print ('tts4 successful') 
# main 
#if __name__ == '__main__': 
#	i=1
#	name=[0,'123','234','liu',0,0]
#	while name[i]!=0:
#		tts4(name[i],i)
#		os.system("mplayer /home/pi/Desktop/ASR/facename/%d.mp3" % (i))
#		i=i+1

#tts2("请选择功能，否则执行上一步操作")	
#tts2("人机互动开始")
#tts2("人机互动结束")
#tts2("传感器展示结束")

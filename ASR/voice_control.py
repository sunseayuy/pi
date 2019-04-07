#encoding:utf-8
import serial  
import time 
import os
import re
import sys
sys.path.append('/home/pi/Desktop/FacialRecognitionProject')
sys.path.append('/home/pi/Desktop/chuangan/action')
sys.path.append('/home/pi/Desktop/chuangan')

import ASR
import recording
import firstface
import thirdface
import readDef
import tuling
import synthetic_voice

import hcsr04
import GP2D12
import hongwaibizhang

i=1
name=[0 for p in range(100)]
while(True):
	readDef.readDef("/home/pi/Desktop/chuangan/action/forward/zhanli.txt")
	#录音
	os.system("mplayer /home/pi/Desktop/ASR/pangbai/start.mp3")
	print("************************开始*************************")
	recording.record("test3.wav")
	print("语音识别:")
	#识别语音
	ASR.stt('test3.wav','demo.txt')
	print("txt文件生成")

	f = open("demo.txt") # 返回一个文件对象 
	statement=f.read()
	print(statement)
	f.close()

	pattern=r"人机互动"
	m1=re.search(pattern,statement)
	if m1!=None:
		print("1.人机互动")
		print("人机互动开始")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人机互动开始.mp3")
		while True:
				recording.record2(3,"tuling/tuling.wav")
				print("语音识别:")
				#识别语音
				ASR.stt('tuling/tuling.wav','/home/pi/Desktop/ASR/tuling/tuling.txt')
				print("txt文件生成")
				f = open("/home/pi/Desktop/ASR/tuling/tuling.txt","r+") # 返回一个文件对象 
				talk=f.read()
				print(talk)
				f.seek(0)
				f.truncate()
				f.close()
				pat=r"结束"
				m=re.search(pat,talk)
				if m!=None:
					break
				reply = tuling.tuling(talk)
				print(reply)
				synthetic_voice.tts3(reply)
				os.system("mplayer /home/pi/Desktop/ASR/tuling/tuling.mp3")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人机互动结束.mp3")

	pattern2=r"人脸检测"
	m2 = re.search(pattern2,statement)
	if m2!=None:
		print("2.人脸检测")
		print("******人脸检测开始******")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人脸检测开始.mp3")
		while True:
			j=firstface.first_face(i)
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问你的名字.mp3")
			print("******录制人脸名称******")
			recording.record("facename/facename.wav")
			print("******开始识别人脸名称***")
			#识别语音
			ASR.stt('facename/facename.wav','/home/pi/Desktop/ASR/facename/facename.txt')
			print("txt文件生成")
			f = open("/home/pi/Desktop/ASR/facename/facename.txt") # 人脸名字 
			facename=f.read()
			print(facename)
			f.close()
			name[i]=facename
			i=j
			#结束
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问是否结束.mp3")
			recording.record2(2,"finishthildface/finish.wav")
			print("语音识别:")
			#识别语音
			ASR.stt('finishthildface/finish.wav','/home/pi/Desktop/ASR/finishthildface/finish.txt')
			print("txt文件生成：")
			f2 = open("/home/pi/Desktop/ASR/finishthildface/finish.txt","r+") # 返回一个文件对象 
			finishpy=f2.read()
			print(finishpy)
			f2.seek(0)
			f2.truncate()
			f2.close()
			pattern=r"结束"
			m=re.search(pattern,finishpy)
			if m!=None:
				break
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人脸检测结束.mp3")
	#time.sleep(2)
	print(name)
	#name=[0,'liusiyuan','wang','zhou',0]
	
	pattern3=r"人脸识别"
	m3=re.search(pattern3,statement)
	if m3!=None:
		p=1
		print("3.人脸识别")
		print("******人脸识别开始******")
		os.system("python /home/pi/Desktop/FacialRecognitionProject/secondface.py")
		while name[p]!=0:
			synthetic_voice.tts4(name[p],p)
			p=p+1
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人脸识别开始.mp3")
		thirdface.findwho(name)
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/人脸识别结束.mp3")
	time.sleep(2)
	
	pattern4=r"前进"
	m4=re.search(pattern4,statement)
	if m4!=None:
		print("4.前进")
		print("******前进开始******")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/开始前进.mp3")
		while True:
			readDef.readDef("/home/pi/Desktop/chuangan/action/forward/qianjing.txt")
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问是否结束.mp3")
			recording.record2(2,"finishthildface/finish.wav")
			print("语音识别:")
			#识别语音
			ASR.stt('finishthildface/finish.wav','/home/pi/Desktop/ASR/finishthildface/finish.txt')
			print("txt文件生成：")
			f = open("/home/pi/Desktop/ASR/finishthildface/finish.txt","r+") # 返回一个文件对象 
			finishpy=f.read()
			print(finishpy)
			f.seek(0)
			f.truncate()
			pattern=r"结束"
			m=re.search(pattern,finishpy)
			if m!=None:
				break
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/前进结束.mp3")
		
	pattern5=r"向右侧移"
	m5=re.search(pattern5,statement)
	if m5!=None:
		print("5.向右侧移")
		print("******向右侧移******")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/向右侧移.mp3")
		while True:
			readDef.readDef("/home/pi/Desktop/chuangan/action/forward/ceyi.txt")
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问是否结束.mp3")
			recording.record2(2,"finishthildface/finish.wav")
			print("语音识别:")
			#识别语音
			ASR.stt('finishthildface/finish.wav','/home/pi/Desktop/ASR/finishthildface/finish.txt')
			print("txt文件生成：")
			f = open("/home/pi/Desktop/ASR/finishthildface/finish.txt","r+") # 返回一个文件对象 
			finishpy=f.read()
			print(finishpy)
			f.seek(0)
			f.truncate()
			pattern=r"结束"
			m=re.search(pattern,finishpy)
			if m!=None:
				break
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/侧移结束.mp3")
	
	pattern6=r"跳舞"
	m6=re.search(pattern6,statement)
	if m6!=None:
		print("6.跳舞")
		print("******跳舞******")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/开始跳舞.mp3")
		while True:
			readDef.readDef("/home/pi/Desktop/chuangan/action/forward/dance.txt")
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问是否结束.mp3")
			recording.record2(2,"finishthildface/finish.wav")
			print("语音识别:")
			#识别语音
			ASR.stt('finishthildface/finish.wav','/home/pi/Desktop/ASR/finishthildface/finish.txt')
			print("txt文件生成：")
			f = open("/home/pi/Desktop/ASR/finishthildface/finish.txt","r+") # 返回一个文件对象 
			finishpy=f.read()
			print(finishpy)
			f.seek(0)
			f.truncate()
			pattern=r"结束"
			m=re.search(pattern,finishpy)
			if m!=None:
				break
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/舞蹈结束.mp3")
	
	pattern7=r"传感器"
	m7=re.search(pattern7,statement)
	if m7!=None:
		print("7.传感器")
		print("******传感器******")
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/开始传感器展示.mp3")
		while True:
			readDef.readDef("/home/pi/Desktop/chuangan/action/forward/zhanli.txt")
			hcsr04long=hcsr04.hcsr04()
			print("超身波测距距离:%f" %hcsr04long)
			gp2d12long=GP2D12.GP2D12()
			print("红外测距距离%f" %gp2d12long)
			hong=hongwaibizhang.bizhang()
			if hong:
				print("1")
				readDef.readDef("/home/pi/Desktop/chuangan/action/forward/datou.txt")
			if hcsr04long>10 and hcsr04long<30:
				print("转向")
				readDef.readDef("/home/pi/Desktop/chuangan/action/forward/dunxia.txt")
			if gp2d12long>10 and gp2d12long<30:
				print("又转向")
				readDef.readDef("/home/pi/Desktop/chuangan/action/forward/right.txt")
			os.system("mplayer /home/pi/Desktop/ASR/pangbai/请问是否结束.mp3")
			recording.record2(2,"finishthildface/finish.wav")
			print("语音识别:")
			#识别语音
			ASR.stt('finishthildface/finish.wav','/home/pi/Desktop/ASR/finishthildface/finish.txt')
			print("txt文件生成：")
			f = open("/home/pi/Desktop/ASR/finishthildface/finish.txt","r+") # 返回一个文件对象 
			finishpy=f.read()
			print(finishpy)
			f.seek(0)
			f.truncate()
			pattern=r"结束"
			m=re.search(pattern,finishpy)
			if m!=None:
				break
		os.system("mplayer /home/pi/Desktop/ASR/pangbai/传感器展示结束.mp3")
		
	print("*****************************************************")

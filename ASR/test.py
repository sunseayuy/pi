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

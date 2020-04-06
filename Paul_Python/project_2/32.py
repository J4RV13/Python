#--------------------- 32 輕鬆完成文字自動轉語音系統 ---------------------
#pip install gTTS
from gtts import gTTS
#在windows下 lang不能使用zh，要用zh-tw
tts = gTTS(text = '全境封鎖2', lang = 'zh-tw')
tts.save('division2.mp3')
import webbrowser
webbrowser.open('division2.mp3')
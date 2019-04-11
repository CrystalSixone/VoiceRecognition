# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:13:02 2018

@author: Administrator
"""

import wave
from pyaudio import PyAudio,paInt16
from aip import AipSpeech
import serial
from time import sleep

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=1
TIME=2

def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*10:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('录音中...')
    save_wave_file('01.wav',my_buf)
    stream.close()

chunk=2014


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def recognize():
     # 定义常量
    APP_ID = '15038029'
    API_KEY = 'GnxYCBLhEBkI3ldnRNfax2Hp'
    SECRET_KEY = 'ofUCv6evemUNbGDQb5hEg0UXh0AlDl2r'

# 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.asr(get_file_content('01.wav'), 'wav', 16000, {
    'dev_pid':1536,
    })    
    if result['err_no'] == 0:
        print(result['result'][0])
    if result['err_no'] != 0:
        print('识别不出来，再来一次吧！')
    return result

if __name__ == '__main__': 
    serialPort="COM4"   #串口
    baudRate=115200       #波特率
    ser=serial.Serial(serialPort,baudRate,timeout=0.5)  
    print("参数设置：串口=%s 波特率=%d"%(serialPort,baudRate))#打开串口
    
    my_record()#录入语音
    print('识别语音中...')
    recognize()#识别语音
    result = recognize()
    if(result['result'][0] == '录音'):
        str = 'c'
        ser.write((str+'\n').encode())
        print('开始录音') 
        sleep(10)
        print('结束')
                #print(ser.readline())#可以接收中文
        ser.close()  
                #break
    elif(result['result'][0] == '放出来'):
        str = 'b'
        ser.write((str+'\n').encode())
        print('开始放音')
        sleep(10)
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    elif(result['result'][0] == '麦克风录音'):
        str = 'a'
        ser.write((str+'\n').encode())
        print('开始麦克风录音')
        sleep(10)
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    elif(result['result'][0] == '灯光模式一'):
        str = 'd'
        ser.write((str+'\n').encode())
        print('开始灯光模式一')
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    elif(result['result'][0] == '灯光模式二'):
        str = 'e'
        ser.write((str+'\n').encode())
        print('开始灯光模式二')
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    elif(result['result'][0] == '灯光模式三'):
        str = 'f'
        ser.write((str+'\n').encode())
        print('开始灯光模式三')
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    elif(result['result'][0] == '关灯'):
        str = 'g'
        ser.write((str+'\n').encode())
        print('开始关灯')
        print('结束')
                    #print(ser.readline())#可以接收中文
        ser.close()
    else:
        print('识别出错，再来一次吧！')
        ser.close() 
                #break
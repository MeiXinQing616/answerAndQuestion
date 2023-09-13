import nltk
import os

def isdown():
    download_path = "C:\TempWork\智能回答升级\source\word_tokenize data"
    # 检查数据是否已经下载
    if not os.path.exists(download_path+'\punkt'):
        nltk.download('punkt',download_dir=download_path)
    # 指定下载路径

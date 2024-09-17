# 导入requests模块，模拟发送请求
import requests
# 导入json
import json
# 导入re
import re
import subprocess
import os
import threading
import concurrent.futures
import csv
import sys

# 定义请求头
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    "cookies":"buvid3=697CB106-6F46-4629-D0A8-8CB68956D83F57842infoc; b_nut=1720313757; _uuid=F49AAD57-C2EA-3837-85B8-910C10FF16CBA758700infoc; buvid_fp=b675c5911b7c0258236771b64678327c; buvid4=27491F12-F800-BCF7-3EA8-05835DB6CF7A59719-024070700-%2BE1443FTBIc73XRxSZw8zQ%3D%3D; CURRENT_FNVAL=4048; rpdid=|(YYJ~lllYJ0J'u~k|JuJ)RY; header_theme_version=CLOSE; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bsource=search_google; bp_t_offset_3546734267468369=959893485207420928; iflogin_when_web_push=1; PVID=1; bp_t_offset_3546734328285550=960697391416082432; bp_t_offset_3493282128595843=960865178608467968; bp_t_offset_3546735911635654=960869907367460864; enable_web_push=DISABLE; home_feed_column=5; DedeUserID=1738828868; DedeUserID__ckMd5=e7f8ce7679d7a3b9; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ4MTUzMjksImlhdCI6MTcyNDU1NjA2OSwicGx0IjotMX0._fg-jSlWKBFk90qIGXkNA73QXVwLovdHt42Hn8ZCZoI; bili_ticket_expires=1724815269; SESSDATA=10e44bbe%2C1740120092%2C34de6%2A82CjAHQT9zhW8-4GYAvnhwHX3x0XSWoxNNILEM6ICwq2mJGDwZ-fNDOGB13_D6zd0Ta14SVkxhem9IcDZZX29oMXNXdE0tNmo0a1hjR2piWkotV0pDeHpCaWtNYlNSSWZoZmtxMTV0bFFlbWhTOTVvYWVZRmFXVXlfdWRuTkY5MmY2c3U5V2tLcHpRIIEC; bili_jct=ad0930f10eaded684649db03bad1dad6; sid=4li150co; CURRENT_QUALITY=80; browser_resolution=1872-1032; bp_t_offset_1738828868=970190192558211072; b_lsid=51109C10DF_19191E95312"
}

def read_cookie():
    with open("./cookies.txt", "r", encoding="utf-8") as f:
        cookies = f.read()
    return cookies

headers['cookies'] = read_cookie()

# 正则表达式，根据条件匹配出值
def my_match(text, pattern):
    match = re.search(pattern, text)
    print(match.group(1))
    print()
    return json.loads(match.group(1))

def resource_path(relative_path):
    """获取资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹，并存储路径到 _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def merge_video_audio(video_file, audio_file, output_file):
    # 构造 ffmpeg 的相对路径
    ffmpeg_path = resource_path("ffmpeg.exe")

    # 使用 subprocess 调用系统中的 ffmpeg 进行视频和音频的合并
    command = [
        ffmpeg_path,                # 相对路径的 ffmpeg
        '-i', video_file,          # 视频文件
        '-i', audio_file,          # 音频文件
        '-c:v', 'copy',            # 视频编解码器
        '-c:a', 'aac',             # 音频编解码器
        '-strict', 'experimental', # 允许实验性编解码器
        output_file                # 输出文件
    ]
    
    try:
        subprocess.run(command, check=True)
        print("视频和音频合并成功！")
    except subprocess.CalledProcessError as e:
        print(f"合并过程中出错: {e}")


 
def download_video(old_video_url, video_url, audio_url, video_name):
    headers.update({"Referer": old_video_url})
    
    session = requests.session()
    print("开始下载视频：%s" % video_name)
    video_content = session.get(video_url, headers=headers)
    print('%s视频大小：' % video_name, video_content.headers['content-length'])
    audio_content = session.get(audio_url, headers=headers)
    print('%s音频大小：' % video_name, audio_content.headers['content-length'])
    # 下载视频开始
    received_video = 0
    with open('%s_video.mp4' % video_name, 'ab') as output:
        while int(video_content.headers['content-length']) > received_video:
            headers['Range'] = 'bytes=' + str(received_video) + '-'
            response = session.get(video_url, headers=headers)
            output.write(response.content)
            received_video += len(response.content)
    # 下载视频结束
    # 下载音频开始
    audio_content = session.get(audio_url, headers=headers)
    received_audio = 0
    with open('%s_audio.mp4' % video_name, 'ab') as output:
        while int(audio_content.headers['content-length']) > received_audio:
            # 视频分片下载
            headers['Range'] = 'bytes=' + str(received_audio) + '-'
            response = session.get(audio_url, headers=headers)
            output.write(response.content)
            received_audio += len(response.content)
    # 下载音频结束
    merge_video_audio(f'{video_name}_video.mp4', f'{video_name}_audio.mp4', f'{video_name}.mp4')
    os.remove(f'{video_name}_video.mp4')
    os.remove(f'{video_name}_audio.mp4')
    return video_name
 
 
def main(url, index):
    # 发送请求，拿回数据
    res = requests.get(url, headers=headers)
    # 视频详情json
    playinfo = my_match(res.text, '__playinfo__=(.*?)</script><script>')
    # 视频内容json
    initial_state = my_match(res.text, r'__INITIAL_STATE__=(.*?);\(function\(\)')
    # 视频分多种格式，直接取分辨率最高的视频 1080p
    video_url = playinfo['data']['dash']['video'][0]['baseUrl']
    # 取出音频地址
    audio_url = playinfo['data']['dash']['audio'][0]['baseUrl']
    video_name = initial_state['videoData']['title'] + str(index)
    print('视频名字为：video_name')
    print('视频地址为：', video_url)
    print('音频地址为：', audio_url)
    download_video(url, video_url, audio_url, video_name)

def read_urls():
    urls = []
    with open("./urls.csv", "r", encoding="utf-8") as f:
        csvfile = csv.reader(f)
        for row in csvfile:
            if row:
                urls.append(row[0])
    return urls

if __name__ == "__main__":
    urls = read_urls()
    # 创建线程池，最多开启 12 个线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        # 提交任务到线程池a
        futures = [executor.submit(main, url, index) for index, url in enumerate(urls)]        
        # 等待所有任务完成
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # 获取结果，若有异常会被抛出
            except Exception as exc:
                print(f'任务抛出异常: {exc}')
    
            
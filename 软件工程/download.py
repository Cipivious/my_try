import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "open.bzpt.com",
    "Pragma": "no-cache",
    "Referer": "https://www.bzpt.com/",
    "Sec-CH-UA": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}


session = requests.session()
for i in range(1, 31):
    base_url = f'https://open.bzpt.com/download/1/GBT25000.1-2021.pdf?response-content-disposition=attachment;filename=GB%2FT%2025000.1-2021%20%E7%B3%BB%E7%BB%9F%E4%B8%8E%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%20%E7%B3%BB%E7%BB%9F%E4%B8%8E%E8%BD%AF%E4%BB%B6%E8%B4%A8%E9%87%8F%E8%A6%81%E6%B1%82%E5%92%8C%E8%AF%84%E4%BB%B7%EF%BC%88SQuaRE%EF%BC%89%20%E7%AC%AC1%E9%83%A8%E5%88%86%EF%BC%9ASQuaRE%E6%8C%87%E5%8D%97.pdf&OSSAccessKeyId=LTAI5tM75jx6rnFf6guEzKSg&Expires=1725339925&Signature=Ut1MUAAAc6OeNip1epBxsJRKtzA%3D'
    response = session.get(base_url, headers=headers)
    print(f"第{i}个返回的结果是", response)
    if response.status_code == 200:
        with open(f"./软件需求规约/标准{i}.pdf", "wb") as f:  # 注意使用 "wb" 模式
            f.write(response.content)
            
            
            
https://open.bzpt.com/download/1/GBT25000.1-2021.pdf?response-content-disposition=attachment&OSSAccessKeyId=LTAI5tM75jx6rnFf6guEzKSg&Expires=1725339925&Signature=Ut1MUAAAc6OeNip1epBxsJRKtzA%3D
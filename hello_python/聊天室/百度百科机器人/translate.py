import requests


def translate_to_english(text):
    url = "https://libretranslate.com/translate"
    headers = {"Content-Type": "application/json"}
    data = {
        "q": text,
        "source": "auto",  # zh 表示中文
        "target": "en",  # en 表示英语
        "format": "text",
        "alternatives": 3,
        "api_key": "",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["translatedText"]
    else:
        print(f"Error: Unable to translate. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    # 获取用户输入的中文文本
    chinese_text = input("请输入要翻译成英文的中文文本: ")

    # 调用翻译函数并打印结果
    translated_text = translate_to_english(chinese_text)
    if translated_text:
        print(f"翻译后的英文: {translated_text}")

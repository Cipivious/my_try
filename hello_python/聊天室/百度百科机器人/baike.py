import requests
from bs4 import BeautifulSoup
import re


def get_url(key):
    encoded_key = requests.utils.quote(key)
    return f"https://baike.baidu.com/item/{encoded_key}?fromModule=lemma_search-box"


def get_html(key):
    url = get_url(key)
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(
            f"Error: Unable to retrieve the page. Status code: {response.status_code}"
        )
        return None


def clean_text(text):
    # 移除方括号和其中的内容，处理引用编号
    text = re.sub(r"\[\d+\]", "", text)
    # 替换多个换行符、空格或制表符为一个空格
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_text_from_xpath(html):
    soup = BeautifulSoup(html, "html.parser")

    main_wrapper = soup.select_one(
        "#J-lemma-main-wrapper > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div:nth-of-type(2)"
    )

    if main_wrapper:
        raw_text = main_wrapper.get_text(separator="\n").strip()
        cleaned_text = clean_text(raw_text)
        return cleaned_text
    else:
        print("Error: Could not find the specified element.")
        return None


def get_key(key):
    html = get_html(key)

    if html:
        content = get_text_from_xpath(html)
        if content:
            print(content)


if __name__ == "__main__":
    get_key("上海")

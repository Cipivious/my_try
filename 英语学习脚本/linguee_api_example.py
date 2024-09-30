from linguee_api import Linguee

# 创建 Linguee API 客户端
linguee_client = Linguee()

# 翻译英文单词 'right' 到中文
results = linguee_client.translate('right', src='en', dst='zh')

# 打印翻译结果
if 'translations' in results and len(results['translations']) > 0:
    translation = results['translations'][0]['text']
    print(f"英文 'right' 的中文翻译是: {translation}")

# 打印相关例句
if 'examples' in results and len(results['examples']) > 0:
    print("\n相关例句:")
    for example in results['examples']:
        print(f"英文例句: {example['src']}")
        print(f"中文翻译: {example['dst']}\n")

import requests

api_root = "https://linguee-api.fly.dev/api/v2"  
resp = requests.get(f"{api_root}/external_sources", params={"query": "right", "src": "en", "dst": "zh"})
for index, source in enumerate(resp.json()):
    if(index >= 5):
        break
    print(f"{source['src']} \n\n {source['dst']} \n\n ************************************************************ \n")
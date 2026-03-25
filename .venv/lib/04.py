import requests
name = "周杰伦"
url = f"https://www.sogou.com/web?query={name}"

headers = {
       "User-Agent":   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}
re= requests.post(url, headers=headers)
print(re.text)


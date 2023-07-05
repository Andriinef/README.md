def det_html(url, headers, *, proxy=None):
    if isinstance(proxy, str):
        print(f"proxy: {proxy}, {url}: {headers}")
    elif proxy is None:
        print(f"proxy: None, {url}: {headers}")


url = "http://google.com"
headers = "text"

det_html(url, headers, proxy="qwe")

def add_https_prefix(url):
        if url.startswith("https://") or url.startswith("http://"):
            return url
        elif url.startswith("//"):
            url = "https:" + url
        elif not url.startswith("https://") and not url.startswith("http://"):
            url = "https://" + url  
        return url
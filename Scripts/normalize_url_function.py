def normalize_url(url):
    cutted_url = str(url[:7])
    if cutted_url == 'https:/':
        return url
    elif cutted_url == 'http://':
        url = url[6:]
        return 'https:/' + url
    else:
        return 'https://' + url


print(normalize_url('https://ya.ru'))  # 'https://ya.ru'
print(normalize_url('google.com'))  # 'https://google.com'
print(normalize_url('http://ai.fi'))  # 'https://ai.fi'

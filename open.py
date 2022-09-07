import webbrowser

def open_chrome():
    n = raw_input('Enter name:')
    base = "www.google.com/search?q="+n+" "
    browser = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    urls = ["profession", "dateofbirth", "nationality", "networth", "height", "religion", "parents", "instagram", "linkedin", "facebook", "twitter","Wife"]
    webbrowser.get(browser)
    for url in urls:
        webbrowser.open(base + url)

open_chrome()
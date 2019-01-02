import webbrowser

# Youtube search site
youtube_url = 'https://www.youtube.com/results?search_query= '

# input is called to serach for what you type in.
search  = input('type in a video name: ')

# Default browser will open.
webbrowser.open(youtube_url + search)

'''if you want to use specific browser like chrome, take out the hash. This path will only work for windows.
i will add for mac and linux later.'''
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#webbrowser.get(chrome_path).open_new_tab(url + url1)

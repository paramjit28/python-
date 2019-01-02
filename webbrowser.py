import webbrowser

# site you want to browser
url = 'https://www.google.com/search?source=hp&ei=jTYsXLy4GYuksAWznpCYDA&q= '

# type in what you want to serach for in.
url1 = input('type to search in google: ')
# browser will open your default browser to open the site.

webbrowser.open(url + url1)

'''if you want to use specific browser like chrome, take out the hash. This path will only work for windows.
i will add for mac and linux later.'''
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#webbrowser.get(chrome_path).open_new_tab(url + url1)

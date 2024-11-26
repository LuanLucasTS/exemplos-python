import pyshorteners

url = 'https://www.instagram.com/luanlucasts/'

s = pyshorteners.Shortener()

shorturl = s.tinyurl.short(url)

print(shorturl)

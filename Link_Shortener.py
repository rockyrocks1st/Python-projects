
import pyshorteners

url = input("Enter the url you want to shorten: ")

s = pyshorteners.Shortener()

print(s.tinyurl.short(url))
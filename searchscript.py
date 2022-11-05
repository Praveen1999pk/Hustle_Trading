import requests
import json


def search(jkey):
	url="https://shoonyatrade.finvasia.com/NorenWClientTP/SearchScrip"
	res=requests.post(url,data='jData={"uid":"FA76210","stext":"TATAMOTORS","exch":"NSE"}&jKey='+jkey)
	print(res.text)

search("9f8c4cca5c9992405902f7daa19cb6cf669fd604e7aa208f088fd76508f897c4")
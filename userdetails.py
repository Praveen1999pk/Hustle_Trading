import requests
import json


def user_details(jkey):
	url="https://shoonyatrade.finvasia.com/NorenWClientTP/UserDetails"
	res=requests.post(url,data='jData={"uid": "FA76210"}&jKey='+jkey)
	print(res.text)
	return res.text


def get_actid(jkey):
	res=json.loads(user_details(jkey))
	print(res["actid"])
	return res["actid"]


get_actid("b4a3f641742b042f0215e1bce190461b8e59e0601645e82877e6ff4a98b12651")
import requests
import hashlib
from pyotp import *
#'jData={"apkversion": "1.0.0", "uid":"FA76210", "pwd": "'+str(hashed_password("Trader@12345"))+', "factor2":"31-08-2017", "imei": "abc1234", "source": "API"}'


def get_2factor(pin):
	totp = TOTP(pin).now()
	print(totp)
	return (totp)


def sha_hashed(string):
	result = hashlib.sha256(string.encode())
	return result.hexdigest()

def login_session():
	url="https://shoonyatrade.finvasia.com/NorenWClientTP/QuickAuth"
	res=requests.post(url,data="jData={ \"apkversion\": \"1.0.0\", \"uid\": \"FA76210\", \"pwd\": \""+str(sha_hashed("Trader@12345"))+"\", \"factor2\":\""+get_2factor("T6SWQFTH465H34432YQSQF6LV55UC6I2")+"\", \"imei\": \"abc1234\", \"source\": \"API\",\"vc\":\"FA76210_U\",\"appkey\":\""+str(sha_hashed("FA76210|2314918f1e343e533c7c98aed4a96b93"))+"\"}")
	print((res.text)["susertoken"])

login_session()
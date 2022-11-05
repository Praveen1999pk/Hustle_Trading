import requests




def place_ord(jkey):
	url="https://shoonyatrade.finvasia.com/NorenWClientTP/PlaceOrder"
	res=requests.post(url,
		data="jData={\"uid\":\"FA76210\",\"actid\":\"FA76210\",\"exch\":\"NSE\",\"tsym\":\"BANKNIFTY\",\"qty\":\"1\",\"prc\":\"11.19\",\"trgprc\":\"\",\"dscqty\":\"\",\"prd\":\"I\",\"exchange\":\"BANKNIFTY 10NOV22 39000 PE\",\"trantype\":\"B\",\"prctyp\":\"SL-LMT\",\"ret\":\"DAY\",\"remarks\":\"dsf\",\"ordersource\":\"sdg\",\"bpprc\":\"dfg\",\"blprc\":\"fdg\",\"trailprc\":\"fdg\",\"amo\":\"dfg\",\"tsym2\":\"fdg\",\"trantype2\":\"fdg\",\"qty2\":\"dfg\",\"prc2\":\"fdg\",\"tsym3\":\"fdg\",\"trantype3\":\"dfg\",\"qty3\":\"fdg\",\"prc3\":\"fdg\"}"+"&"+"jKey="+str(jkey)

		)
	print(res.text)


place_ord("56629053de8665f79300b86f1cb82636bef5ce36cd6402918c7b0e29e84e1869")
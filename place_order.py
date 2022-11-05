




def place_ord(jkey):
	url="https://shoonyatrade.finvasia.com/NorenWClientTP/PlaceOrder"
	res=requests.post(url,
		data="jData={\"uid\":\"\",\"actid\":\"\",\"exch\":\"\",\"tsym\":\"\",\"qty\":\"\",\"prc\":\"\",\"trgprc\":\"\",\"dscqty\":\"\",\"prd\":\"\",\"exchange\":\"\",\"trantype\":\"\",\"prctyp\":\"\",\"ret\":\"\",\"remarks\":\"\",\"ordersource\"\"\",\"bpprc\":\"\",\"blprc\":\"\",\"trailprc\":\"\",\"amo\":\"\",\"tsym2\":\"\",\"trantype2\":\"\",\"qty2\":\"\",\"prc2\":\"\",\"tsym3\":\"\",\"trantype3\":\"\",\"qty3\":\"\",\"prc3\":\"\"}"
		+"&"+"jKey="+str(jkey)

		)
	print(res.text)



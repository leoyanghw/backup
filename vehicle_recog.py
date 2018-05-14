#!/usr/bin/python
import TencentYoutuyun
import json
import sys,os
appid='10130422'
secret_id = 'AKID7CD6rYXXoyyoU3fpEVcKyOjuBTuI8qzx'
secret_key = 'ymZI856HIXgfT9e1pcImBSYo0Uq482qU'
userid= '345393041'

end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT       


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
f=open('result.txt','wb+')
os.chdir("../功能车牌图像数据库")


for i in range(0,50):
	ret = youtu.carclassify('http://www.buttoncar.com/wp-content/uploads/2018/04/WechatIMG276.jpeg',1)
	jsret = json.dumps(ret,ensure_ascii=False,encoding='utf-8',indent=2)
	#print jsret.encode('raw_unicode_escape').decode('utf8')
	f.write(jsret.encode('raw_unicode_escape').decode('utf8').encode('utf8'))
f.close()

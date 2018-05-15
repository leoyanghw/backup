#!/usr/bin/python
import TencentYoutuyun
import json
import sys,os
import cv2
# -*- coding: utf-8 -*-
appid='10130422'
secret_id = 'AKID7CD6rYXXoyyoU3fpEVcKyOjuBTuI8qzx'
secret_key = 'ymZI856HIXgfT9e1pcImBSYo0Uq482qU'
userid= '345393041'

end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT       


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
path="../lp_dataset"

list_f=open('log_warning').readlines()


log_err=open('recheck_vr_log_err','wb+')
log_warning=open('recheck_vr_log_warning','wb+')

#for i in range(0,20):
for i in range(0,len(list_f)):
	list_f[i]=list_f[i].strip("\n")
	ret = youtu.carclassify(list_f[i],0)
	print(list_f[i])
	filename_start=list_f[i].rfind("/")+1
	filename="./output_json/"+list_f[i][filename_start:]+".json"
#	filename="./output_json/"+str(i)+".json"
#	print(filename)
	f=open(filename,'wb+')
	jsret = json.dumps(ret,ensure_ascii=False,encoding='utf-8',indent=2)
	#print jsret.encode('raw_unicode_escape').decode('utf8')
	f.write(jsret.encode('raw_unicode_escape').decode('utf8').encode('utf8'))
#	f.write("\n")
	f.close()
	if(ret['errorcode']!=0):
		log_err.write(list_f[i]+"\n")
		continue
	if(len(ret['tags'])==0):
		log_warning.write(list_f[i]+"\n")
		continue
	y=int(ret['car_coord']['x'])
	x=int(ret['car_coord']['y'])
	h=int(ret['car_coord']['height'])
	w=int(ret['car_coord']['width'])
	color=ret['tags'][0]['color']
	image=cv2.imread(list_f[i])
	x2=x+h
	y2=y+w
	crop=image[x:x2,y:y2]
	filename="./jpg_cropped/"+list_f[i][filename_start:]+".bmp"
	cv2.imwrite(filename,crop)


#f.close()

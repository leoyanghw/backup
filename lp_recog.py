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

def file_list (path,f,list_f):
	parents = os.listdir(path)
	for parent in parents:
		child = os.path.join(path,parent)
		if os.path.isdir(child):
			file_list(child,f,list_f)
		else:
			list_f.append(child)
			f.write(child)
			f.write("\n")

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
path="./jpg_cropped"

f=open('lp_file_list.txt','wb+')
list_f=[]
file_list(path,f,list_f)
f.close()
print(len(list_f))

plate_number=open("plate_number","wb+")

log_err=open('lp_log_err','wb+')
log_warning=open('lp_log_warning','wb+')

#for i in range(0,2):
for i in range(0,len(list_f)):
	ret = youtu.plateocr(list_f[i],0)
	print(list_f[i])
	filename_start=list_f[i].rfind("/")+1
	filename="./lp_output_json/"+list_f[i][filename_start:]+".json"
	fname=list_f[i][filename_start:]
	fname=fname.strip("\.bmp")
#	print(filename)
	f=open(filename,'wb+')
	jsret = json.dumps(ret,ensure_ascii=False,encoding='utf-8',indent=2)
	#print jsret.encode('raw_unicode_escape').decode('utf8')
	f.write(jsret.encode('raw_unicode_escape').decode('utf8').encode('utf8'))
#	f.write("\n")
	f.close()
	if(ret['errorcode']!=0):
		log_err.write("[ERROR]:"+list_f[i]+"\n")
		continue
	if(len(ret['items'])==0):
		log_warning.write(list_f[i]+"\n")
		continue
	y=int(ret['items'][0]['itemcoord']['x'])
	x=int(ret['items'][0]['itemcoord']['y'])
	h=int(ret['items'][0]['itemcoord']['height'])
	w=int(ret['items'][0]['itemcoord']['width'])
	plate=ret['items'][0]['itemstring']
	plate_number.write(fname+','+plate.encode('raw_unicode_escape').decode('utf8').encode('utf8')+'\n')
	image=cv2.imread(list_f[i])
	x2=x+h
	y2=y+w
	crop=image[x:x2,y:y2]
	filename="./lp_cropped/"+list_f[i][filename_start:]+".bmp"
	cv2.imwrite(filename,crop)


#f.close()

#!/usr/bin/python
import TencentYoutuyun
import json
import sys,os
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
path="../lp_dataset"

f=open('file_list.txt','wb+')
list_f=[]
file_list(path,f,list_f)
f.close()
print(len(list_f))


#f=open('result.json','wb+')

#for i in range(0,1):
for i in range(0,len(list_f)):
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


#f.close()

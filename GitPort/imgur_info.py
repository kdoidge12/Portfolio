#Kristopher Doidge, krd14g, Project 4 Part 2 - 7/17/2016
from __future__ import print_function
import json
import requests
import re
import sys

if __name__ == "__main__":
	user = raw_input("Enter username: ")
	counter =0
	lst = []
	while counter<50:
		u_page = ("http://imgur.com/user/"+str(user)+"/index/newest/page/"+str(counter)+"/hit.json?scrolling")
		page = requests.get(u_page)
		if not page.text or not page:
			break
		j_s = page.json()
		j= json.dumps(j_s,skipkeys=True,sort_keys=True,indent =4)
		
		j_s = json.loads(j)
		#print(j)
		i = 0
		#for x in (j_s['data']['captions']['images']):
		#	print(x)
		
		
		while len(j_s['data']['captions']['data']) > i:
			Hash= j_s['data']['captions']['data'][i]['hash']
			Points= j_s['data']['captions']['data'][i]['points']
			Title = j_s['data']['captions']['data'][i]['title']
			Date = j_s['data']['captions']['data'][i]['datetime']
			lst.append([Points,Hash,Title,Date])
			i=i+1
		

		counter = counter +1
	if(counter == 0):
		print("No user/ Comment History")
	else:
		lst = sorted(lst)
		num = 1
		if len(lst) <6:
			derp = -1
			while derp*-1 <=len(lst):
				p = lst[derp][0]
				h = lst[derp][1]
				t = lst[derp][2]
				d = lst[derp][3]
				print(num,". ",h)
				print("Points: ",p)
				print("Title: ",t)
				print("Date: ",d)
				derp = derp -1
				num=num+1
		else:
			derp = -1
			while derp != -6:
				p = lst[derp][0]
				h = lst[derp][1]
				t = lst[derp][2]
				d = lst[derp][3]
				print(num,". ",h)
				print("Points: ",p)
				print("Title: ",t)
				print("Date: ",d)
				num = num+1
				derp = derp-1
	'''lst = sorted(lst)
	print(lst[-5:])'''
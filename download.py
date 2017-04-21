# This py file defines 2 functions, get_data() and delete_data().

import urllib3
import os

def get_data(url):
    
    filename = url.split('/')[-1]
    if os.path.isfile(filename):
    	print('File is already there.')

    http = urllib3.PoolManager()
    try:
    	r = http.request('GET',url)
    except UnboundLocalError:
    	print('The file url points to does not exist')
    	return False
    else:
	    with open(filename, 'wb') as out:
	    	out.write(r.data)
    r.release_conn()


def delete_data(filename):
	try:
		os.remove(filename)
	except FileNotFoundError:
		print('There is no such file.')



urlnamenode = "http://192.168.0.231:50070/jmx"
urldatanode = "http://192.168.0.231:50075/jmx"

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import socket
import json
import sys
import getopt
import time

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def load_jmx(url):
	# print url
	jmx = urlopen(url)
	data = str(jmx.read())
	xjson = json.loads(data)
	# beans = xjson.get('beans')
	beans = xjson['beans']
	return beans

def get_metricscategory_position(xbeans, lookupcategory):
	pointer = 0
	while pointer < len(xbeans):
		catname = xbeans[pointer]['name']
		if catname == lookupcategory:
			return pointer
		pointer += 1
	return 254

#print get_metricscategory_position(masterbeans, 'java.lang:type=Memory')
def get_vol_name(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=DataNodeInfo')
	nodedata = str(xbeans[pointer_id].get('VolumeInfo'))
	yjson = json.loads(nodedata)

	volinfo = []

	for key in yjson:
		volinfo.append({'{#VOL_NAME}': key})
	print json.dumps({'data': volinfo}, indent=4, separators=(',', ':'))

def usage():
	print sys.argv[0],"-h[elp] -n[namenode server name] -t[ime]"

def main():
	#print sys.argv
	# if len(sys.argv[1:]) < 1:
	# 	usage()
	# 	sys.exit(3)
	# try:
	# 	opts, args = getopt.getopt(sys.argv[1:], "htn:", ["help","time", "namenode="])
	# except getopt.GetoptError as err:
	# 	print str(err)
	# 	usage()
	# 	sys.exit(2)
	# for opt, arg in opts:
	# 	if opt in ("-h", "--help"):
	# 		usage()
	# 		sys.exit()
	# 	elif opt in ("-t"):
	# 		epoch_time = int(time.time())
	# 		print epoch_time
	# 		sys.exit(1)
	# 	elif opt in ("-n", "--namenode"):
	#server = "10.69.130.2"
	server = get_host_ip()
	epoch_time = int(time.time())
	beans = load_jmx("http://"+server+":50075/jmx")

	get_vol_name(beans, server, epoch_time)

#main(sys.argv)
if __name__ == "__main__":
    main()
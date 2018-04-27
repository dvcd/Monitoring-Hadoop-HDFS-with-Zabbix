import json
import sys
import getopt
import time

def get_metricscategory_position(xbeans, lookupcategory):
	pointer = 0
	while pointer < len(xbeans):
		catname = xbeans[pointer]['name']
		if catname == lookupcategory:
			return pointer
		pointer += 1
	return 254

def get_livenode_status(xnodename,xparaname):
	with open('/tmp/livennodedetails', 'r') as fp:
		data = fp.read()
		xjson = json.loads(data)
		result = xjson[xnodename][xparaname]
		return result




def usage():
	print sys.argv[0],"{#NODE_NAME},ParameterName"

def main():
	#print sys.argv
	if len(sys.argv[1:]) < 1:
		usage()
		sys.exit(3)
	else:
		# print sys.argv
		nodename = sys.argv[1]
		paraname = sys.argv[2]

	print get_livenode_status(nodename,paraname)

#main(sys.argv)
if __name__ == "__main__":
    main()
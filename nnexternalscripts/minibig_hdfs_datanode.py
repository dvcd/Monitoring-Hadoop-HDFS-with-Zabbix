urlnamenode = "http://192.168.0.231:50070/jmx"
urldatanode = "http://192.168.0.231:50075/jmx"

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import sys
import getopt
import time

def load_jmx(url):
	#print url
	jmx = urlopen(url)
	data = str(jmx.read())
	xjson = json.loads(data)
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

#0
def get_dn_memory(xbeans,hostsource,epoch_time):
	#Get the pointer id (just in case that the json order had changes)
	dn_memory_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Memory')
	print hostsource+" dn_memory_heap_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['HeapMemoryUsage'].get('committed'))
	print hostsource+" dn_memory_heap_usage_init "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['HeapMemoryUsage'].get('init'))
	print hostsource+" dn_memory_heap_usage_max "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['HeapMemoryUsage'].get('max'))
	print hostsource+" dn_memory_heap_usage_used "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['HeapMemoryUsage'].get('used'))
	print hostsource+" dn_memory_nonheap_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['NonHeapMemoryUsage'].get('committed'))
	print hostsource+" dn_memory_nonheap_usage_init "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['NonHeapMemoryUsage'].get('init'))
	print hostsource+" dn_memory_nonheap_usage_max "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['NonHeapMemoryUsage'].get('max'))
	print hostsource+" dn_memory_nonheap_usage_used "+str(epoch_time)+" "+str(xbeans[dn_memory_pointer_id]['NonHeapMemoryUsage'].get('used'))

#1
def get_dn_status(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=DataNodeStatus')
	print hostsource+" dn_status_State "+str(epoch_time)+" "+str(xbeans[pointer_id].get('State'))
	print hostsource+" dn_status_SecurityEnabled "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SecurityEnabled'))
	print hostsource+" dn_status_LastHATransitionTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LastHATransitionTime'))
	print hostsource+" dn_status_HostAndPort "+str(epoch_time)+" "+str(xbeans[pointer_id].get('HostAndPort'))
	
#2
def get_dn_rpc(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=RpcActivityForPort8020')
	print hostsource+" dn_rpc_SentBytes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SentBytes'))
	print hostsource+" dn_rpc_ReceivedBytes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReceivedBytes'))
	print hostsource+" dn_rpc_RpcQueueTimeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcQueueTimeNumOps'))
	print hostsource+" dn_rpc_RpcQueueTimeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcQueueTimeAvgTime'))
	print hostsource+" dn_rpc_RpcProcessingTimeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcProcessingTimeNumOps'))
	print hostsource+" dn_rpc_RpcProcessingTimeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcProcessingTimeAvgTime'))
	print hostsource+" dn_rpc_RpcAuthenticationFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthenticationFailures'))
	print hostsource+" dn_rpc_RpcAuthenticationSuccesses "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthenticationSuccesses'))
	print hostsource+" dn_rpc_RpcAuthorizationFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthorizationFailures'))
	print hostsource+" dn_rpc_RpcAuthorizationSuccesses "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthorizationSuccesses'))
	print hostsource+" dn_rpc_NumOpenCodnections "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumOpenCodnections'))
	print hostsource+" dn_rpc_CallQueueLength "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CallQueueLength'))
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=RpcDetailedActivityForPort8020')
	print hostsource+" dn_rpc_VersionRequestNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VersionRequestNumOps'))
	print hostsource+" dn_rpc_VersionRequestAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VersionRequestAvgTime'))
	print hostsource+" dn_rpc_RegisterDatanodeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RegisterDatanodeNumOps'))
	print hostsource+" dn_rpc_RegisterDatanodeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RegisterDatanodeAvgTime'))
	print hostsource+" dn_rpc_SendHeartbeatNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendHeartbeatNumOps'))
	print hostsource+" dn_rpc_SendHeartbeatAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendHeartbeatAvgTime'))
	print hostsource+" dn_rpc_BlockReportNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportNumOps'))
	print hostsource+" dn_rpc_BlockReportAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportAvgTime'))

#3
def get_dn_ugi(xbeans,hostsource,epoch_time):
	dn_ugi_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=UgiMetrics')
	print hostsource+" dn_ugi_LoginSuccessNumOps "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('LoginSuccessNumOps'))
	print hostsource+" dn_ugi_LoginSuccessAvgTime "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('LoginSuccessAvgTime'))
	print hostsource+" dn_ugi_LoginFailureNumOps "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('LoginFailureNumOps'))
	print hostsource+" dn_ugi_LoginFailureAvgTime "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('LoginFailureAvgTime'))
	print hostsource+" dn_ugi_tag.Hostname "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('tag.Hostname'))
	print hostsource+" dn_ugi_GetGroupsNumOps "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('GetGroupsNumOps'))
	print hostsource+" dn_ugi_GetGroupsAvgTime "+str(epoch_time)+" "+str(xbeans[dn_ugi_pointer_id].get('GetGroupsAvgTime'))

#4
def get_dn_GC_marksweep(xbeans,hostsource,epoch_time):
	dn_gcms_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=GarbageCollector,name=ConcurrentMarkSweep')
	try:
		print hostsource+" dn_gcms_CollectionCount "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id].get('CollectionCount'))
		print hostsource+" dn_gcms_CollectionTime "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id].get('CollectionTime'))
		print hostsource+" dn_gcms_lastgcinfo_GcThreadCount "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo'].get('GcThreadCount'))
		print hostsource+" dn_gcms_lastgcinfo_duration "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo'].get('duration'))
		print hostsource+" dn_gcms_lastgcinfo_endTime "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo'].get('endTime'))
		print hostsource+" dn_gcms_lastgcinfo_id "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo'].get('id'))
		print hostsource+" dn_gcms_lastgcinfo_startTime "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo'].get('startTime'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
		print hostsource+" dn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[dn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#5
def get_dn_bufferpool(xbeans,hostsource,epoch_time):
	dn_bufferpool_pointer_id = get_metricscategory_position(xbeans, 'java.nio:type=BufferPool,name=mapped')
	print hostsource+" dn_bufferpool_TotalCapacity "+str(epoch_time)+" "+str(xbeans[dn_bufferpool_pointer_id].get('TotalCapacity'))
	print hostsource+" dn_bufferpool_MemoryUsed "+str(epoch_time)+" "+str(xbeans[dn_bufferpool_pointer_id].get('MemoryUsed'))
	print hostsource+" dn_bufferpool_Count "+str(epoch_time)+" "+str(xbeans[dn_bufferpool_pointer_id].get('Count'))

#6
def get_dn_compilation(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Compilation')
	print hostsource+" dn_compilation_TotalCompilationTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalCompilationTime'))

#7
def get_dn_mp_eden(xbeans,hostsource,epoch_time):
	dn_mp_eden_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Eden Space')
	try:
		print hostsource+" dn_mp_eden_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['Usage'].get('committed'))
		print hostsource+" dn_mp_eden_usage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['Usage'].get('init'))
		print hostsource+" dn_mp_eden_usage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['Usage'].get('max'))
		print hostsource+" dn_mp_eden_usage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['Usage'].get('used'))
		print hostsource+" dn_mp_eden_peakusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" dn_mp_eden_peakusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['PeakUsage'].get('init'))
		print hostsource+" dn_mp_eden_peakusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['PeakUsage'].get('max'))
		print hostsource+" dn_mp_eden_peakusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['PeakUsage'].get('used'))
		print hostsource+" dn_mp_eden_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" dn_mp_eden_collectionusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" dn_mp_eden_collectionusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" dn_mp_eden_collectionusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_eden_pointer_id]['CollectionUsage'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#8
def get_dn_mp_perm(xbeans,hostsource,epoch_time):
	dn_mp_perm_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Eden Space')
	try:
		print hostsource+" dn_mp_perm_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['Usage'].get('committed'))
		print hostsource+" dn_mp_perm_usage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['Usage'].get('init'))
		print hostsource+" dn_mp_perm_usage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['Usage'].get('max'))
		print hostsource+" dn_mp_perm_usage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['Usage'].get('used'))
		print hostsource+" dn_mp_perm_peakusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" dn_mp_perm_peakusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['PeakUsage'].get('init'))
		print hostsource+" dn_mp_perm_peakusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['PeakUsage'].get('max'))
		print hostsource+" dn_mp_perm_peakusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['PeakUsage'].get('used'))
		print hostsource+" dn_mp_perm_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" dn_mp_perm_collectionusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" dn_mp_perm_collectionusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" dn_mp_perm_collectionusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_perm_pointer_id]['CollectionUsage'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#9
def get_dn_os(xbeans,hostsource,epoch_time):
	dn_os_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=OperatingSystem')
	print hostsource+" dn_os_OpenFileDescriptorCount "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('OpenFileDescriptorCount'))
	print hostsource+" dn_os_MaxFileDescriptorCount "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('MaxFileDescriptorCount'))
	print hostsource+" dn_os_CommittedVirtualMemorySize "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('CommittedVirtualMemorySize'))
	print hostsource+" dn_os_TotalSwapSpaceSize "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('TotalSwapSpaceSize'))
	print hostsource+" dn_os_FreeSwapSpaceSize "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('FreeSwapSpaceSize'))
	print hostsource+" dn_os_ProcessCpuTime "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('ProcessCpuTime'))
	print hostsource+" dn_os_FreePhysicalMemorySize "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('FreePhysicalMemorySize'))
	print hostsource+" dn_os_TotalPhysicalMemorySize "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('TotalPhysicalMemorySize'))
	print hostsource+" dn_os_SystemCpuLoad "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('SystemCpuLoad'))
	print hostsource+" dn_os_ProcessCpuLoad "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('ProcessCpuLoad'))
	print hostsource+" dn_os_SystemLoadAverage "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('SystemLoadAverage'))
	print hostsource+" dn_os_AvailableProcessors "+str(epoch_time)+" "+str(xbeans[dn_os_pointer_id].get('AvailableProcessors'))

#10
def get_dn_mp_survivor(xbeans,hostsource,epoch_time):
	dn_mp_survivor_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Survivor Space')
	try:
		print hostsource+" dn_mp_survivor_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['Usage'].get('committed'))
		print hostsource+" dn_mp_survivor_usage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['Usage'].get('init'))
		print hostsource+" dn_mp_survivor_usage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['Usage'].get('max'))
		print hostsource+" dn_mp_survivor_usage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['Usage'].get('used'))
		print hostsource+" dn_mp_survivor_peakusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" dn_mp_survivor_peakusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['PeakUsage'].get('init'))
		print hostsource+" dn_mp_survivor_peakusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['PeakUsage'].get('max'))
		print hostsource+" dn_mp_survivor_peakusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['PeakUsage'].get('used'))
		print hostsource+" dn_mp_survivor_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" dn_mp_survivor_collectionusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" dn_mp_survivor_collectionusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" dn_mp_survivor_collectionusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_survivor_pointer_id]['CollectionUsage'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#12
def get_dn_mp_oldgen(xbeans,hostsource,epoch_time):
	dn_mp_oldgen_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=CMS Old Gen')
	try:
		print hostsource+" dn_mp_oldgen_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['Usage'].get('committed'))
		print hostsource+" dn_mp_oldgen_usage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['Usage'].get('init'))
		print hostsource+" dn_mp_oldgen_usage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['Usage'].get('max'))
		print hostsource+" dn_mp_oldgen_usage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['Usage'].get('used'))
		print hostsource+" dn_mp_oldgen_peakusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" dn_mp_oldgen_peakusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['PeakUsage'].get('init'))
		print hostsource+" dn_mp_oldgen_peakusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['PeakUsage'].get('max'))
		print hostsource+" dn_mp_oldgen_peakusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['PeakUsage'].get('used'))
		print hostsource+" dn_mp_oldgen_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" dn_mp_oldgen_collectionusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" dn_mp_oldgen_collectionusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" dn_mp_oldgen_collectionusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_oldgen_pointer_id]['CollectionUsage'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#13
def get_dn_replication(xbeans,hostsource,epoch_time):
	dn_replication_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Replication')
	print hostsource+" dn_replication_sink.appliedOps "+str(epoch_time)+" "+str(xbeans[dn_replication_pointer_id].get('sink.appliedOps'))
	print hostsource+" dn_replication_sink.appliedBatches "+str(epoch_time)+" "+str(xbeans[dn_replication_pointer_id].get('sink.appliedBatches'))
	print hostsource+" dn_replication_sink.ageOfLastAppliedOp "+str(epoch_time)+" "+str(xbeans[dn_replication_pointer_id].get('sink.ageOfLastAppliedOp'))
#14
def get_dn_mp_codecache(xbeans,hostsource,epoch_time):
	dn_mp_codecache_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Code Cache')
	print hostsource+" dn_mp_codecache_usage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['Usage'].get('committed'))
	print hostsource+" dn_mp_codecache_usage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['Usage'].get('init'))
	print hostsource+" dn_mp_codecache_usage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['Usage'].get('max'))
	print hostsource+" dn_mp_codecache_usage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['Usage'].get('used'))
	print hostsource+" dn_mp_codecache_peakusage_committed "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" dn_mp_codecache_peakusage_init "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" dn_mp_codecache_peakusage_max "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" dn_mp_codecache_peakusage_used "+str(epoch_time)+" "+str(xbeans[dn_mp_codecache_pointer_id]['PeakUsage'].get('used'))

#15
def get_dn_jvm(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=JvmMetrics')
	try:
		print hostsource+" dn_jvm_MemNonHeapUsedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemNonHeapUsedM'))
		print hostsource+" dn_jvm_MemNonHeapCommittedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemNonHeapCommittedM'))
		print hostsource+" dn_jvm_MemHeapUsedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemHeapUsedM'))
		print hostsource+" dn_jvm_MemHeapCommittedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemHeapCommittedM'))
		print hostsource+" dn_jvm_MemMaxM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemMaxM'))
		print hostsource+" dn_jvm_GcCountParNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCountParNew'))
		print hostsource+" dn_jvm_GcTimeMillisParNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillisParNew'))
		print hostsource+" dn_jvm_GcCountConcurrentMarkSweep "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCountConcurrentMarkSweep'))
		print hostsource+" dn_jvm_GcTimeMillisConcurrentMarkSweep "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillisConcurrentMarkSweep'))
		print hostsource+" dn_jvm_GcCount "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCount'))
		print hostsource+" dn_jvm_GcTimeMillis "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillis'))
		print hostsource+" dn_jvm_ThreadsNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsNew'))
		print hostsource+" dn_jvm_ThreadsRunnable "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsRunnable'))
		print hostsource+" dn_jvm_ThreadsBlocked "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsBlocked'))
		print hostsource+" dn_jvm_ThreadsWaiting "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsWaiting'))
		print hostsource+" dn_jvm_ThreadsTimedWaiting "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsTimedWaiting'))
		print hostsource+" dn_jvm_ThreadsTerminated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsTerminated'))
		print hostsource+" dn_jvm_LogFatal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogFatal'))
		print hostsource+" dn_jvm_LogError "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogError'))
		print hostsource+" dn_jvm_LogWarn "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogWarn'))
		print hostsource+" dn_jvm_LogInfo "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogInfo'))
	except IndexError:
		x=0
	else:
		x=0

#17
def get_dn_fsnamesys(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=FSNamesystemState')
	print hostsource+" dn_fsnamesys_CapacityTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityTotal'))
	print hostsource+" dn_fsnamesys_CapacityUsed "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsed'))
	print hostsource+" dn_fsnamesys_CapacityRemaining "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityRemaining'))
	print hostsource+" dn_fsnamesys_TotalLoad "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalLoad'))
	print hostsource+" dn_fsnamesys_BlocksTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksTotal'))
	print hostsource+" dn_fsnamesys_MaxObjects "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MaxObjects'))
	print hostsource+" dn_fsnamesys_FilesTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesTotal'))
	print hostsource+" dn_fsnamesys_PendingReplicationBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PendingReplicationBlocks'))
	print hostsource+" dn_fsnamesys_UnderReplicatedBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('UnderReplicatedBlocks'))
	print hostsource+" dn_fsnamesys_ScheduledReplicationBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ScheduledReplicationBlocks'))
	print hostsource+" dn_fsnamesys_PendingDeletionBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PendingDeletionBlocks'))
	print hostsource+" dn_fsnamesys_BlockDeletionStartTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockDeletionStartTime'))
	print hostsource+" dn_fsnamesys_FSState "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FSState'))
	print hostsource+" dn_fsnamesys_NumLiveDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumLiveDataNodes'))
	print hostsource+" dn_fsnamesys_NumDeadDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDeadDataNodes'))
	print hostsource+" dn_fsnamesys_NumDecomLiveDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecomLiveDataNodes'))
	print hostsource+" dn_fsnamesys_NumDecomDeadDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecomDeadDataNodes'))
	print hostsource+" dn_fsnamesys_VolumeFailuresTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VolumeFailuresTotal'))
	print hostsource+" dn_fsnamesys_EstimatedCapacityLostTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('EstimatedCapacityLostTotal'))
	print hostsource+" dn_fsnamesys_NumDecommissioningDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecommissioningDataNodes'))
	print hostsource+" dn_fsnamesys_NumStaleDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumStaleDataNodes'))
	print hostsource+" dn_fsnamesys_NumStaleStorages "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumStaleStorages'))
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=FSNamesystem')
	print hostsource+" dn_fsnamesys_MissingBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MissingBlocks'))
	print hostsource+" dn_fsnamesys_MissingReplOneBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MissingReplOneBlocks'))
	print hostsource+" dn_fsnamesys_ExpiredHeartbeats "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ExpiredHeartbeats'))
	print hostsource+" dn_fsnamesys_TransactionsSinceLastCheckpoint "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsSinceLastCheckpoint'))
	print hostsource+" dn_fsnamesys_TransactionsSinceLastLogRoll "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsSinceLastLogRoll'))
	print hostsource+" dn_fsnamesys_LastCheckpointTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LastCheckpointTime'))
	print hostsource+" dn_fsnamesys_CapacityTotalGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityTotalGB'))
	print hostsource+" dn_fsnamesys_CapacityUsedGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsedGB'))
	print hostsource+" dn_fsnamesys_CapacityRemainingGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityRemainingGB'))
	print hostsource+" dn_fsnamesys_CapacityUsedNonDFS "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsedNonDFS'))

#11
def get_dn_retrycache(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=RetryCache.DataNodeRetryCache')
	print hostsource+" dn_retrycache_CacheHit "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheHit'))
	print hostsource+" dn_retrycache_CacheCleared "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheCleared'))
	print hostsource+" dn_retrycache_CacheUpdated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheUpdated'))

#19
def get_dn_threading(xbeans,hostsource,epoch_time):
	dn_treading_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Threading')
	print hostsource+" dn_threading_ThreadCount "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('ThreadCount'))
	print hostsource+" dn_threading_TotalStartedThreadCount "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('TotalStartedThreadCount'))
	print hostsource+" dn_threading_CurrentThreadCpuTime "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('CurrentThreadCpuTime'))
	print hostsource+" dn_threading_CurrentThreadUserTime "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('CurrentThreadUserTime'))
	print hostsource+" dn_threading_PeakThreadCount "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('PeakThreadCount'))
	print hostsource+" dn_threading_DaemonThreadCount "+str(epoch_time)+" "+str(xbeans[dn_treading_pointer_id].get('DaemonThreadCount'))


#def get_dn_region_tables_type(xbeans):
	#dn_regions_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Regions')
	#while xbeans[dn_regions_id]:
		#tabletype = xbeans[pointer]['name']
		#if catname == lookupcategory:
			#return pointer
			#pointer += 1
	#return 254

#21
#def get_dn_regions(xbeans):
	#dn_regions_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Regions'))
	#print hostsource+" dn_regions_

#22
def get_dn_wal(xbeans,hostsource,epoch_time):
	dn_wal_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=WAL')
	print hostsource+" dn_wal_rollRequest "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('rollRequest'))
	print hostsource+" dn_wal_SyncTime_num_ops "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('SyncTime_num_ops'))
	print hostsource+" dn_wal_SyncTime_min "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('SyncTime_min'))
	print hostsource+" dn_wal_SyncTime_max "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('SyncTime_max'))
	print hostsource+" dn_wal_AppendSize_num_ops "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendSize_num_ops'))
	print hostsource+" dn_wal_AppendSize_min "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendSize_min'))
	print hostsource+" dn_wal_AppendSize_max "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendSize_max'))
	print hostsource+" dn_wal_AppendTime_num_ops "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendTime_num_ops'))
	print hostsource+" dn_wal_AppendTime_min "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendTime_min'))
	print hostsource+" dn_wal_AppendTime_max "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('AppendTime_max'))
	print hostsource+" dn_wal_slowAppendCount "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('slowAppendCount'))
	print hostsource+" dn_wal_lowReplicaRollRequest "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('lowReplicaRollRequest'))
	print hostsource+" dn_wal_appendCount "+str(epoch_time)+" "+str(xbeans[dn_wal_pointer_id].get('appendCount'))

#23
def get_dn_gc_new(xbeans,hostsource,epoch_time):
	dn_gc_new_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=GarbageCollector,name=ParNew')
	try:
		print hostsource+" dn_gc_new_CollectionCount "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id].get('CollectionCount'))
		print hostsource+" dn_gc_new_CollectionTime "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id].get('CollectionTime'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
		print hostsource+" dn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[dn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))
	except IndexError:
		x=0
	else:
		x=0

#24
def get_dn_hbsys(xbeans,hostsource,epoch_time):
	dn_hbsys_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=MetricsSystem,sub=Stats')
	print hostsource+" dn_hbsys_NumActiveSources "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('NumActiveSources'))
	print hostsource+" dn_hbsys_NumAllSources "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('NumAllSources'))
	print hostsource+" dn_hbsys_NumActiveSinks "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('NumActiveSinks'))
	print hostsource+" dn_hbsys_NumAllSinks "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('NumAllSinks'))
	print hostsource+" dn_hbsys_SnapshotNumOps "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('SnapshotNumOps'))
	print hostsource+" dn_hbsys_SnapshotAvgTime "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('SnapshotAvgTime'))
	print hostsource+" dn_hbsys_PublishNumOps "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('PublishNumOps'))
	print hostsource+" dn_hbsys_PublishAvgTime "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('PublishAvgTime'))
	print hostsource+" dn_hbsys_DroppedPubAll "+str(epoch_time)+" "+str(xbeans[dn_hbsys_pointer_id].get('DroppedPubAll'))

#plus1
def get_dn_hostname(xbeans):
	dn_hostname_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=DataNodeInfo')
	hostname = str(xbeans[dn_hostname_pointer_id].get('DatanodeHostname'))
	return hostname



#5
def get_dn_activity(xbeans,hostsource,epoch_time):
	dn_hostname = get_dn_hostname(xbeans)
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=DataNode,name=DataNodeActivity-'+dn_hostname+'-9866')
	print hostsource+" dn_activity_BytesWritten "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BytesWritten'))
	print hostsource+" dn_activity_TotalWriteTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalWriteTime'))
	print hostsource+" dn_activity_BytesRead "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BytesRead'))
	print hostsource+" dn_activity_TotalReadTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalReadTime'))
	print hostsource+" dn_activity_BlocksWritten "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksWritten'))
	print hostsource+" dn_activity_BlocksRead "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksRead'))
	print hostsource+" dn_activity_BlocksReplicated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksReplicated'))
	print hostsource+" dn_activity_BlocksRemoved "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksRemoved'))
	print hostsource+" dn_activity_BlocksVerified "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksVerified'))
	print hostsource+" dn_activity_BlockVerificationFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockVerificationFailures'))
	print hostsource+" dn_activity_BlocksCached "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksCached'))
	print hostsource+" dn_activity_BlocksUncached "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksUncached'))
	print hostsource+" dn_activity_ReadsFromLocalClient "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReadsFromLocalClient'))
	print hostsource+" dn_activity_ReadsFromRemoteClient "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReadsFromRemoteClient'))
	print hostsource+" dn_activity_WritesFromLocalClient "+str(epoch_time)+" "+str(xbeans[pointer_id].get('WritesFromLocalClient'))
	print hostsource+" dn_activity_WritesFromRemoteClient "+str(epoch_time)+" "+str(xbeans[pointer_id].get('WritesFromRemoteClient'))
	print hostsource+" dn_activity_BlocksGetLocalPathInfo "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksGetLocalPathInfo'))
	print hostsource+" dn_activity_RemoteBytesRead "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RemoteBytesRead'))
	print hostsource+" dn_activity_RemoteBytesWritten "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RemoteBytesWritten'))
	print hostsource+" dn_activity_RamDiskBlocksWrite "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksWrite'))
	print hostsource+" dn_activity_RamDiskBlocksWriteFallback "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksWriteFallback'))
	print hostsource+" dn_activity_RamDiskBytesWrite "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBytesWrite'))
	print hostsource+" dn_activity_RamDiskBlocksReadHits "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksReadHits'))
	print hostsource+" dn_activity_RamDiskBlocksEvicted "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksEvicted'))
	print hostsource+" dn_activity_RamDiskBlocksEvictedWithoutRead "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksEvictedWithoutRead'))
	print hostsource+" dn_activity_RamDiskBlocksEvictionWindowMsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksEvictionWindowMsNumOps'))
	print hostsource+" dn_activity_RamDiskBlocksEvictionWindowMsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksEvictionWindowMsAvgTime'))
	print hostsource+" dn_activity_RamDiskBlocksLazyPersisted "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksLazyPersisted'))
	print hostsource+" dn_activity_RamDiskBlocksDeletedBeforeLazyPersisted "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksDeletedBeforeLazyPersisted'))
	print hostsource+" dn_activity_RamDiskBytesLazyPersisted "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBytesLazyPersisted'))
	print hostsource+" dn_activity_RamDiskBlocksLazyPersistWindowMsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksLazyPersistWindowMsNumOps'))
	print hostsource+" dn_activity_RamDiskBlocksLazyPersistWindowMsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RamDiskBlocksLazyPersistWindowMsAvgTime'))
	print hostsource+" dn_activity_FsyncCount "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FsyncCount'))
	print hostsource+" dn_activity_VolumeFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VolumeFailures'))
	print hostsource+" dn_activity_DatanodeNetworkErrors "+str(epoch_time)+" "+str(xbeans[pointer_id].get('DatanodeNetworkErrors'))
	print hostsource+" dn_activity_ReadBlockOpNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReadBlockOpNumOps'))
	print hostsource+" dn_activity_ReadBlockOpAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReadBlockOpAvgTime'))
	print hostsource+" dn_activity_WriteBlockOpNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('WriteBlockOpNumOps'))
	print hostsource+" dn_activity_WriteBlockOpAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('WriteBlockOpAvgTime'))
	print hostsource+" dn_activity_BlockChecksumOpNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockChecksumOpNumOps'))
	print hostsource+" dn_activity_BlockChecksumOpAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockChecksumOpAvgTime'))
	print hostsource+" dn_activity_CopyBlockOpNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CopyBlockOpNumOps'))
	print hostsource+" dn_activity_CopyBlockOpAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CopyBlockOpAvgTime'))
	print hostsource+" dn_activity_ReplaceBlockOpNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReplaceBlockOpNumOps'))
	print hostsource+" dn_activity_ReplaceBlockOpAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReplaceBlockOpAvgTime'))
	print hostsource+" dn_activity_HeartbeatsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('HeartbeatsNumOps'))
	print hostsource+" dn_activity_HeartbeatsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('HeartbeatsAvgTime'))
	print hostsource+" dn_activity_BlockReportsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportsNumOps'))
	print hostsource+" dn_activity_BlockReportsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportsAvgTime'))
	print hostsource+" dn_activity_IncrementalBlockReportsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('IncrementalBlockReportsNumOps'))
	print hostsource+" dn_activity_IncrementalBlockReportsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('IncrementalBlockReportsAvgTime'))
	print hostsource+" dn_activity_CacheReportsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheReportsNumOps'))
	print hostsource+" dn_activity_CacheReportsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheReportsAvgTime'))
	print hostsource+" dn_activity_PacketAckRoundTripTimeNanosNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PacketAckRoundTripTimeNanosNumOps'))
	print hostsource+" dn_activity_PacketAckRoundTripTimeNanosAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PacketAckRoundTripTimeNanosAvgTime'))
	print hostsource+" dn_activity_FlushNanosNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FlushNanosNumOps'))
	print hostsource+" dn_activity_FlushNanosAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FlushNanosAvgTime'))
	print hostsource+" dn_activity_FsyncNanosNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FsyncNanosNumOps'))
	print hostsource+" dn_activity_FsyncNanosAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FsyncNanosAvgTime'))
	print hostsource+" dn_activity_SendDataPacketBlockedOnNetworkNanosNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendDataPacketBlockedOnNetworkNanosNumOps'))
	print hostsource+" dn_activity_SendDataPacketBlockedOnNetworkNanosAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendDataPacketBlockedOnNetworkNanosAvgTime'))
	print hostsource+" dn_activity_SendDataPacketTransferNanosNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendDataPacketTransferNanosNumOps'))
	print hostsource+" dn_activity_SendDataPacketTransferNanosAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendDataPacketTransferNanosAvgTime'))

#27
def get_dn_ipc(xbeans,hostsource,epoch_time):
	dn_ipc_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=IPC,sub=IPC')
	print hostsource+" dn_ipc_queueSize "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('queueSize'))
	print hostsource+" dn_ipc_numCallsInGeneralQueue "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('numCallsInGeneralQueue'))
	print hostsource+" dn_ipc_numCallsInReplicationQueue "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('numCallsInReplicationQueue'))
	print hostsource+" dn_ipc_numCallsInPriorityQueue "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('numCallsInPriorityQueue'))
	print hostsource+" dn_ipc_numOpenCodnections "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('numOpenCodnections'))
	print hostsource+" dn_ipc_numActiveHandler "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('numActiveHandler'))
	print hostsource+" dn_ipc_TotalCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('TotalCallTime_num_ops'))
	print hostsource+" dn_ipc_TotalCallTime_min "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('TotalCallTime_min'))
	print hostsource+" dn_ipc_TotalCallTime_max "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('TotalCallTime_max'))
	print hostsource+" dn_ipc_TotalCallTime_mean "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('TotalCallTime_mean'))
	print hostsource+" dn_ipc_TotalCallTime_median "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('TotalCallTime_median'))
	print hostsource+" dn_ipc_exceptions.FailedSanityCheckException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.FailedSanityCheckException'))
	print hostsource+" dn_ipc_exceptions.RegionMovedException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.RegionMovedException'))
	print hostsource+" dn_ipc_QueueCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('QueueCallTime_num_ops'))
	print hostsource+" dn_ipc_QueueCallTime_min "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('QueueCallTime_min'))
	print hostsource+" dn_ipc_QueueCallTime_max "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('QueueCallTime_max'))
	print hostsource+" dn_ipc_QueueCallTime_mean "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('QueueCallTime_mean'))
	print hostsource+" dn_ipc_QueueCallTime_median "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('QueueCallTime_median'))
	print hostsource+" dn_ipc_authenticationFailures "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('authenticationFailures'))
	print hostsource+" dn_ipc_authorizationFailures "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('authorizationFailures'))
	print hostsource+" dn_ipc_exceptions "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions'))
	print hostsource+" dn_ipc_RequestSize_num_ops "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('RequestSize_num_ops'))
	print hostsource+" dn_ipc_RequestSize_min "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('RequestSize_min'))
	print hostsource+" dn_ipc_RequestSize_max "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('RequestSize_max'))
	print hostsource+" dn_ipc_RequestSize_mean "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('RequestSize_mean'))
	print hostsource+" dn_ipc_RequestSize_median "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('RequestSize_median'))
	print hostsource+" dn_ipc_ResponseSize_num_ops "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ResponseSize_num_ops'))
	print hostsource+" dn_ipc_ResponseSize_min "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ResponseSize_min'))
	print hostsource+" dn_ipc_ResponseSize_max "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ResponseSize_max'))
	print hostsource+" dn_ipc_ResponseSize_mean "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ResponseSize_mean'))
	print hostsource+" dn_ipc_ResponseSize_median "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ResponseSize_median'))
	print hostsource+" dn_ipc_authenticationSuccesses "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('authenticationSuccesses'))
	print hostsource+" dn_ipc_authorizationSuccesses "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('authorizationSuccesses'))
	print hostsource+" dn_ipc_ProcessCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ProcessCallTime_num_ops'))
	print hostsource+" dn_ipc_ProcessCallTime_min "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ProcessCallTime_min'))
	print hostsource+" dn_ipc_ProcessCallTime_max "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ProcessCallTime_max'))
	print hostsource+" dn_ipc_ProcessCallTime_mean "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ProcessCallTime_mean'))
	print hostsource+" dn_ipc_ProcessCallTime_median "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('ProcessCallTime_median'))
	print hostsource+" dn_ipc_exceptions.NotServingRegionException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.NotServingRegionException'))
	print hostsource+" dn_ipc_sentBytes "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('sentBytes'))
	print hostsource+" dn_ipc_exceptions.RegionTooBusyException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.RegionTooBusyException'))
	print hostsource+" dn_ipc_receivedBytes "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('receivedBytes'))
	print hostsource+" dn_ipc_exceptions.OutOfOrderScadnerNextException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.OutOfOrderScadnerNextException'))
	print hostsource+" dn_ipc_exceptions.UnknownScadnerException "+str(epoch_time)+" "+str(xbeans[dn_ipc_pointer_id].get('exceptions.UnknownScadnerException'))

def usage():
	print sys.argv[0],"-h[elp] -d[atanode server name] -t[ime]"

def main():
	#print sys.argv
	if len(sys.argv[1:]) < 1:
		usage()
		sys.exit(3)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "htd:", ["help","time", "datanode="])
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-t"):
			epoch_time = int(time.time())
			print epoch_time
			sys.exit(1)
		elif opt in ("-d", "--datanode"):
			server = arg
			epoch_time = int(time.time())
			beans = load_jmx("http://"+server+":50075/jmx")

	get_dn_memory(beans,server,epoch_time)
	#get_dn_status(beans,server,epoch_time)
	#get_dn_rpc(beans,server,epoch_time)
	#get_dn_ugi(beans,server,epoch_time)
	get_dn_GC_marksweep(beans,server,epoch_time)
	get_dn_bufferpool(beans,server,epoch_time)
	get_dn_activity(beans,server,epoch_time)
	get_dn_compilation(beans,server,epoch_time)
	get_dn_mp_eden(beans,server,epoch_time)
	get_dn_mp_perm(beans,server,epoch_time)
	get_dn_mp_survivor(beans,server,epoch_time)
	get_dn_mp_codecache(beans,server,epoch_time)
	get_dn_mp_oldgen(beans,server,epoch_time)
	get_dn_os(beans,server,epoch_time)
	#get_dn_retrycache(beans,server,epoch_time)
	get_dn_jvm(beans,server,epoch_time)
	get_dn_threading(beans,server,epoch_time)
	get_dn_gc_new(beans,server,epoch_time)
	#get_dn_fsnamesys(beans,server,epoch_time)

#main(sys.argv)
if __name__ == "__main__":
    main()

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
#  	 print url
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
def get_nn_memory(xbeans,hostsource,epoch_time):
	#Get the pointer id (just in case that the json order had changes)
	nn_memory_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Memory')
	print hostsource+" nn_memory_heap_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['HeapMemoryUsage'].get('committed'))
	print hostsource+" nn_memory_heap_usage_init "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['HeapMemoryUsage'].get('init'))
	print hostsource+" nn_memory_heap_usage_max "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['HeapMemoryUsage'].get('max'))
	print hostsource+" nn_memory_heap_usage_used "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['HeapMemoryUsage'].get('used'))
	print hostsource+" nn_memory_nonheap_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['NonHeapMemoryUsage'].get('committed'))
	print hostsource+" nn_memory_nonheap_usage_init "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['NonHeapMemoryUsage'].get('init'))
	print hostsource+" nn_memory_nonheap_usage_max "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['NonHeapMemoryUsage'].get('max'))
	print hostsource+" nn_memory_nonheap_usage_used "+str(epoch_time)+" "+str(xbeans[nn_memory_pointer_id]['NonHeapMemoryUsage'].get('used'))

#1
def get_nn_status(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=NameNodeStatus')
	print hostsource+" nn_status_State "+str(epoch_time)+" "+str(xbeans[pointer_id].get('State'))
	print hostsource+" nn_status_SecurityEnabled "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SecurityEnabled'))
	print hostsource+" nn_status_LastHATransitionTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LastHATransitionTime'))
	print hostsource+" nn_status_HostAndPort "+str(epoch_time)+" "+str(xbeans[pointer_id].get('HostAndPort'))
	
#2
def get_nn_rpc(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=RpcActivityForPort8020')
	print hostsource+" nn_rpc_SentBytes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SentBytes'))
	print hostsource+" nn_rpc_ReceivedBytes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ReceivedBytes'))
	print hostsource+" nn_rpc_RpcQueueTimeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcQueueTimeNumOps'))
	print hostsource+" nn_rpc_RpcQueueTimeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcQueueTimeAvgTime'))
	print hostsource+" nn_rpc_RpcProcessingTimeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcProcessingTimeNumOps'))
	print hostsource+" nn_rpc_RpcProcessingTimeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcProcessingTimeAvgTime'))
	print hostsource+" nn_rpc_RpcAuthenticationFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthenticationFailures'))
	print hostsource+" nn_rpc_RpcAuthenticationSuccesses "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthenticationSuccesses'))
	print hostsource+" nn_rpc_RpcAuthorizationFailures "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthorizationFailures'))
	print hostsource+" nn_rpc_RpcAuthorizationSuccesses "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RpcAuthorizationSuccesses'))
	print hostsource+" nn_rpc_NumOpenConnections "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumOpenConnections'))
	print hostsource+" nn_rpc_CallQueueLength "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CallQueueLength'))
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=RpcDetailedActivityForPort8020')
	print hostsource+" nn_rpc_VersionRequestNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VersionRequestNumOps'))
	print hostsource+" nn_rpc_VersionRequestAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VersionRequestAvgTime'))
	print hostsource+" nn_rpc_RegisterDatanodeNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RegisterDatanodeNumOps'))
	print hostsource+" nn_rpc_RegisterDatanodeAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RegisterDatanodeAvgTime'))
	print hostsource+" nn_rpc_SendHeartbeatNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendHeartbeatNumOps'))
	print hostsource+" nn_rpc_SendHeartbeatAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SendHeartbeatAvgTime'))
	print hostsource+" nn_rpc_BlockReportNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportNumOps'))
	print hostsource+" nn_rpc_BlockReportAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportAvgTime'))

#3
def get_nn_ugi(xbeans,hostsource,epoch_time):
	nn_ugi_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=UgiMetrics')
	print hostsource+" nn_ugi_LoginSuccessNumOps "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('LoginSuccessNumOps'))
	print hostsource+" nn_ugi_LoginSuccessAvgTime "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('LoginSuccessAvgTime'))
	print hostsource+" nn_ugi_LoginFailureNumOps "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('LoginFailureNumOps'))
	print hostsource+" nn_ugi_LoginFailureAvgTime "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('LoginFailureAvgTime'))
	print hostsource+" nn_ugi_tag.Hostname "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('tag.Hostname'))
	print hostsource+" nn_ugi_GetGroupsNumOps "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('GetGroupsNumOps'))
	print hostsource+" nn_ugi_GetGroupsAvgTime "+str(epoch_time)+" "+str(xbeans[nn_ugi_pointer_id].get('GetGroupsAvgTime'))

#4
def get_nn_GC_marksweep(xbeans,hostsource,epoch_time):
	nn_gcms_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=GarbageCollector,name=ConcurrentMarkSweep')
	print hostsource+" nn_gcms_CollectionCount "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id].get('CollectionCount'))
	print hostsource+" nn_gcms_CollectionTime "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id].get('CollectionTime'))
	try:
		print hostsource+" nn_gcms_lastgcinfo_GcThreadCount "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo'].get('GcThreadCount'))
		print hostsource+" nn_gcms_lastgcinfo_duration "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo'].get('duration'))
		print hostsource+" nn_gcms_lastgcinfo_endTime "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo'].get('endTime'))
		print hostsource+" nn_gcms_lastgcinfo_id "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo'].get('id'))
		print hostsource+" nn_gcms_lastgcinfo_startTime "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo'].get('startTime'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
		print hostsource+" nn_gcms_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[nn_gcms_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))
	except AttributeError:
		x=0

#5
def get_nn_bufferpool(xbeans,hostsource,epoch_time):
	nn_bufferpool_pointer_id = get_metricscategory_position(xbeans, 'java.nio:type=BufferPool,name=mapped')
	print hostsource+" nn_bufferpool_TotalCapacity "+str(epoch_time)+" "+str(xbeans[nn_bufferpool_pointer_id].get('TotalCapacity'))
	print hostsource+" nn_bufferpool_MemoryUsed "+str(epoch_time)+" "+str(xbeans[nn_bufferpool_pointer_id].get('MemoryUsed'))
	print hostsource+" nn_bufferpool_Count "+str(epoch_time)+" "+str(xbeans[nn_bufferpool_pointer_id].get('Count'))

#6
def get_nn_compilation(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Compilation')
	print hostsource+" nn_compilation_TotalCompilationTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalCompilationTime'))

#7
def get_nn_mp_eden(xbeans,hostsource,epoch_time):
	nn_mp_eden_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Eden Space')
	print hostsource+" nn_mp_eden_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['Usage'].get('committed'))
	print hostsource+" nn_mp_eden_usage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['Usage'].get('init'))
	print hostsource+" nn_mp_eden_usage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['Usage'].get('max'))
	print hostsource+" nn_mp_eden_usage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['Usage'].get('used'))
	print hostsource+" nn_mp_eden_peakusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" nn_mp_eden_peakusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" nn_mp_eden_peakusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" nn_mp_eden_peakusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['PeakUsage'].get('used'))
	print hostsource+" nn_mp_eden_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['CollectionUsage'].get('committed'))
	print hostsource+" nn_mp_eden_collectionusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['CollectionUsage'].get('init'))
	print hostsource+" nn_mp_eden_collectionusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['CollectionUsage'].get('max'))
	print hostsource+" nn_mp_eden_collectionusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_eden_pointer_id]['CollectionUsage'].get('used'))

#8
def get_nn_mp_perm(xbeans,hostsource,epoch_time):
	nn_mp_perm_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Eden Space')
	print hostsource+" nn_mp_perm_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['Usage'].get('committed'))
	print hostsource+" nn_mp_perm_usage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['Usage'].get('init'))
	print hostsource+" nn_mp_perm_usage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['Usage'].get('max'))
	print hostsource+" nn_mp_perm_usage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['Usage'].get('used'))
	print hostsource+" nn_mp_perm_peakusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" nn_mp_perm_peakusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" nn_mp_perm_peakusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" nn_mp_perm_peakusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['PeakUsage'].get('used'))
	print hostsource+" nn_mp_perm_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['CollectionUsage'].get('committed'))
	print hostsource+" nn_mp_perm_collectionusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['CollectionUsage'].get('init'))
	print hostsource+" nn_mp_perm_collectionusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['CollectionUsage'].get('max'))
	print hostsource+" nn_mp_perm_collectionusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_perm_pointer_id]['CollectionUsage'].get('used'))

#9
def get_nn_os(xbeans,hostsource,epoch_time):
	nn_os_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=OperatingSystem')
	print hostsource+" nn_os_OpenFileDescriptorCount "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('OpenFileDescriptorCount'))
	print hostsource+" nn_os_MaxFileDescriptorCount "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('MaxFileDescriptorCount'))
	print hostsource+" nn_os_CommittedVirtualMemorySize "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('CommittedVirtualMemorySize'))
	print hostsource+" nn_os_TotalSwapSpaceSize "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('TotalSwapSpaceSize'))
	print hostsource+" nn_os_FreeSwapSpaceSize "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('FreeSwapSpaceSize'))
	print hostsource+" nn_os_ProcessCpuTime "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('ProcessCpuTime'))
	print hostsource+" nn_os_FreePhysicalMemorySize "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('FreePhysicalMemorySize'))
	print hostsource+" nn_os_TotalPhysicalMemorySize "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('TotalPhysicalMemorySize'))
	print hostsource+" nn_os_SystemCpuLoad "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('SystemCpuLoad'))
	print hostsource+" nn_os_ProcessCpuLoad "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('ProcessCpuLoad'))
	print hostsource+" nn_os_SystemLoadAverage "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('SystemLoadAverage'))
	print hostsource+" nn_os_AvailableProcessors "+str(epoch_time)+" "+str(xbeans[nn_os_pointer_id].get('AvailableProcessors'))

#10
def get_nn_mp_survivor(xbeans,hostsource,epoch_time):
	nn_mp_survivor_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Par Survivor Space')
	print hostsource+" nn_mp_survivor_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['Usage'].get('committed'))
	print hostsource+" nn_mp_survivor_usage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['Usage'].get('init'))
	print hostsource+" nn_mp_survivor_usage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['Usage'].get('max'))
	print hostsource+" nn_mp_survivor_usage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['Usage'].get('used'))
	print hostsource+" nn_mp_survivor_peakusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" nn_mp_survivor_peakusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" nn_mp_survivor_peakusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" nn_mp_survivor_peakusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['PeakUsage'].get('used'))
	print hostsource+" nn_mp_survivor_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['CollectionUsage'].get('committed'))
	print hostsource+" nn_mp_survivor_collectionusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['CollectionUsage'].get('init'))
	print hostsource+" nn_mp_survivor_collectionusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['CollectionUsage'].get('max'))
	print hostsource+" nn_mp_survivor_collectionusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_survivor_pointer_id]['CollectionUsage'].get('used'))

#12
def get_nn_mp_oldgen(xbeans,hostsource,epoch_time):
	nn_mp_oldgen_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=CMS Old Gen')
	print hostsource+" nn_mp_oldgen_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['Usage'].get('committed'))
	print hostsource+" nn_mp_oldgen_usage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['Usage'].get('init'))
	print hostsource+" nn_mp_oldgen_usage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['Usage'].get('max'))
	print hostsource+" nn_mp_oldgen_usage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['Usage'].get('used'))
	print hostsource+" nn_mp_oldgen_peakusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" nn_mp_oldgen_peakusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" nn_mp_oldgen_peakusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" nn_mp_oldgen_peakusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['PeakUsage'].get('used'))
	print hostsource+" nn_mp_oldgen_collectionusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['CollectionUsage'].get('committed'))
	print hostsource+" nn_mp_oldgen_collectionusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['CollectionUsage'].get('init'))
	print hostsource+" nn_mp_oldgen_collectionusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['CollectionUsage'].get('max'))
	print hostsource+" nn_mp_oldgen_collectionusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_oldgen_pointer_id]['CollectionUsage'].get('used'))

#13
def get_nn_replication(xbeans,hostsource,epoch_time):
	nn_replication_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Replication')
	print hostsource+" nn_replication_sink.appliedOps "+str(epoch_time)+" "+str(xbeans[nn_replication_pointer_id].get('sink.appliedOps'))
	print hostsource+" nn_replication_sink.appliedBatches "+str(epoch_time)+" "+str(xbeans[nn_replication_pointer_id].get('sink.appliedBatches'))
	print hostsource+" nn_replication_sink.ageOfLastAppliedOp "+str(epoch_time)+" "+str(xbeans[nn_replication_pointer_id].get('sink.ageOfLastAppliedOp'))
#14
def get_nn_mp_codecache(xbeans,hostsource,epoch_time):
	nn_mp_codecache_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=MemoryPool,name=Code Cache')
	print hostsource+" nn_mp_codecache_usage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['Usage'].get('committed'))
	print hostsource+" nn_mp_codecache_usage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['Usage'].get('init'))
	print hostsource+" nn_mp_codecache_usage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['Usage'].get('max'))
	print hostsource+" nn_mp_codecache_usage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['Usage'].get('used'))
	print hostsource+" nn_mp_codecache_peakusage_committed "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['PeakUsage'].get('committed'))
	print hostsource+" nn_mp_codecache_peakusage_init "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['PeakUsage'].get('init'))
	print hostsource+" nn_mp_codecache_peakusage_max "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['PeakUsage'].get('max'))
	print hostsource+" nn_mp_codecache_peakusage_used "+str(epoch_time)+" "+str(xbeans[nn_mp_codecache_pointer_id]['PeakUsage'].get('used'))

#15
def get_nn_jvm(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=JvmMetrics')
	print hostsource+" nn_jvm_MemNonHeapUsedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemNonHeapUsedM'))
	print hostsource+" nn_jvm_MemNonHeapCommittedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemNonHeapCommittedM'))
	print hostsource+" nn_jvm_MemHeapUsedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemHeapUsedM'))
	print hostsource+" nn_jvm_MemHeapCommittedM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemHeapCommittedM'))
	print hostsource+" nn_jvm_MemMaxM "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MemMaxM'))
	print hostsource+" nn_jvm_GcCountParNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCountParNew'))
	print hostsource+" nn_jvm_GcTimeMillisParNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillisParNew'))
	print hostsource+" nn_jvm_GcCountConcurrentMarkSweep "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCountConcurrentMarkSweep'))
	print hostsource+" nn_jvm_GcTimeMillisConcurrentMarkSweep "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillisConcurrentMarkSweep'))
	print hostsource+" nn_jvm_GcCount "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcCount'))
	print hostsource+" nn_jvm_GcTimeMillis "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GcTimeMillis'))
	print hostsource+" nn_jvm_ThreadsNew "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsNew'))
	print hostsource+" nn_jvm_ThreadsRunnable "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsRunnable'))
	print hostsource+" nn_jvm_ThreadsBlocked "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsBlocked'))
	print hostsource+" nn_jvm_ThreadsWaiting "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsWaiting'))
	print hostsource+" nn_jvm_ThreadsTimedWaiting "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsTimedWaiting'))
	print hostsource+" nn_jvm_ThreadsTerminated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ThreadsTerminated'))
	print hostsource+" nn_jvm_LogFatal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogFatal'))
	print hostsource+" nn_jvm_LogError "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogError'))
	print hostsource+" nn_jvm_LogWarn "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogWarn'))
	print hostsource+" nn_jvm_LogInfo "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LogInfo'))

#17
def get_fsnamesys(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=FSNamesystemState')
	print hostsource+" fsnamesys_CapacityTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityTotal'))
	print hostsource+" fsnamesys_CapacityUsed "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsed'))
	print hostsource+" fsnamesys_CapacityRemaining "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityRemaining'))
	print hostsource+" fsnamesys_TotalLoad "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalLoad'))
	print hostsource+" fsnamesys_BlocksTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlocksTotal'))
	print hostsource+" fsnamesys_MaxObjects "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MaxObjects'))
	print hostsource+" fsnamesys_FilesTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesTotal'))
	print hostsource+" fsnamesys_PendingReplicationBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PendingReplicationBlocks'))
	print hostsource+" fsnamesys_UnderReplicatedBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('UnderReplicatedBlocks'))
	print hostsource+" fsnamesys_ScheduledReplicationBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ScheduledReplicationBlocks'))
	print hostsource+" fsnamesys_PendingDeletionBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PendingDeletionBlocks'))
	print hostsource+" fsnamesys_BlockDeletionStartTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockDeletionStartTime'))
	print hostsource+" fsnamesys_FSState "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FSState'))
	print hostsource+" fsnamesys_NumLiveDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumLiveDataNodes'))
	print hostsource+" fsnamesys_NumDeadDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDeadDataNodes'))
	print hostsource+" fsnamesys_NumDecomLiveDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecomLiveDataNodes'))
	print hostsource+" fsnamesys_NumDecomDeadDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecomDeadDataNodes'))
	print hostsource+" fsnamesys_VolumeFailuresTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('VolumeFailuresTotal'))
	print hostsource+" fsnamesys_EstimatedCapacityLostTotal "+str(epoch_time)+" "+str(xbeans[pointer_id].get('EstimatedCapacityLostTotal'))
	print hostsource+" fsnamesys_NumDecommissioningDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumDecommissioningDataNodes'))
	print hostsource+" fsnamesys_NumStaleDataNodes "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumStaleDataNodes'))
	print hostsource+" fsnamesys_NumStaleStorages "+str(epoch_time)+" "+str(xbeans[pointer_id].get('NumStaleStorages'))
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=FSNamesystem')
	print hostsource+" fsnamesys_MissingBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MissingBlocks'))
	print hostsource+" fsnamesys_MissingReplOneBlocks "+str(epoch_time)+" "+str(xbeans[pointer_id].get('MissingReplOneBlocks'))
	print hostsource+" fsnamesys_ExpiredHeartbeats "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ExpiredHeartbeats'))
	print hostsource+" fsnamesys_TransactionsSinceLastCheckpoint "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsSinceLastCheckpoint'))
	print hostsource+" fsnamesys_TransactionsSinceLastLogRoll "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsSinceLastLogRoll'))
	print hostsource+" fsnamesys_LastCheckpointTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('LastCheckpointTime'))
	print hostsource+" fsnamesys_CapacityTotalGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityTotalGB'))
	print hostsource+" fsnamesys_CapacityUsedGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsedGB'))
	print hostsource+" fsnamesys_CapacityRemainingGB "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityRemainingGB'))
	print hostsource+" fsnamesys_CapacityUsedNonDFS "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CapacityUsedNonDFS'))

#11
def get_nn_retrycache(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=RetryCache.NameNodeRetryCache')
	print hostsource+" nn_retrycache_CacheHit "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheHit'))
	print hostsource+" nn_retrycache_CacheCleared "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheCleared'))
	print hostsource+" nn_retrycache_CacheUpdated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheUpdated'))

#19
def get_nn_threading(xbeans,hostsource,epoch_time):
	nn_treading_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Threading')
	print hostsource+" nn_threading_ThreadCount "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('ThreadCount'))
	print hostsource+" nn_threading_TotalStartedThreadCount "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('TotalStartedThreadCount'))
	print hostsource+" nn_threading_CurrentThreadCpuTime "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('CurrentThreadCpuTime'))
	print hostsource+" nn_threading_CurrentThreadUserTime "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('CurrentThreadUserTime'))
	print hostsource+" nn_threading_PeakThreadCount "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('PeakThreadCount'))
	print hostsource+" nn_threading_DaemonThreadCount "+str(epoch_time)+" "+str(xbeans[nn_treading_pointer_id].get('DaemonThreadCount'))


#def get_nn_region_tables_type(xbeans):
	#nn_regions_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Regions')
	#while xbeans[nn_regions_id]:
		#tabletype = xbeans[pointer]['name']
		#if catname == lookupcategory:
			#return pointer
			#pointer += 1
	#return 254

#21
#def get_nn_regions(xbeans):
	#nn_regions_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=Regions'))
	#print hostsource+" nn_regions_

#22
def get_nn_wal(xbeans,hostsource,epoch_time):
	nn_wal_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=RegionServer,sub=WAL')
	print hostsource+" nn_wal_rollRequest "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('rollRequest'))
	print hostsource+" nn_wal_SyncTime_num_ops "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('SyncTime_num_ops'))
	print hostsource+" nn_wal_SyncTime_min "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('SyncTime_min'))
	print hostsource+" nn_wal_SyncTime_max "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('SyncTime_max'))
	print hostsource+" nn_wal_AppendSize_num_ops "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendSize_num_ops'))
	print hostsource+" nn_wal_AppendSize_min "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendSize_min'))
	print hostsource+" nn_wal_AppendSize_max "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendSize_max'))
	print hostsource+" nn_wal_AppendTime_num_ops "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendTime_num_ops'))
	print hostsource+" nn_wal_AppendTime_min "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendTime_min'))
	print hostsource+" nn_wal_AppendTime_max "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('AppendTime_max'))
	print hostsource+" nn_wal_slowAppendCount "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('slowAppendCount'))
	print hostsource+" nn_wal_lowReplicaRollRequest "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('lowReplicaRollRequest'))
	print hostsource+" nn_wal_appendCount "+str(epoch_time)+" "+str(xbeans[nn_wal_pointer_id].get('appendCount'))

#23
def get_nn_gc_new(xbeans,hostsource,epoch_time):
	nn_gc_new_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=GarbageCollector,name=ParNew')
	print hostsource+" nn_gc_new_CollectionCount "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id].get('CollectionCount'))
	print hostsource+" nn_gc_new_CollectionTime "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id].get('CollectionTime'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
	print hostsource+" nn_gc_new_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(xbeans[nn_gc_new_pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))

#24
def get_nn_hbsys(xbeans,hostsource,epoch_time):
	nn_hbsys_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=MetricsSystem,sub=Stats')
	print hostsource+" nn_hbsys_NumActiveSources "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('NumActiveSources'))
	print hostsource+" nn_hbsys_NumAllSources "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('NumAllSources'))
	print hostsource+" nn_hbsys_NumActiveSinks "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('NumActiveSinks'))
	print hostsource+" nn_hbsys_NumAllSinks "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('NumAllSinks'))
	print hostsource+" nn_hbsys_SnapshotNumOps "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('SnapshotNumOps'))
	print hostsource+" nn_hbsys_SnapshotAvgTime "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('SnapshotAvgTime'))
	print hostsource+" nn_hbsys_PublishNumOps "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('PublishNumOps'))
	print hostsource+" nn_hbsys_PublishAvgTime "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('PublishAvgTime'))
	print hostsource+" nn_hbsys_DroppedPubAll "+str(epoch_time)+" "+str(xbeans[nn_hbsys_pointer_id].get('DroppedPubAll'))

#5
def get_nn_activity(xbeans,hostsource,epoch_time):
	pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=NameNode,name=NameNodeActivity')
	print hostsource+" nn_activity_CreateFileOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CreateFileOps'))
	print hostsource+" nn_activity_FilesCreated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesCreated'))
	print hostsource+" nn_activity_FilesAppended "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesAppended'))
	print hostsource+" nn_activity_GetBlockLocations "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetBlockLocations'))
	print hostsource+" nn_activity_FilesRenamed "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesRenamed'))
	print hostsource+" nn_activity_FilesTruncated "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesTruncated'))
	print hostsource+" nn_activity_GetListingOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetListingOps'))
	print hostsource+" nn_activity_DeleteFileOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('DeleteFileOps'))
	print hostsource+" nn_activity_FilesDeleted "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesDeleted'))
	print hostsource+" nn_activity_FileInfoOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FileInfoOps'))
	print hostsource+" nn_activity_AddBlockOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('AddBlockOps'))
	print hostsource+" nn_activity_GetAdditionalDatanodeOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetAdditionalDatanodeOps'))
	print hostsource+" nn_activity_CreateSymlinkOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CreateSymlinkOps'))
	print hostsource+" nn_activity_GetLinkTargetOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetLinkTargetOps'))
	print hostsource+" nn_activity_FilesInGetListingOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FilesInGetListingOps'))
	print hostsource+" nn_activity_AllowSnapshotOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('AllowSnapshotOps'))
	print hostsource+" nn_activity_DisallowSnapshotOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('DisallowSnapshotOps'))
	print hostsource+" nn_activity_CreateSnapshotOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CreateSnapshotOps'))
	print hostsource+" nn_activity_DeleteSnapshotOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('DeleteSnapshotOps'))
	print hostsource+" nn_activity_RenameSnapshotOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('RenameSnapshotOps'))
	print hostsource+" nn_activity_ListSnapshottableDirOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('ListSnapshottableDirOps'))
	print hostsource+" nn_activity_SnapshotDiffReportOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SnapshotDiffReportOps'))
	print hostsource+" nn_activity_BlockReceivedAndDeletedOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReceivedAndDeletedOps'))
	print hostsource+" nn_activity_StorageBlockReportOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('StorageBlockReportOps'))
	print hostsource+" nn_activity_TransactionsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsNumOps'))
	print hostsource+" nn_activity_TransactionsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsAvgTime'))
	print hostsource+" nn_activity_SyncsNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SyncsNumOps'))
	print hostsource+" nn_activity_SyncsAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SyncsAvgTime'))
	print hostsource+" nn_activity_TransactionsBatchedInSync "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TransactionsBatchedInSync'))
	print hostsource+" nn_activity_BlockReportNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportNumOps'))
	print hostsource+" nn_activity_BlockReportAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('BlockReportAvgTime'))
	print hostsource+" nn_activity_CacheReportNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheReportNumOps'))
	print hostsource+" nn_activity_CacheReportAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('CacheReportAvgTime'))
	print hostsource+" nn_activity_SafeModeTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('SafeModeTime'))
	print hostsource+" nn_activity_FsImageLoadTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('FsImageLoadTime'))
	print hostsource+" nn_activity_GetEditNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetEditNumOps'))
	print hostsource+" nn_activity_GetEditAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetEditAvgTime'))
	print hostsource+" nn_activity_GetImageNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetImageNumOps'))
	print hostsource+" nn_activity_GetImageAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('GetImageAvgTime'))
	print hostsource+" nn_activity_PutImageNumOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PutImageNumOps'))
	print hostsource+" nn_activity_PutImageAvgTime "+str(epoch_time)+" "+str(xbeans[pointer_id].get('PutImageAvgTime'))
	print hostsource+" nn_activity_TotalFileOps "+str(epoch_time)+" "+str(xbeans[pointer_id].get('TotalFileOps'))

#27
def get_nn_ipc(xbeans,hostsource,epoch_time):
	nn_ipc_pointer_id = get_metricscategory_position(xbeans, 'Hadoop:service=HBase,name=IPC,sub=IPC')
	print hostsource+" nn_ipc_queueSize "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('queueSize'))
	print hostsource+" nn_ipc_numCallsInGeneralQueue "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('numCallsInGeneralQueue'))
	print hostsource+" nn_ipc_numCallsInReplicationQueue "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('numCallsInReplicationQueue'))
	print hostsource+" nn_ipc_numCallsInPriorityQueue "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('numCallsInPriorityQueue'))
	print hostsource+" nn_ipc_numOpenConnections "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('numOpenConnections'))
	print hostsource+" nn_ipc_numActiveHandler "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('numActiveHandler'))
	print hostsource+" nn_ipc_TotalCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('TotalCallTime_num_ops'))
	print hostsource+" nn_ipc_TotalCallTime_min "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('TotalCallTime_min'))
	print hostsource+" nn_ipc_TotalCallTime_max "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('TotalCallTime_max'))
	print hostsource+" nn_ipc_TotalCallTime_mean "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('TotalCallTime_mean'))
	print hostsource+" nn_ipc_TotalCallTime_median "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('TotalCallTime_median'))
	print hostsource+" nn_ipc_exceptions.FailedSanityCheckException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.FailedSanityCheckException'))
	print hostsource+" nn_ipc_exceptions.RegionMovedException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.RegionMovedException'))
	print hostsource+" nn_ipc_QueueCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('QueueCallTime_num_ops'))
	print hostsource+" nn_ipc_QueueCallTime_min "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('QueueCallTime_min'))
	print hostsource+" nn_ipc_QueueCallTime_max "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('QueueCallTime_max'))
	print hostsource+" nn_ipc_QueueCallTime_mean "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('QueueCallTime_mean'))
	print hostsource+" nn_ipc_QueueCallTime_median "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('QueueCallTime_median'))
	print hostsource+" nn_ipc_authenticationFailures "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('authenticationFailures'))
	print hostsource+" nn_ipc_authorizationFailures "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('authorizationFailures'))
	print hostsource+" nn_ipc_exceptions "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions'))
	print hostsource+" nn_ipc_RequestSize_num_ops "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('RequestSize_num_ops'))
	print hostsource+" nn_ipc_RequestSize_min "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('RequestSize_min'))
	print hostsource+" nn_ipc_RequestSize_max "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('RequestSize_max'))
	print hostsource+" nn_ipc_RequestSize_mean "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('RequestSize_mean'))
	print hostsource+" nn_ipc_RequestSize_median "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('RequestSize_median'))
	print hostsource+" nn_ipc_ResponseSize_num_ops "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ResponseSize_num_ops'))
	print hostsource+" nn_ipc_ResponseSize_min "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ResponseSize_min'))
	print hostsource+" nn_ipc_ResponseSize_max "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ResponseSize_max'))
	print hostsource+" nn_ipc_ResponseSize_mean "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ResponseSize_mean'))
	print hostsource+" nn_ipc_ResponseSize_median "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ResponseSize_median'))
	print hostsource+" nn_ipc_authenticationSuccesses "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('authenticationSuccesses'))
	print hostsource+" nn_ipc_authorizationSuccesses "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('authorizationSuccesses'))
	print hostsource+" nn_ipc_ProcessCallTime_num_ops "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ProcessCallTime_num_ops'))
	print hostsource+" nn_ipc_ProcessCallTime_min "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ProcessCallTime_min'))
	print hostsource+" nn_ipc_ProcessCallTime_max "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ProcessCallTime_max'))
	print hostsource+" nn_ipc_ProcessCallTime_mean "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ProcessCallTime_mean'))
	print hostsource+" nn_ipc_ProcessCallTime_median "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('ProcessCallTime_median'))
	print hostsource+" nn_ipc_exceptions.NotServingRegionException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.NotServingRegionException'))
	print hostsource+" nn_ipc_sentBytes "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('sentBytes'))
	print hostsource+" nn_ipc_exceptions.RegionTooBusyException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.RegionTooBusyException'))
	print hostsource+" nn_ipc_receivedBytes "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('receivedBytes'))
	print hostsource+" nn_ipc_exceptions.OutOfOrderScannerNextException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.OutOfOrderScannerNextException'))
	print hostsource+" nn_ipc_exceptions.UnknownScannerException "+str(epoch_time)+" "+str(xbeans[nn_ipc_pointer_id].get('exceptions.UnknownScannerException'))

def usage():
	print sys.argv[0],"-h[elp] -n[namenode server name] -t[ime]"

def main():
	#print sys.argv
	if len(sys.argv[1:]) < 1:
		usage()
		sys.exit(3)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "htn:", ["help","time", "namenode="])
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
		elif opt in ("-n", "--namenode"):
			server = arg
			epoch_time = int(time.time())
			beans = load_jmx("http://"+server+":50070/jmx")

	get_nn_memory(beans,server,epoch_time)
	get_nn_status(beans,server,epoch_time)
	get_nn_rpc(beans,server,epoch_time)
	get_nn_ugi(beans,server,epoch_time)
	#get_nn_GC_marksweep(beans,server,epoch_time)
	get_nn_bufferpool(beans,server,epoch_time)
	get_nn_activity(beans,server,epoch_time)
	get_nn_compilation(beans,server,epoch_time)
	#get_nn_mp_eden(beans,server,epoch_time)
	#get_nn_mp_perm(beans,server,epoch_time)
	#get_nn_mp_survivor(beans,server,epoch_time)
	#get_nn_mp_codecache(beans,server,epoch_time)
	#get_nn_mp_oldgen(beans,server,epoch_time)
	get_nn_os(beans,server,epoch_time)
	#get_nn_retrycache(beans,server,epoch_time)
	#get_nn_jvm(beans,server,epoch_time)
	#get_nn_threading(beans,server,epoch_time)
	#get_nn_gc_new(beans,server,epoch_time)
	get_fsnamesys(beans,server,epoch_time)

#main(sys.argv)
if __name__ == "__main__":
    main()

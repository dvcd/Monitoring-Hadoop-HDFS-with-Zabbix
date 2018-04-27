# Monitoring-Hadoop-HDFS-with-Zabbix
This repo shows how to monitor hadoop HDFS with Zabbix

This project incorporates minibig's intial developement of monitoring HDFS. Since minibig doesn't update anymore. This project tries to present a usable monitorinig solution on HDFS with Zabbix 3.x. With updates on autodiscovery of datanodes, volumes. Thanks to the contribution of minibig.


Here is the necessary configurations:
1. On Namenode
agent config setting at NameNode:

UserParameter=nn.getlivenode,/usr/bin/python /etc/zabbix/externalscripts/namenode_get_livenode.py

UserParameter=nn.getlivenodedetails,/usr/bin/python /etc/zabbix/externalscripts/namenode_get_livenoded.py

UserParameter=nn.livenodegetstatus[*],/usr/bin/python /etc/zabbix/externalscripts/nn_livenodegetstatus.py $1 $2

 cron configuration at NameNode:

* * * * * /etc/zabbix/externalscripts/minibig_zabbix_hdfs_namenode.sh 10.69.130.1

* * * * * /etc/zabbix/externalscripts/minibig_zabbix_hdfs_datanode.sh 10.69.130.2

* * * * * /etc/zabbix/externalscripts/minibig_zabbix_hdfs_datanode.sh 10.69.130.3

* * * * * /etc/zabbix/externalscripts/minibig_zabbix_hdfs_datanode.sh 10.69.130.4

* * * * * /etc/zabbix/externalscripts/minibig_zabbix_hdfs_datanode.sh 10.69.130.5

2.On Datanode
agent config setting at DataNode:

UserParameter=dn.getvolume,/usr/bin/python /etc/zabbix/externalscripts/datanode_get_vol.py

UserParameter=dn.getvolumedetails,/usr/bin/python /etc/zabbix/externalscripts/datanode_get_vold.py

UserParameter=dn.getvolumestatus[*],/usr/bin/python /etc/zabbix/externalscripts/dn_volgetstatus.py $1 $2

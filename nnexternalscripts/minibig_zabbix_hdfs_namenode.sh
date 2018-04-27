#!/bin/bash

PYTHON_SCRIPT_HOME=/etc/zabbix/externalscripts
ZABBIX_SENDER=/usr/bin/zabbix_sender
ZABBIX_SERVER=zabbix.ygomi.com
ZABBIX_PORT=10051
SOURCE_HOST=${1}

RC=0

#/usr/bin/python ${PYTHON_SCRIPT_HOME}/minibig_hdfs_namenode.py -n ${SOURCE_HOST} | ${ZABBIX_SENDER} -z ${ZABBIX_SERVER} -p ${ZABBIX_PORT} -T -i - >/dev/null 2>&1
/usr/bin/python ${PYTHON_SCRIPT_HOME}/minibig_hdfs_namenode.py -n ${SOURCE_HOST} | ${ZABBIX_SENDER} -vv -z ${ZABBIX_SERVER} -p ${ZABBIX_PORT} -T -i -
let RC=${RC}+${?}

exit ${RC}

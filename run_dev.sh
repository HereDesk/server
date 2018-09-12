#!/bin/bash

#杀死进程
ps -ef | grep python3 | grep -v grep | awk '{print $2}' | xargs kill -9

#启动uwsgi
num=`ps -ef | grep python3 | grep -v grep | wc -l`
if [ 0 -eq ${num} ];then
	echo " -> Success: kill the process."
	python3 manage_dev.py runserver
else
	echo " -> Error:Please check."
fi
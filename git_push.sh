#!/bin/bash

set -e
[ $# -ne 1 ] && echo "Usage : sh $0 message " && exit
message=$1
echo "添加文件到本地仓库"
git add .
sleep 2

echo "提交文件到本地仓库"
git commit -m "$message" &>/dev/null
sleep 2

echo "提交文件到远程仓库，github"
git push origin master


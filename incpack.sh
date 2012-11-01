#!/bin/sh
# @desc 
#   this script can generate a incmental package 
#   from the version $start_version(not inclued the $start_version) to the $end_version 
#   where svn path is $svn_path 
# 
# @version 0.1
# @author bugzhu
# 

#the following three parameters must be seted by yourselfs
svn_path=/data/home/bugzhu/snswin/ #the svn path where you want to package
start_version=1883 #start version, change in start_version will not be included!
end_version=1905 #end version

today=$(date +'%Y%m%d')
prefix=${HOME}/incpack_${today} #create the package in your HOME path

test -e ${prefix} && rm -rf ${prefix}
if [ -e $svn_path ];then
	cd $svn_path
	svn diff -r ${start_version}:${end_version} --summarize | cut -d ' ' -f 8 | while read file
	do
		if [ -f ${svn_path}${file} ];then
#filepath=${prefix}$(echo ${file} | awk -F/ '{gsub($NF,"");sub(".$", "");print}')
			filepath=`dirname ${prefix}/${file}`
			test ! -e $filepath && mkdir -p $filepath
			cp ${svn_path}${file} $filepath
		fi
	done
	tar -C ${HOME} -zcvf ${prefix}.tar.gz incpack_${today}  
	rm -rf ${prefix}
fi

echo incmental package ${prefix}.tar.gz has been created!

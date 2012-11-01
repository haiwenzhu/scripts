#!/usr/bin/python
'''
 @desc 
   this script can generate a incmental package 
   from the version $start_version(not inclued the $start_version) to the $end_version 
   where svn path is $svn_path 
 
 @version 0.1
 @author bugzhu
'''

from datetime import date
import os
import shutil
import commands
import sys

#the following three parameters must set by yourselfes
svn_path = '/data/home/bugzhu/snswin/'
start_version = 1883 #changes in start version will not be includes
end_version = 1905

today = date.today().strftime('%Y%m%d')
home = os.environ['HOME']
target = home + '/incpack_' + today

if os.path.exists(target) :
	if os.path.isdir(target) :
		shutil.rmtree(target)
	else :
		os.remove(target)

if os.path.exists(svn_path) :
	os.chdir(svn_path)
	status, output = commands.getstatusoutput('svn diff -r ' + str(start_version) + ':' + str(end_version) + ' --summarize')
	if status == 0 :
		output = output.splitlines()
		for file in output :
			file = file[1:].lstrip()
			src_file = svn_path + file
			dest_file = target + '/' + file
			if os.path.isfile(src_file) :
				if not os.path.exists(os.path.dirname(dest_file)) :
					os.makedirs(os.path.dirname(dest_file))
				shutil.copy(src_file, dest_file)
		os.chdir(home)
		os.system('tar -C ' + home + ' -zcvf ' + target + '.tar.gz incpack_' + today)
		shutil.rmtree(target)
		print 'incremental package ' + target + '.tar.gz has been created!'
	else :
		print output
		sys.exit()
else :
	print 'path ' + svn_path + ' dose not exists!' 

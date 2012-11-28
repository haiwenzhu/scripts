#!/usr/bin/python
'''
 @desc 
   this script can generate a incmental package 
   from the version $start_version(not inclued the $start_version) to the $end_version 
   where svn path is $svn_path 
   the script accept 4 parameters
	@param $svn_path svn base path (required)
	@param $start_version the start version of svn,changes in start version will not be included (required)
	@param $end_version the end version of svn (required)
	@param $the the directory where you want put the package,default to current path (optional)

 @usage
    python incpack.py --svn_path=/data/home/snvpath --start_version=1000 --end_version=2000 --prefix=/data/home/bugzhu
 
 @version 0.1
 @author bugzhu
'''

from datetime import date
import os
import shutil
import commands
import sys

#handle params
svn_path = ''
start_version = ''
end_version = ''
prefix = os.path.abspath('.')
for param in sys.argv[1:] :
	param_partion = param.split('=')
	if param_partion[0] == '--svn_path' :
		svn_path = param_partion[1]
	elif param_partion[0] == '--start_version' :
		start_version = param_partion[1]
	elif param_partion[0] == '--end_version' :
		end_version = param_partion[1]
	elif param_partion[0] == '--prefix' :
		prefix = param_partion[1]

if svn_path == '' or start_version == '' or end_version == '' :
	print 'usage is: python incpack.py --svn_path=/data/home/snvpath --start_version=1000 --end_version=2000 --prefix=/data/home/bugzhu\n'
	sys.exit();

if not os.path.exists(svn_path) :
	print 'svn_path:' + svn_path + ' dose not exists!\n'
	sys.exit()

if not os.path.exists(prefix) :
	print 'prefix:' + prefix + ' dose not exists!'
	sys.exit();

svn_path = svn_path.rstrip('/');
today = date.today().strftime('%Y%m%d')
target = prefix + '/incpack_' + today

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
			src_file = svn_path + '/' + file
			dest_file = target + '/' + file
			if os.path.isfile(src_file) :
				if not os.path.exists(os.path.dirname(dest_file)) :
					os.makedirs(os.path.dirname(dest_file))
				shutil.copy(src_file, dest_file)
		os.chdir(target)
		os.system('tar -C ' + target + ' -zcvf ' + target + '.tar.gz *')
		shutil.rmtree(target)
		print 'incremental package ' + target + '.tar.gz has been created!'
	else :
		print output
		sys.exit()
else :
	print 'path ' + svn_path + ' dose not exists!' 

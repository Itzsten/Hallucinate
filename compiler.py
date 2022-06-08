# | -------------------------------------------------------------------------------- |
# |  Compiler.py - Responsible for compiling the Python files into an executable.    |
# | -------------------------------------------------------------------------------- |

filename = "main.py"
output_name = "Hallucinate"
include_stuff = True

key_aes256 = 'HAL256Ucin5234#!3gArTlJ'
run_as_admin = True

version = '6.6.6.6'
company_name = "Itzsten"
file_description = "Realtime Hallucinations"

upx_dir = r"upx"

import os
import shutil
import time
import cv2
import sys
import pyinstaller_versionfile as pyvrs

pyvrs.create_versionfile(
    output_file="version.txt",
    version=version,
    company_name=company_name,
    file_description=file_description,
    internal_name="Hallucinate",
    legal_copyright="Hallucinate written by Itzsten",
    original_filename="Hallucinate.exe",
    product_name="Hallucinate.exe"
)


cvdir = os.sep.join(cv2.__file__.split(os.sep)[:-1])

#try:shutil.rmtree('build')
#except:pass

def walk(dire):
    paths = []
    for subdir, dirs, files in os.walk(dire):
        for fn in files:
            paths.append(subdir + os.sep + fn)
    return paths
with open('i.ico', 'w') as f:
	f.write('\000' * 8) # empty icon
icon = 'i.ico'
includes = []
previous_dir = []
fname_d = '.'.join(filename.split('.')[:-1])
if include_stuff:
	for subdir, dirs, files in os.walk('include'):
		
		directory = subdir + os.sep
		if directory!='include\\':
			if not True in [directory.startswith(de) for de in previous_dir]:
				previous_dir.append(directory)
				includes.append('--add-data "{};{}";.'.format(directory[:-1].replace('\\','/'), directory.split('\\')[-2].replace('\\','/') + '/'))
		for file in files:
			if not True in [((subdir + os.sep + file).replace('/','\\')).startswith(de) for de in previous_dir]:
				includes.append( '--add-data "{};.;"'.format(subdir + os.sep + file))

#print(previous_dir)
command = """pyinstaller −−key "{}" −−upx-dir "{}" −−noconfirm −−onefile −−version−file version .txt −-windowed {}−−icon "{}" {} "{}" """.format(key_aes256, upx_dir, "-−uac-admin " if run_as_admin else "", icon,' '.join(includes), filename)
print('>>> ' + command)
os.system(command)
os.remove(icon)
os.remove("version.txt")

time.sleep(3)

try:shutil.rmtree('build')
except:
	pass
try:
	os.rename('dist', 'build')
except:
	time.sleep(3)
	try:os.rename('dist', 'build')
	except:pass
try:os.rename('build/{}.exe'.format(fname_d), 'build/{}.exe'.format(output_name))
except:pass
print("Build completed")

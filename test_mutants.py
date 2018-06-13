import os
import sys

mutant_directory = sys.argv[1]
project_directory = sys.argv[2]
current_directory = os.getcwd()
if 'mutantsReport.txt' in os.listdir(current_directory):
	os.system('rm mutantsReport.txt')

total_num = 0
file_list = os.listdir(mutant_directory)

for mutant_file in file_list:
	if '.py' in mutant_file: 
		path = '/'.join(mutant_file.split('.')[:-2][0].split('___')[1:-1])
		mutant_python_file = '.'.join(mutant_file.split('.')[:-1])
		original_python_file = mutant_python_file.split('___')[-1]
		
		execution_directory = project_directory + '/' + path
		os.chdir(mutant_directory)
		os.system('mv %s %s'%(mutant_file, execution_directory))
		os.chdir(execution_directory)
		os.system('mv %s %s'%(original_python_file, mutant_directory))
		os.system('mv %s %s'%(mutant_file, mutant_python_file))
		
		os.system('echo Executing %s 1>> %s/mutantsReport.txt'% (mutant_file, current_directory))
		os.system('python %s 2>> %s/mutantsReport.txt'%(mutant_python_file, current_directory))
		
		os.system('mv %s %s'%(mutant_python_file, mutant_file))
		os.system('mv %s %s'%(mutant_file, mutant_directory))

		os.chdir(mutant_directory)
		os.system('mv %s %s'%(original_python_file, execution_directory))
		os.chdir(current_directory)

		total_num += 1

os.chdir(current_directory)
count_err = 0
with open('mutantsReport.txt') as f:
	for line in f.readlines():
		if 'Error:' in line:
			count_err += 1

print '%d errors out of %d files'%(count_err, total_num)
os.system('python "%s/src/checkErr.py" mutantsReport.txt'%current_directory)

		#mv 
#print mutant_directory, project_directory
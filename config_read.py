import sys
import configparser
import getopt

def getopts():
	env=''
	opts, args=getopt.getopt(sys.argv[1:],'he:',['help=','env=',])

	for opt, arg in opts:
		
		if opt not in ('-e','--env'):
			print('incorrect parameter')
			sys.exit()
		if opt in('-e','--env'):
			if arg not in('QA','PSC'):
				print('incorrect env')
				sys.exit()
		else:
			env=arg
			print (arg)
	return env

def get_config():

	my_env=getopts()
	config=configparser.ConfigParser()
	config.read('trial_config.ini')
	database= config.get(my_env,'dbdb')

	print (database)

get_config()	
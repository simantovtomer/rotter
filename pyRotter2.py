import sys
import urllib
import getopt


#print help

def printHelp():
    print 'Usage:'
    print '  -h, --help     show help'
    print '  -q, --quit     quit app'
    print '  -v, --version  show version'
    print '  -a, --all      all rows'


#get web content

def getWebContent():

	url='http://rotter.net/rss/rotternews.xml'

	return urllib.urlopen(url).readlines()


#display data

def displayData(srcLines,maxRows):

	counter=0

	for line in srcLines:

		if "<item>" in line:
		
			line=line.decode("cp1255").encode("utf-8")

			title   = line[line.find("<title>")+7 : line.find("</title>")]

			print unicode(title, 'utf-8')[::-1]

			counter+=1

			if counter>maxRows:
				sys.exit(0)



#parse commands

opts, args = getopt.getopt(sys.argv[1:], "hva", ["help", "version", "all"])

displayAll=0

for o, a in opts:

    if o in ('-h','--help'):
		printHelp()
		sys.exit(2)
    elif o in ('-v','--version'):
		print 'Version: 1.0.0'
		sys.exit(2)
    elif o in ('-a','--all'):
		displayAll=1



#get web contents

srcLines=getWebContent()


#display web content

if displayAll==1:
	displayData(srcLines,5000)
else:
	displayData(srcLines,5)

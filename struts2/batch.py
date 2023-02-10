import sys,os,subprocess

#headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

def run():
	text = str(sys.argv[1])
	exp = str(sys.argv[2])

	with open(text,"r") as f:
		for line in f.readlines():
			domain = str(line.strip())
			try:
				test = "{0}{1}".format(exp,domain)
				print "#"*20,test,"#"*20
				p = subprocess.Popen('%s' % test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    
				#print p.stdout.readlines() 
				result = []   
				for t in p.stdout.readlines():    
					result.append(str(t))    
				retval = p.wait()
				test_result = ''.join(result)
				#print domain
				print test_result
			except:
				print "[-]:",domain,"fail!"

if __name__ == '__main__':
	if len(sys.argv) < 3 :
		print "python %s 'domain.txt' cmd " % sys.argv[0]
		sys.exit(0)
	run()


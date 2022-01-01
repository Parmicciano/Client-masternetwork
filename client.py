import json
import requests, subprocess
import random, os, time
import os
from dotenv import load_dotenv
load_dotenv()
BASEURL = os.getenv('BASEURL')
PRICE = os.getenv('PRICE')

while True :
    try :
        random1 = random.randint(100,999999999999999989999)
        headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.38"
        }
        r = requests.get(BASEURL+'/'+str(PRICE),headers=headers)
        dacode =  r.json()
        dacode = dacode[1:]
        dacode = dacode[:-1]
        lecode = dacode.split(",")
        jobchosen = lecode[random.randint(0,len(lecode)-1)]
        jobchosen = jobchosen.replace('"',"")
        jobchosen = jobchosen.replace(' ',"")
        print('newjob !')
        print(jobchosen)
        r = requests.get(BASEURL+'/code/'+jobchosen)
        elcode = r.json()
        f = open(str(random1)+".py", "w")
        f.write(str(elcode[0]))
        f.close()
        
        try : 
            start_time = time.time()
            subprocess.run("python3 "+str(random1)+".py "+ str(jobchosen), shell=True, check=True,  stdout=subprocess.DEVNULL, timeout=600)
            print(time.time() - start_time, "seconds")
        except :
            os.popen("python3 -m  pipreqs.pipreqs . --force")
            os.popen("pip3 install requirements.txt")
            pass
        os.remove(str(random1)+".py")
    except:
        print("error, retrying ...")
        time.sleep(2)
        pass

import threading
import requests, subprocess
import  os, time
import os
from dotenv import load_dotenv
load_dotenv()
BASEURL = os.getenv('BASEURL')
PRICE = os.getenv('PRICE')

def script():
    while True :
        try :
            headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.38"
            }
            r = requests.get(BASEURL+'/python/'+str(PRICE),headers=headers)
            dacode =  r.json()
            dacode = dacode.replace('"',"")
            print('newjob !')
            print(dacode)
            r = requests.get(BASEURL+'/pythoncode/'+dacode)
            elcode = r.json()
            f = open(str(dacode), "w")
            f.write(str(elcode[0]))
            f.close()
            try : 
                start_time = time.time()
                subprocess.run("python3 "+str(dacode), shell=False, check=True,  stdout=subprocess.DEVNULL, timeout=600)
                print(time.time() - start_time, "seconds")
            except :
                os.popen("python3 -m  pipreqs.pipreqs . --force")
                os.popen("pip3 install -r requirements.txt")
                pass
        except:
            print("error, retrying ...")
            time.sleep(50)
            pass

if __name__ == "__main__":
    t1 = threading.Thread(target=script)
    t2 = threading.Thread(target=script)
    t3 = threading.Thread(target=script)
    t4 = threading.Thread(target=script)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

  
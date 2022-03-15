import requests, random, subprocess, os, io, time, zipfile, threading
from dotenv import load_dotenv
load_dotenv()
BASEURL = os.getenv('BASEURL')
PRICE = os.getenv('PRICE')
#docker build --tag client .
#docker run --name=client -e PYTHONUNBUFFERED=1 -d client
if not os.path.exists("./filetorun/"):
    os.makedirs("./filetorun/")

def script():
    while True :
        try:
            headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.38"
            }
            r = requests.get(BASEURL+'/python/'+str(PRICE),headers=headers)
            folderid =  r.json()
            
            r = requests.get(BASEURL+'/getfile/'+folderid, stream=True)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            dapath = "./filetorun/"+str(random.randint(0,9999988898999989))
            z.extractall(dapath)
            try :
               
                start_time = time.time()
                subprocess.run("python3 "+dapath+"/main.py", shell=True, check=True, timeout=600)
                print('newjob !')
                os.remove(dapath)
                print(time.time() - start_time, "seconds")
            except : 
                pass
        except :
            print("error, retrying ...")
            time.sleep(50)
            pass

if __name__ == "__main__":
    n = 1
    x = 0
    while x < n :
        x+= 1
        threading.Thread(target=script).start()








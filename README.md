# Client-masternetwork
This is the client that allows your computer to execute python script in exchange of monero 

About auto update :
```
from git import Repo # pip3 install GitPython
import os # already in python3
def git_pull_change(path):
    repo = Repo(path)
    current = repo.head.commit

    repo.remotes.origin.pull()

    if current == repo.head.commit:
        print("Repo not changed. Sleep mode activated.")
        return False
    else:
        print("Repo changed! Activated.")
        return True


if  git_pull_change("./Client-masternetwork") == True : 
    os.chdir("./Client-masternetwork/client-repo-docker")
    os.system("docker build --tag client .")
    os.system("docker rm -f client")
    os.system("docker run --name=client -e PYTHONUNBUFFERED=1 -d client")
```

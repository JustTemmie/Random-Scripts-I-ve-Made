from git import Repo
import random
import time

for x in range(0,20000):
    repo = Repo(".")
    repo.git.add(update=True)
    repo.index.commit("spam to inflate the numbers lmao")
    origin = repo.remote(name="origin")
    if x % 400 == 0:
        print("push")
        origin.push()
        time.sleep(3)
    
    with open('random.txt', 'w') as f:
        f.write(str(random.randrange(0,999999999999999999999999999999999999999999999999999999999999999999)))
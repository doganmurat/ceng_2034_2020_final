#MURAT DOGAN 170709033
from multiprocessing import Pool
import os,uuid,requests,hashlib

url = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","​https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg​ ","​http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg​ ","​https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg​ "]

hashes = []

def download(url, file_name=None):
    r = requests.get(url, allow_redirects=True)
    file = file_name if file_name else str(uuid.uuid4())
    open(file, 'wb').write(r.content)

def gethash(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    hashes.append(hash_md5.hexdigest()) 

def isDuplicate(lists):
    if len(lists) == len(set(lists)):
        print("There is not duplicate files")
    else:
        print("There is duplicate files")

print("Parent proc", os.getpid())
child = os.fork()
if child==0:
    print("Child proc", os.getpid())
    download(​url[0],"img1")
    download(​url[1],"img2")
    download(​url[2],"img3")
    download(​url[3],"img4")
    download(​url[4],"img5")
    os._exit(0)
os.wait()

with Pool(5) as p:
    p.map(gethash, ["img1","img2","img3","img4","img5"])
    p.map(isDuplicate, ["hashes"])



 



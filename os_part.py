import os
from urllib.request import urlretrieve

url='https://dblp.org/rec/journals/access/LiZZPY22.bib?param=1'
dir=os.path.abspath('.')
dir=os.path.join(dir,'need')

if not os.path.exists(dir):
    print("creating...");
    os.makedirs(dir)
    print("success")

filepath=os.path.join(dir,'1.bib')
urlretrieve(url,filepath);

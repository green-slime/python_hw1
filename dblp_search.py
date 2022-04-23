from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
import re

class dblp:
    'class for crawling'
    
    header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

    def __init__(self,author):
        
        self.author=author;
        author=author.replace(" ","%20");
        self.url="https://dblp.org/search?q="+author;
        self.response=requests.get(self.url,headers=dblp.header);       
        self.doc=self.response.text;
        self.response.close();        
        self.soup=BeautifulSoup(self.doc,'lxml');
        self.biblist=self.soup.find('ul',class_='publ-list').find_all('a',href=re.compile("view=bibtex"));
        self.links=[];
        for link in self.biblist:
            self.links.append(link['href']);
        # we print out the result and find that the 2kth and the 2k+1th links are the same
        self.n=int(len(self.links)/2);
        for i in range(self.n,0,-1):
            self.links.pop(2*i-1);
        for i in range(0,self.n):
            self.links[i]=self.links[i].replace(".html?view=bibtex",".bib?param=1")
            # now they are download links
        self.titlelist=self.soup.find_all('span',class_='title');
        self.titles=[]; # used for listbox in gui
        for title in self.titlelist:
            self.titles.append(title.text);
        for i in range(0,self.n):
            self.titles[i]=str(i)+"_"+self.titles[i];
    def printbib(self):
        print(self.links);

    def create_dir(self,dir=''):
        if dir=='' or dir=='Default':
            dir=os.path.abspath('.')
            dir=os.path.join(dir,self.author)   # Default: download in workdir
        if not os.path.exists(dir):
            print("Cannot detect this folder, creating a new one...");
            os.makedirs(dir)
        self.dir=dir;

    def download_all_bib(self,dir=''):
        self.create_dir(dir); 
        dir=self.dir;   
        for i in range(0,self.n):
            print("downloading "+str(i)+"th bib;")
            filepath=os.path.join(dir,str(i)+".bib")
            urlretrieve(self.links[i],filepath); 
        print("success in downloading "+str(self.n)+" bibs.");

    def download_selected_bib(self,dir='',index=[]):
        self.create_dir(dir);
        dir=self.dir;  
        for i in index:
            print("downloading "+str(i)+"th bib;")
            filepath=os.path.join(dir,str(i)+".bib")
            urlretrieve(self.links[i],filepath);
        print("success in downloading "+str(len(index))+" bibs.");


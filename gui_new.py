import tkinter as tk
import dblp_search as crawl

win=tk.Tk();
win.title("homework1: dblp downloader");
win.geometry('750x600+400+50');

authorname="";
dir="";

welcome=tk.Label(win,text="Thanks for using dblp bib downloader!",bg='red',fg='gold',anchor='center',font=('arial',30));
welcome.grid(row=0,column=0,columnspan=2)
l=tk.Label(win,text="Enter the name of the author:",bg='silver',fg='black');
l.grid(row=1,column=0)
w=tk.Entry(win);
w.grid(row=2,column=0)
messvar=tk.StringVar();
messvar.set("Click search and wait for a moment...")
dirvar=tk.StringVar();
dirvar.set("dir has not been set.")
lbox=tk.Listbox(win,selectmode=tk.MULTIPLE,width=100,height=20);
l4=tk.Label(win,bg='snow',fg='green')

def dir1(top):
    global dir
    dir='Default';
    dirvar.set("current dir is "+dir);
    top.destroy();

def dir2(str,top):
    global dir
    dir=str;
    dirvar.set("current dir is "+dir);
    top.destroy();

def cancel(top):
    top.destroy();

def download_dir(): # child widget
    top=tk.Toplevel();
    top.title("Choose the download dir");
    l2=tk.Label(top,text="Enter the download dir with the seperator of \'\\\\\',or click \'Default\' to download in the workdir.",bg='silver',fg='black').grid(row=0,column=0,columnspan=3);
    w2=tk.Entry(top);
    w2.delete(0,"end");
    w2.insert(0,dir);
    w2.grid(row=1,column=0,columnspan=3);
    
    b1=tk.Button(top,text="Default",command=lambda:dir1(top)).grid(row=2,column=0);
    b2=tk.Button(top,text="OK",command=lambda:dir2(w2.get(),top)).grid(row=2,column=1);
    b3=tk.Button(top,text="Cancel",command=lambda:cancel(top)).grid(row=2,column=2);


def dl_s(a,dir):
    sl=lbox.curselection();
    a.download_selected_bib(dir,sl);
    l4.config(text='Selected documents have been downloaded.') 
    l4.grid(row=6,column=0,columnspan=2);
def dl_all(a,dir):
    a.download_all_bib(dir)
    l4.config(text='All documents have been downloaded.') 
    l4.grid(row=6,column=0,columnspan=2);
    
def search():
    global authorname;
    authorname=w.get();
    messvar.set("正在检索"+authorname+"相关bib");
    a=crawl.dblp(authorname);
    messvar.set("成功生成"+authorname+"的"+str(a.n)+"篇bib链接");    
    
    lbox.delete(0,'end');
    for articles in a.titles:
        lbox.insert('end',articles)
    lbox.grid(row=4,column=0,columnspan=2)
    
    d_selected=tk.Button(win,text="Download Selected",command=lambda:dl_s(a,dir))
    d_selected.grid(row=5,column=0)  
    d_all=tk.Button(win,text="Download All",command=lambda: dl_all(a,dir))  
    d_all.grid(row=5,column=1)
    

b=tk.Button(win,text="search",command=search);
b.grid(row=3,column=0)
mess=tk.Label(win,textvariable=messvar,bg='silver',fg='black',width=40);
mess.grid(row=1,column=1)
d=tk.Button(win,text="choose dir",command=download_dir);
l3=tk.Label(win,textvariable=dirvar,bg='silver',fg='black')
d.grid(row=2,column=1)
l3.grid(row=3,column=1)

win.mainloop();
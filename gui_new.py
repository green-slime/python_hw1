import tkinter as tk
import dblp_search as crawl

win=tk.Tk();
win.title("homework1");
win.geometry('800x600+400+50');

authorname="";
dir="";

l=tk.Label(win,text="Enter the name of the author:",bg='silver',fg='black');
l.pack();
w=tk.Entry(win);
w.pack();
messvar=tk.StringVar();
dirvar=tk.StringVar();
dirvar.set("dir has not been set.")
lbox=tk.Listbox(win,selectmode=tk.MULTIPLE);

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

    l3.pack();

def dl(a,dir):
        sl=lbox.curselection();
        a.download_selected_bib(dir,sl);

def search():
    global authorname;
    authorname=w.get();
    messvar.set("正在检索"+authorname+"相关bib");
    a=crawl.dblp(authorname);
    messvar.set("成功生成"+authorname+"的"+str(a.n)+"篇bib链接");    
    d.pack();
    l3.pack();
    
    for articles in a.links:
        lbox.insert('end',articles)
    lbox.pack();
    
    d_selected=tk.Button(win,text="Download Selected",command=lambda:dl(a,dir))
    d_selected.pack();   
    d_all=tk.Button(win,text="Download All",command=lambda:a.download_all_bib(dir))   
    d_all.pack();
    

b=tk.Button(win,text="search",command=search);
b.pack();
mess=tk.Label(win,textvariable=messvar,bg='silver',fg='black',width=40);
mess.pack();
d=tk.Button(win,text="choose dir",command=download_dir);
l3=tk.Label(win,textvariable=dirvar,bg='silver',fg='black')

win.mainloop();
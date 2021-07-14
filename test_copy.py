# coding=gbk
import os,time
from tkinter import Entry, Tk
import tkinter.filedialog as dir
from tkinter.ttk import Treeview
def findSOMEFile(base,search_key):
    
    for root, ds, fs in os.walk(base):
        for f in fs:
            if search_key in f:
            #if (res := re.match(f'{search_key}')):
                fullname = os.path.join(root, f)
                yield fullname

def findAllFile(base):#遍历
    
    for root, ds, fs in os.walk(base):
        for f in fs:
           
            fullname = os.path.join(root, f)
            yield fullname


def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
 
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)





#'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

 
 


#'''获取文件的创建时间'''
def get_FileCreateTime(filePath):

    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


#'''获取文件的修改时间'''
def get_FileModifyTime(filePath):

    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)

def tree_claer(tree:Treeview):
    for item in tree.get_children():
        tree.delete(item)

def key_search(user_text1:Entry,user_text:Entry,tree:Treeview):
    tree_claer(tree)
    base = user_text1.get()
    searchkey = user_text.get()
    j=0
    for i in findSOMEFile(base,searchkey):
        j+=1
        value = [j,i,str(getDocSize(i)),get_FileCreateTime(i),get_FileModifyTime(i)]
        
        tree.insert('','end',values=value)
        

def size_search(user_text1:Entry,user_text:Entry,tree:Treeview):
    tree_claer(tree)
    base = user_text1.get()
    searchkey = user_text.get()
    j=0
    for i in findAllFile(base):
        if getDocSize(i)==searchkey:
            j+=1
            value = [j,i,str(getDocSize(i)),get_FileCreateTime(i),get_FileModifyTime(i)]
        
            tree.insert('','end',values=value)

def CT_search(user_text1:Entry,user_text:Entry,tree:Treeview):
    tree_claer(tree)
    base = user_text1.get()
    searchkey = user_text.get()
    j=0
    for i in findAllFile(base):
        if get_FileCreateTime(i)==searchkey:
            j+=1
            value = [j,i,str(getDocSize(i)),get_FileCreateTime(i),get_FileModifyTime(i)]
        
            tree.insert('','end',values=value) 


def MT_search(user_text1:Entry,user_text:Entry,tree:Treeview):
    tree_claer(tree)

    base = user_text1.get()
    searchkey = user_text.get()
    j=0
    for i in findAllFile(base):
        if get_FileModifyTime(i)==searchkey:
            j+=1
            value = [j,i,str(getDocSize(i)),get_FileCreateTime(i),get_FileModifyTime(i)]
        
            tree.insert('','end',values=value)            

def tree_del(event,tree:Treeview) -> None:
    item = tree.selection()[0]
    itemData = tree.item(item, "values")
    itemData = [itemData[i] for i in range(3)]
    tree.delete(item)




    
    
    
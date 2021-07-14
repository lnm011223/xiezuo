# coding=gbk
from test_copy import CT_search,MT_search,key_search,size_search, tree_del

from tkinter import *
from tkinter import ttk
import tkinter.filedialog as dir



 

class searchUI:
    def __init__(self):
        
        root = Tk()
        self.master=root
        
        self.draw(root)
        
    
    def draw(self,root):
        
        
        root.title('简易搜索工具')
        root.geometry('1000x600')
        l1=Label(text='请输入用于搜索的关键字：')
        l1.pack()
        user_text=Entry()
        user_text.pack()
        l2=Label(text='请输入需要搜索的文件夹路径：')
        l2.pack()
        user_text1=Entry()
        user_text1.pack()
        
        col=[1,2,3,4,5]
        tree =ttk.Treeview(root, columns=col,show='headings')
        
        tree.heading('1',text='序号')
        tree.heading('2',text='文件名')
        tree.heading('3',text='文件大小')
        tree.heading('4',text='创建时间')
        tree.heading('5',text='修改时间')
        
        tree.column('1',width=50,anchor='center')
        tree.column('2',width=450,anchor='center')
        tree.column('3',width=100,anchor='center')
        tree.column('4',width=200,anchor='center')
        tree.column('5',width=200,anchor='center')
        
        start_search1=Button(root,text='用文件名关键字搜索',command=lambda user_text1=user_text1,user_text=user_text,tree=tree :key_search(user_text1,user_text,tree))
        start_search2=Button(root,text='用文件大小搜索',command=lambda user_text1=user_text1,user_text=user_text,tree=tree :size_search(user_text1,user_text,tree))
        start_search3=Button(root,text='用创建时间搜索',command=lambda user_text1=user_text1,user_text=user_text,tree=tree :CT_search(user_text1,user_text,tree))
        start_search4=Button(root,text='用最后修改时间搜索',command=lambda user_text1=user_text1,user_text=user_text,tree=tree :MT_search(user_text1,user_text,tree))
        

        tree.bind('<Button-3>',lambda event,tree=tree: tree_del(event,tree))
        start_search1.pack()
        start_search2.pack()
        start_search3.pack()
        start_search4.pack()
        

        tree.pack()
        root.mainloop()
        

if __name__ == '__main__':
    
    searchUI()
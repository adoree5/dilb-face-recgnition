import os.path
from gain_face import gain
from load_known_faces import load_known_faces
import pandas as pd
from io_help import save_to_csv,append_to_csv,clear_csv
def create_data():  #构造csv数据
    names, datas = load_known_faces('datas', 0)
    save_to_csv(names,datas,'data.csv')
def add_data(name):  #添加csv数据
    gain(name)
    names,datas = load_known_faces('face',1)
    clear('face')
    append_to_csv(names,datas,'data.csv')
def remove(name): #移除数据
    path = os.path.join('datas',name)
    for i in os.listdir(path):
        os.remove(os.path.join(path, i))
    os.rmdir(path)
def clear(dir): #清空指定目录数据
    for name in os.listdir(dir):
        path  = os.path.join(dir,name)
        for p in os.listdir(path):
            os.remove(os.path.join(path,p))
        os.rmdir(path)
def clearall(): #清空所有数据
    clear('face')
    clear('datas')
    clear_csv('data.csv')
op = input('input your opration:(cla,add,rm,cr)\n')
if op == 'cla':clearall()
elif op =='add':
    name = input('input your name\n')
    print('collecting......')
    add_data(name)
    print('done')
elif op == 'rm':
    name = input('input name you want to remove\n')
    remove(name)
    create_data()
    print('remove successfully')
elif op == 'cr':
    create_data()
else:print('error')
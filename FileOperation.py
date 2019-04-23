# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import os

# 该返回path目录下一级的文件
path = 'D:\\'

def ls(path):
    return os.listdir(path)

# 返回路径连接
def path_join(path,*filename):
    return os.path.join(path,*filename)

# 判断文件是否为文件夹
def isdir(filename):
    return os.path.isdir(filename)

# 返回path该目录下(一级)所有绝对路径
def abspath_list(path):
    dirlist = ls(path)
    absdirlist = []
    for i in dirlist:
        absdirlist.append(path_join(path,i))
    return absdirlist

# # 递归返回path下所层级的所有文件的有绝对路径
# def deep_abspath_list(begin_path):
#     print(begin_path,"-->","\n")
#     current_all_file_name = abspath_list(begin_path)
#
#     dir_list = []
#     file_list = []
#     for i in current_all_file_name:
#         if isdir(i):
#             dir_list.append(i)
#         else:
#             file_list.append(i)
#
#     print("file->:", file_list)
#     print("dir-->:",dir_list)
#     for dir_i in dir_list:
#         deep_abspath_list(dir_i)




path_ = r"C:\Users\guoyongqi\Desktop\os_test"
def operating_one_category_file_all(path,file_postfix):
    info_dict = {'1':'删除同类文件',
                 '2':'将同类文件移动',
                 '3':'输出同类文件绝对路径',
                 '4':'为文件添加同一前缀',
                 '5':'为文件添加同一后缀'}
    for k,v in info_dict.items():
        print(k,":",v,"\n")
    operating_num = input("请输入你要操作的数字：")

    if operating_num == '1':
        confirm = input("删除文件，不可逆操作，请谨慎。如确定请输入1：")
    else:
        confirm = input("确定你的选择是{}吗？如确定请输入1：".format(info_dict[operating_num]))

    target_list = []
    for dirpath,dirnames,filenames in os.walk(path):
        for file_i in filenames:
            file_absname = (path_join(dirpath,file_i))
            if file_postfix in file_absname:
                target_list.append(file_absname)

    if operating_num == '1' and confirm == '1':
        [os.remove(i) for i in target_list]

    if operating_num == '2' and confirm == '1':
        import shutil
        # shutil.move(src, dst) #先复制后移动，最后删除，被占用的不会删除
        # os.rename(sourceFile, targetFile) #占用也可以被移动
        target_dir = input("请输入要移动至的目录路径：")


operating_one_category_file_all(path_,'txt')
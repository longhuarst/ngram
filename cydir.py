#coding=utf-8

import os






def getFileTree(root) :
    print(root)


    for top in os.walk(root):
        print("root = ", root)

    for dirs in os.walk(root) :
        print("sub dirs = ",dirs)

    for files in os.walk(root):
        print("files =", files)



if __name__ == '__main__':
    getFileTree("D:\\17111\\")
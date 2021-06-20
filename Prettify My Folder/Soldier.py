# oh soldier prettify my folder
# take a path from user which has folders and files,
# do not change folders only operate on files
# include.txt file which includes names of files and folders we have to capatilize
# capitalize only files and not folders
# ask user to specify any format type files he wants to rename in proper order. example jpg

import os
def soldier(path,file,format):
    folder_list=(os.listdir(path))
    print(folder_list)
    os.chdir(path)

    # this file includes name of those files which user wants to capatilaize
    f=open(file)
    list=f.read().split(",")
    print(list)

    # loop to capatilize those files
    for item in folder_list:
        if os.path.isfile(item):
            if item in list:
                os.rename(item,item.capitalize())


    # to rename the files
    count=0
    for x in folder_list:
        if os.path.isfile(x):
            format_type=os.path.splitext(x)
            if format_type[1]==format and format_type[0]!="exclude":
                count=count+1
                os.rename(x,f"{count}{format}")


ask=input("enter the path :")
soldier(ask,"include.txt",".jpg")
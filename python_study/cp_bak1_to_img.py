import dircache
import os.path
from os import system




if __name__ == "__main__":
    img_list=dircache.listdir(".");
    for img in img_list:
      print(img);
      if img[-2:]==".1":
        cmd="copy .\\"+img+" " + ".\\"+img[:-2]
        print(cmd);
        ret=system(cmd)
        print ret  
import dircache
import os.path
from os import system

package_dir=['ASWDIR', 'BLCODE', 'LFILES', 'LINDIR', 'MMDIRE', 'OFILES', 'RDTEMP', 'WEBFIL']
src_dir=['corr0','corr1','corr2','corr3','corr4_SWBT_OK']

def patch_corr_to_package(file):
  for dir in package_dir:
    path = '.\\'+dir+'\\'+os.path.basename(file)
    # print path
    if(os.path.exists(path)) :
      do_copy(file, path)
      break
  print(file + " is patched to" + dir)
  
def do_copy(src, target):
  if(not os.path.exists(target)):
    return
  print(src + ' is going to patch to ' + target)
  cmd='copy /y ' + src + ' ' + target
  print("cmd is: " + cmd);
  system(cmd)


if __name__ == "__main__":
  for src in src_dir:
    print('handling ' + src)
    all_corr=dircache.listdir(src)
    for corr_file in all_corr:
      src_file='.\\' + src + '\\' + corr_file
      patch_corr_to_package(src_file) 
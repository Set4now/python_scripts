import os

def list_files(cur_dir):
#  files = os.listdir(cur_dir)
  lof = []
  for file in os.listdir(cur_dir):
    lof.append(file)
  return lof

print list_files('/scripts_python')



  

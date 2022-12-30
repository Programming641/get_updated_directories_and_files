import os, sys
from pathlib import Path
import pickle
import datetime, shutil

from sys import platform

if platform == "linux":
   directory_separator = "/"
elif platform == "win32":
   directory_separator = "\\"

def create_dirs_cp_file( filepath, top_dirname, dest_topdir ):
   # in windows, directory is separated by \\. in linux directory seperator is /
   os_fixed_filepath = filepath.replace("\\", ",").replace("/", ",")
   
   print("os_fixed_filepath " + os_fixed_filepath )
   
   split_path = os_fixed_filepath.split(",")
   top_dir_index = split_path.index( top_dirname )

   for dir_index in range( top_dir_index + 1, len( split_path ) - 1 ):
      dest_topdir += "/" + split_path[dir_index]

      if not os.path.exists( dest_topdir ):
         os.makedirs( dest_topdir )
   
   shutil.copy( file_cp, dest_topdir )


def modified_or_not(cur_file ):

   cur_file_mtime = os.path.getmtime( cur_file )
   cur_file_mtime = datetime.datetime.fromtimestamp( cur_file_mtime )

   if type(last_updated_time) is datetime.datetime:
      if cur_file_mtime > last_updated_time:
         modified_dirs_files.append( cur_file )
   elif type(last_updated_time) is str and last_updated_time == "first time":
      # this is the first time so copy all files need to be copied to destination
      modified_dirs_files.append( cur_file )



def go_into_dir(cur_dir):
   #print()
   #print("current directory " + cur_dir)

   dir_contents = os.listdir( cur_dir )

   #print("current directory contents")
   #print(dir_contents)
   #print()

   for dir_content in dir_contents:
      cur_fullpath = cur_dir + "/" + dir_content
      if os.path.isdir( cur_fullpath ):
         go_into_dir( cur_fullpath )

      else:
         # current dir_content is file
         #print("current file " + cur_fullpath ) 
         modified_or_not( cur_fullpath )
         

destination = input("enter directory path where you want to copy all updated files:")

destination = destination.strip()

last_update_fname = "last_update.data"


if not os.path.exists( last_update_fname ):
   f = Path(last_update_fname)
   f.touch(exist_ok=True)

if os.stat("last_update.data").st_size == 0:
   print("last update file is emtpy or just has been created")
   last_updated_time = "first time"
   
else:
   last_update_file = open(last_update_fname, "rb")
   last_updated_time = pickle.load(last_update_file)
   last_update_file.close()



top_dir = os.getcwd()

print("top_dir " + top_dir)

top_dirs_files = os.listdir()

print( top_dirs_files )

modified_dirs_files = list()


for top_dir_or_file in top_dirs_files:
   if os.path.isdir(top_dir_or_file):
      go_into_dir( top_dir + "/" + top_dir_or_file )

   else:
      print("current file " + top_dir + "/" + top_dir_or_file )

      modified_or_not( top_dir + "/" + top_dir_or_file )



print("modified_dirs_files")
print(modified_dirs_files)
     
# copying all the modified files to destination

# copy top directory if not exists

topdir_path = top_dir.split(directory_separator)

top_dirname = topdir_path[len(topdir_path) - 1 ]

print("top_dirname " + top_dirname)

dest_topdir = destination + "/" + top_dirname

if not os.path.exists( dest_topdir ):
   os.makedirs( dest_topdir )

for file_cp in modified_dirs_files:
   create_dirs_cp_file( file_cp, top_dirname, dest_topdir )



last_updated_file = open( "last_update.data", "wb" )

current_time = datetime.datetime.now()
pickle.dump( current_time, last_updated_file )

last_updated_file.close()









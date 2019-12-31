
import os

work_dir = os.getcwd()
print(work_dir)

os.chdir("..")
work_dir = os.getcwd()
print(work_dir)

print(dir(os))
for str in dir(os):
    if str.find("get") != -1:
        print(str)
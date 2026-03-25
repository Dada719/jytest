# s=open("lib/wwenjian.txt","a",encoding="utf-8")
# lst = ["1","2","3","4","5","6","7","8","9"]
#
# for item in lst:
#     s.write(item+"\n")
#
# s.close()

#
# with open("lib/222.jpeg", "r", encoding="utf-8") as s:
#     print(s.read())
import os
import time

with open("lib/wwenjian.txt","r",encoding="utf-8") as fh,\
    open("lib/wwenjian1.txt","w",encoding="utf-8") as fw:
    for line in fh:
        if line.startswith("z"):
            line =line.replace("z","Z")
        fw.write(line)
time.sleep(5)
os.remove("lib/wwenjian.txt")
time.sleep(3)
os.rename("lib/wwenjian1.txt","lib/wwenjian.txt")




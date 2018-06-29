import os
for root, dirs, files in os.walk("testpics", topdown=True):
   for name in dirs:
      print(os.path.join(root, name))

# (Windows Defender may prevent you from running)
# (make sure pip and pyinstaller are installed/updated)

# 1. cd to directory that contains your .py file

# 2. pyinstaller -F -w -i icon.ico clock.py

#   -F   (all in 1 file)
#   -w   (removes terminal window)
#   -i icon.ico  (adds custom icon to .exe)
#   clock.py  (name of your main python file)

# 3. exe is located in the dist folder
# ~/W/p/python-learning/e/1-python-course-bro-code/clock | main ?3  pyinstaller -F -w -i icon.ico clock.py   
import os

for file in os.listdir('.'):
    if file.endswith('.ui'):
        os.system(f'pyuic5 -x {file} -o {file.replace(".ui", ".py")}')
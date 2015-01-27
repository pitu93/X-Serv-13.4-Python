#!/user/bin/python
# -*- coding: utf-8 -*-

fd=open("/etc/passwd", "r")
lineas = fd.readlines();

longitud= range(0, len(lineas))

for usuario in longitud :
    print(lineas[usuario].split(":")[0] + " utiliza " + lineas[usuario].split(":")[len(lineas[usuario].split(":"))-1])

print("En esta máquina hay " + str(len(lineas)) + " usuarios");

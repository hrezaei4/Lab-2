#!/usr/bin/env python3
import sys
#Author: Hossein Rezaei
#Author ID: 188348213
#Date Created: 2024/09/23
if len(sys.argv) == 2:
 timer = int(sys.argv[1])
else:
 timer = 3
 
while timer > 0:
 print(timer)
 timer -= 1  

print("blast off!")
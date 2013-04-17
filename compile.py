#! /usr/bin/python

import os, subprocess, logging

def prep()
  subprocess.check_output("java -jar apktool.jar if .\source\system\framework\framework-res.apk", stderr=subprocess.STDOUT, shell=True ) 
  subprocess.check_output("java -jar apktool.jar if .\source\system\framework\framework-miui-res.apk" , stderr=subprocess.STDOUT, shell=True) 

def decompile( work )
  prep()
  try:
    subprocess.check_output("java -jar apktool.jar d -b .\source\system\%s .\source\system\%s.out" , stderr=subprocess.STDOUT, shell=True % ( work, work ) )
  except:
    return work
    continue

def compile( work )
  errors=list()
  try:
    subprocess.check_output("java -jar apktool.jar b .\source\system\%s.out" , stderr=subprocess.STDOUT, shell=True % ( work ) )
  except:
    return work
    continue
  try:
    os.remove('.\source\system\%s.out\build\apk\AndroidManifest.xml' % ( work ) )
    subprocess.check_output('winrar a -afzip -ep1 -df -r -m5 .\source\system\%s .\source\system\%s.out\build\apk\*' % ( work, work ) )
  except:
    print("Failed to append to rar file.")  # need actual logging here
    return work


#decompile
#w=open('files.txt', r)
#for files in w.readlines():
#  decompile(files)

# loop through the working file list
w.seek(0,0)
retry=list()
for files in w.readlines():
  retry.append(compile(files))

w.close()

# retry 
while retry:
  attempt=1
  while attempt:
    attempt=raw_input("You have some failed file attempts.  Would you like to retry? Y/N" )
    if attempt.uppercase() == 'Y':
      attempt = 0
      for files in retry:
        retry.remove(files)
        retry.append(compile(files))
    else if attempt.uppercase() == 'N':
      attempt = 0
      retry = list()
    else: attempt = 1

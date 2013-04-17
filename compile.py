#! /usr/bin/python

import os, subprocess, logging

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


# loop through the working file list
retry=list()
w=open('files.txt', r)
for files in w.readlines():
  retry.append(compile(files))

w.close()

# retry 
if retry:
  attempt=1
  while attempt:
    attempt=raw_input("You have some failed file attempts.  Would you like to retry? Y/N" )
    if attempt.uppercase() == 'Y':
      attempt = 0
      for files in retry:
        compile(files)
    else if attempt.uppercase() == 'N':
      attempt = 0
    else: attempt = 1

#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
  if len(sys.argv) != 2:
    assert(0)
  #print(sys.argv[0])
  #print(sys.argv[1])
  target_dir = sys.argv[1];
  if not os.path.exists(target_dir):
    print("%s not exists" % target_dir)
  if not os.path.isdir(target_dir):
    print("%s is not dir" % target_dir)
  names = os.listdir(target_dir)
  for name in names:
    if name.endswith(".dex"):
      dexpath = os.path.join(target_dir,name)
      cmd = "java -jar ~/bin/baksmali d %s" % dexpath
      print(cmd)
      os.system(cmd)

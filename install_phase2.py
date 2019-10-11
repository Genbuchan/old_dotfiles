#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import sys

def main() :
  internet()
  creative()
  writing()
  games()
  development()
  sys.exit()

def development() :
  print("\nPhase 5. Install development environment")
  installApps(["visual-studio-code", "virtualbox", "local-by-flywheel",])
  installCaskApps(["node", "vagrant", "docker"])
  installVSCodeExtension(["hookyqr.beautify", "michelemelluso.code-beautifier", "anseki.vscode-color", "msjsdiag.debugger-for-chrome", "dbaeumer.vscode-eslint", "oderwat.indent-rainbow", "MS-CEINTL.vscode-language-pack-ja", "ritwickdey.liveserver", "ms-python.python", "octref.vetur", "peakchen90.vue-beautify"])
  return 0

def creative() :
  print("\nPhase 2. Install creative applications")
  installCaskApps(["adobe-creative-cloud", "blender"])
  return 0

def internet() :
  print("\nPhase 1. Install internet applications")
  installCaskApps(["google-chrome", "firefox", "discord", "slack"])
  return 0

def writing() :
  print("\nPhase 3. Install writing applications")
  installCaskApps(["typora"])
  return 0

def games() :
  print("\nPhase 4. Install games")
  installCaskApps(["minecraft"])
  return 0

# apps引数に、Appの名前を配列で格納して代入
def installApps(apps) :
  for appName in apps :
    print("Installing", appName)
    #subprocess.run("brew install " + appName, shell=True)
  return 0

# apps引数に配列にCask Appの名前を配列で格納して代入
def installCaskApps(apps) :
  for appName in apps :
    print("Installing", appName)
    #subprocess.run("brew cask install " + appName, shell=True)
  return 0

# exts引数にExtensionの名前を配列で格納して代入
def installVSCodeExtension(exts) :
  for extName in exts :
    print("Installing", extName)
    #subprocess.run("/Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin/code --install-extension " + extName, shell=True)

main()

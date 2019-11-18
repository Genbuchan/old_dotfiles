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
  installCaskApps(["visual-studio-code", "virtualbox", "vagrant", "docker"])
  installApps(["node"])
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
  for app in apps :
    print("Installing", app)
    subprocess.run("brew install " + app, shell=True)
  return 0

# apps引数に配列にCask Appの名前を配列で格納して代入
def installCaskApps(apps) :
  for app in apps :
    print("Installing", app)
    subprocess.run("brew cask install " + app, shell=True)
  return 0

# exts引数にExtensionの名前を配列で格納して代入
def installVSCodeExtension(exts) :
  for ext in exts :
    print("Installing", ext)
    subprocess.run("/Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin/code --install-extension " + ext, shell=True)

main()

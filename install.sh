#!/bin/bash

# This is a dotfiles.
# You can install many applications and configuration.
#
# Genbu's dotfiles
#
# ver 1.0 (Karasuma)
#

# Initialize
init () {
  echo -e "\nGenbu's dotfiles ver 1.0 (Karasuma)"
  echo -e "\nReady? [Y/n] > "
  read ready
  if [ "$ready" = "y" ] || [ "$ready" = "Y" ] || [ "$ready" = "" ]; then
    main
  elif [ "$ready" = "n" ] || [ "$ready" = "N" ]; then
    exit
  else
    exit
  fi
  exit
}

# Main
main () {
  # Homebrew をインストール
  homebrew

  # Python 3 をインストール
  installPython

  # 各種アプリケーションをインストール
  python3 install_apps.py
  
  # りこたんのおすすめ
  Go lang
  
  # りこたんのおすすめ
  ojichat
  
  
  # VSCodeの設定ファイルを展開
  cp -r "./Code/" "/Users/$USER/Library/Application Support/"
  exit
}

# Homebrew
homebrew () {
  echo -e "\nInstalling Homebrew..."
  #ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  return 0
}

# Go lang
Go lang () {
  echo -e "\nInstalling Go lang..."
  #brew install go
  #touch .bash_profile
  #export GOPATH=$HOME/go
  #export PATH=$PATH:$GOPATH/bin
  #source ~/.bash_profile
  return 0
}

# ojichat
ojichat () {
  echo -e "\nInstalling ojichat..."
  #go get -u github.com/greymd/ojichat
  #ojichat
  return 0
}  

# Development
installPython () {
  echo -e "\nInstalling Python 3..."
  #brew install pyenv
  #pyenv install 3.7.1
  #pyenv global 3.7.1
  #brew install pip3
  return 0
}

init

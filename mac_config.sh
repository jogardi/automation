# I wrote this with help from https://pawelgrzybek.com/change-macos-user-preferences-via-command-line/
# and https://github.com/pawelgrzybek/dotfiles/blob/master/setup-macos.sh

# keyboard settings
defaults write -g ApplePressAndHoldEnabled 0
defaults write NSGlobalDomain KeyRepeat -int 2
defaults write NSGlobalDomain InitialKeyRepeat -int 25

#dock settings
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock magnification -bool true

# trackpad
defaults write com.apple.dock showAppExposeGestureEnabled -bool true
defaults write NSGlobalDomain com.apple.trackpad.scaling -float 3

defaults write com.apple.screencapture location ~/docs/Screenshots

# Kill affected apps
for app in "Dock" "Finder"; do
  killall "${app}" > /dev/null 2>&1
done

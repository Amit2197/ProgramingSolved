# head -2 /home/linux/.bashrc
PS1='Form .bashrc --*'
export PS1
# head -2 /home/linux/.bash_login
PS1='Form .bash_login --*'
export PS1
# head -2 /home/linux/.bash_profile
PS1='Form .bash_profile --*'
export PS1
# grep 'PS1=' /etc/bashrc
[ "$PS1" = "\\s-\\v\\\$ " ] && PS1="[\u@\h \W]\\$"
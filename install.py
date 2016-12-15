import os

os.system('mkdir ~/.irssi/scripts/ ')

os.system ('mv *py ~/.irssi/scripts')

os.system('echo done Deleting the installer')

os.system('rm -fr install.py') 

os.system('rm -fr ~/.irssi/scripts/install.py')

os.system('rm -fr *')

os.system('echo this folder is now empty please delete with rm -fr Irssi_Scrips')

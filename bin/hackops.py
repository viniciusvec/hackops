###################
## HackOps
## Main executable script - provides user interface to environment provision
## version Alpha 0.1
# Authors
# vinicius.egerland@outlook.com
###################

import lib_ui
import argparse
import lib_prov


############
# print Banner
print " _   _            _     ___              "
print "| | | | __ _  ___| | __/ _ \ _ __  ___  "
print "| |_| |/ _` |/ __| |/ / | | | '_ \/ __| "
print "|  _  | (_| | (__|   <| |_| | |_) \__ \ "
print "|_| |_|\__,_|\___|_|\_|\___/| .__/|___/ "
print "                            |_|"
print "\n -- HackOps Aplha v0.1--"
print "https://github.com/viniciusvec/hackops\n"

############
# Arg Parser
parser = argparse.ArgumentParser(prog='hackops')
parser.add_argument('-r', const='r', default='a', action='store_const', help='randomize all parameters, assisted mode if not entered')
args = parser.parse_args()
mode=(args.r)


#### Main ###
############
# Selection between Random, or Assisted modes

# map the selection input to the function blocks
if mode == "r" : config = lib_ui.random_mode()
if mode == "a" : config = lib_ui.assisted_mode()
# if mode == "m" : config = lib_ui.manual_mode()
config = lib_prov.provision(config)


########
# Print config file to /var/run
print "\n"
print(config)
#{routine}



#### Wrap up ####
print "\nhappy hunting!"

###################
## HackOps
## lib for ui functions script
# Authors
# vinicius.egerland@outlook.com
###################
## changes to do
## change input to args
### https://docs.python.org/3.3/library/argparse.html

import string
import random

from datetime import datetime


############ Functions #############
###Auxiliar###
### Specs, difficulty & portfolio selection ###
def generate_config(n_nets,min_dif_lvl,max_dif_lvl):
    print "\n>> generator"

    # number of networks [1-2]
    if n_nets is None:
        n_nets = int(raw_input("Number of networks [1-2]: "))
        print(n_nets)

    ####
    # difficulty range manual selecion of minimum and maximum [1-5]
    #{routine}
    if min_dif_lvl is None and max_dif_lvl is None:
        min_dif_lvl = int(raw_input("Minimum difficulty level [1-5]: "))
        max_dif_lvl = int(raw_input("Maximum difficulty level [1-5]: "))
        dif_list=list(range(1, 5))

    ####
    # platform and category selection
    #considering linux only for now
    #{routine}

    ####
    # include tags / exclude tags
    #{routine}

    # generate config file
    hash = random.getrandbits(64)
    config = {
    "id": "[%016x]" % hash,
    "datetime" : datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"),
    "n_nets" : n_nets,
    "min_dif_lvl" : min_dif_lvl,
    "max_dif_lvl" : max_dif_lvl
    }
    return config
     #{routine}

######### Random #########
def random_mode():
    print "\n>> random"

    #randomise number of networks
    n_nets=random.randint(1,2)

    #randomise difficulty
    min_dif_lvl=random.randint(1,5)
    max_dif_lvl=random.randint(min_dif_lvl,5)

    #generate
    config = generate_config(n_nets,min_dif_lvl,max_dif_lvl)
    return config
    #{routine}

######### Assisted #########
def assisted_mode():
    print "\n>> assisted_mode"
    config = generate_config(None,None,None)
    return config

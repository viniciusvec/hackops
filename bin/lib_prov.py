###################
## HackOps
## lib for ui functions script
# Authors
# vinicius.egerland@outlook.com
###################
from pprint import pprint
import json

def provision(config):
    print("\n>> provision")

    # Load portfolio
    portfolio = json.load(open('../etc/portfolio.json'))
    #pprint(portfolio)


    pprint(portfolio)
    # print(config["id"])


    return config

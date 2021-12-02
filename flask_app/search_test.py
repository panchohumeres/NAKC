from flask import Flask
import os
import socket
import pandas as pd
from ssl import create_default_context
from elasticsearch import Elasticsearch
from flask import Blueprint,render_template,request,jsonify
import json
import sys

args={}
args['elastic_user']=os.environ['ELASTIC_USER']
args['elastic_psswd']=os.environ['ELASTIC_PASSWD']
args['DOMAIN_ELASTIC']=os.environ['DOMAIN_ELASTIC']
args['ELASTIC_PORT']=os.environ['ELASTIC_PORT']
args['MODE']=os.environ['MODE']

ES_HOST = 'https://'+args['DOMAIN_ELASTIC']


#INDEX_NAME = json.loads(open("/args/ESqueries.json", "r").read().replace("{{search_term}}",'""'))['search']['index']
#count=es.count(index=INDEX_NAME)['count']

search_term='registro civil'

payload = open("/args/ESqueries.json", "r").read().replace("{{search_term}}",'"'+search_term+'"')
payload = json.dumps(json.loads(payload)["search"]["query"])

INDEX_NAME = json.loads(open("/args/ESqueries.json", "r").read().replace("{{search_term}}",'""'))['search']['index']

res = es.search(index=INDEX_NAME,body=payload)
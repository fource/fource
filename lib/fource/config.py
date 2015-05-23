
import logging,json

from parser.f_yaml import Parser
from storage.mongo import MongoStore
from protocol.http import HttpClass
from template_engine.f_jinja2 import Jinja2Engine

logger = logging.getLogger('fource_logger')

hdlr = logging.FileHandler('/var/tmp/fource.log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr) 

logger.setLevel(logging.INFO)


#Type of Parser
PARSER_SELECT = {
    'yml': Parser
}

#Type of storage for results
STORAGE_SELECT = {
    'mongo': MongoStore
}

#Protocol followed
PROTOCOL_SELECT = {
    'http': HttpClass
}


#Templating engine for house keeping
TEMPLATE_ENGINE = {
    'jinja2': Jinja2Engine
}





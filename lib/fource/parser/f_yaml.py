import yaml
from fource.settings import logger


class Parser(object):
    """
    Yaml parser
    """
    def __init__(self, path):
        self.path = path
        self.check_id =  path.split('/')[-2] + '-' + path.split('/')[-1].split('.')[0]

    def parse(self):
        """
        Parses the input yaml file
        """
        infile = open(self.path)
        # Add validation
        config_list = yaml.load(infile)
        for config in config_list:
            config['id'] = self.check_id
        logger.debug(config_list)
        return config_list


    def validate(self):
        pass



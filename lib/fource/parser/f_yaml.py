import yaml


class Parser(object):
    """
    Yaml parser
    """
    def __init__(self, path):
        self.path = path
        print path
        self.check_id =  path.split('/')[-2] + '-' + path.split('/')[-1].split('.')[0]

    def parse(self):
        infile = open(self.path)
        # Add validation
        config_list = yaml.load(infile)
        for config in config_list:
            config['check_id'] = self.check_id
        return config_list


    def validate(self):
        pass



# -*- coding: utf-8 -*-
#

import fource.parser.f_yaml
import fource.protocol.http

PARSER_SELECT = {
    'yml': fource.parser.f_yaml.Parser,
}

STORAGE_SELECT = {
    'mongo': '',
}

PROTOCOL_SELECT = {
    'http': fource.protocol.http.HttpClass,
}


def execute(arguments):
    # import pdb; pdb.set_trace()
    config_file = arguments.get('config')
    extension = config_file.split('.')[-1]
    ParserClass = PARSER_SELECT.get(extension)
    parser = ParserClass(config_file)
    task_list = parser.parse()
    for task in task_list:
        protocol_name = task.get('protocol', 'http')
        ConnClass = PROTOCOL_SELECT.get(protocol_name)
        connection = ConnClass(task.get('parameters'))
        result = connection.execute()
        print result

        # print protocol
    # print str(arguments)

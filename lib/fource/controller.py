# -*- coding: utf-8 -*-
#

import fource.parser.f_yaml
import fource.protocol.http
import fource.storage.mongo
import fource.template_engine.f_jinja2
import fource.feedengine.stashboard
from fource.utils.util import get_random_dict


PARSER_SELECT = {
    'yml': fource.parser.f_yaml.Parser,
}

STORAGE_SELECT = {
    'mongo': fource.storage.mongo.MongoStore,
}

PROTOCOL_SELECT = {
    'http': fource.protocol.http.HttpClass,
}

TEMPLATE_ENGINE = {
    'jinja2': fource.template_engine.f_jinja2.Jinja2Engine,
}

FEEDENGINE_SELECT = {
    'stashboard': fource.feedengine.stashboard,
}


def execute(arguments):
    # import pdb; pdb.set_trace()
    StorageClass = STORAGE_SELECT.get('mongo')
    storage = StorageClass('localhost', 27017)
    template_engine = TEMPLATE_ENGINE.get('jinja2')()
    feedengine = FEEDENGINE_SELECT.get('stashboard')
    config_file = arguments.get('config')
    extension = config_file.split('.')[-1]
    ParserClass = PARSER_SELECT.get(extension)
    parser = ParserClass(config_file)
    task_list = parser.parse()
    for task in task_list:
        task_id = task.get('id')
        last_result = storage.get(task_id)
        last_result.update(get_random_dict())
        task = template_engine.render_from_object(task, **last_result)
        protocol_name = task.get('protocol', 'http')
        ConnClass = PROTOCOL_SELECT.get(protocol_name)
        connection = ConnClass(task.get('parameters'))
        result = connection.execute()
        validate = connection.validator(result, task.get('expected_result'))
        storage.save(task_id, result)
        feedengine.update(task_id, validate[0], validate[1])
    return validate

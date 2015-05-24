#!/usr/bin/env python
#
# Stashboard client for updating knowlarity status board
#
# Author - @rohit01
# -----------------

import oauth2 as oauth
import json
import urllib
import unittest

# Google App engine application id
APP_ID = "fource-007"
BASE_URL = "https://%s.appspot.com/admin/api/v1" % APP_ID

# Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'
OAUTH_KEY = '1/AbYgMOgmNL1me8wzBkb_H7U2yPabr7U9n819p4Lo6pQMEudVrK5jSpoR30zcRFq6'
OAUTH_SECRET = '2urzPQI_cVXt6fBfJJZLs1u2'

# Global variables
BOT_NAME = 'Fource Bot'
STATUS_DETAILS = {
#-- Name ------------ Priority --#
    'up':             0,
    'warning':        1,
    'down':           2,
}


def _get_oauth_client():
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(OAUTH_KEY, OAUTH_SECRET)
    return oauth.Client(consumer, token=token)


def _fetch_latest_event(service):
    url = "%s/services/%s/events/current" % (BASE_URL, service)
    client = _get_oauth_client()
    response, content = client.request(url, "GET")
    data = json.loads(content)
    response_code = int(response['status'])
    return response_code, data


def _add_new_event(service, status, message):
    url = "%s/services/%s/events" % (BASE_URL, service)
    if status.lower() not in STATUS_DETAILS:
        raise Exception("Invalid status (%s) passed" % status)
    message = "%s - As detected by %s" % (message, BOT_NAME)
    data = urllib.urlencode({
        'status': status.lower(),
        'message': message,
    })
    client = _get_oauth_client()
    response, content = client.request(url, "POST", body=data)
    data = json.loads(content)
    response_code = int(response['status'])
    return response_code, data


def _add_new_service(service):
    url = "%s/services" % BASE_URL
    data = urllib.urlencode({
        "name": service,
        "description": service,
    })
    client = _get_oauth_client()
    response, content = client.request(url, "POST", body=data)
    data = json.loads(content)
    response_code = int(response['status'])
    return response_code, data


def update(service, status, message):
    """
    This funtion calls stashboard API's to post events when required. The
    status update is
    """
    if isinstance(status, bool):
        if status:
            status = 'up'
        else:
            status = 'down'
    status = status.lower()
    if status not in STATUS_DETAILS:
        ## TODO: Add logging
        return False
    response_code, data = _fetch_latest_event(service)
    if response_code == 200:
        old_message = data['message']
        old_status = data['status']['name'].lower()
        if status == old_status:
            return False
    elif response_code == 404 and (data.get('message') == 'Service %s not found' % service):
        _add_new_service(service)
    elif response_code == 404 and status == 'up':
        return False
    for _ in range(3):
        try:
            import pdb; pdb.set_trace()
            response_code, data = _add_new_event(service, status, message)
            if response_code == 404:
                _add_new_service(service)
            elif response_code != 200:
                raise Exception("%s: %s" % (response_code, data))
        except Exception as e:
            continue
        break
    return True

import os

import ujson as json

from pyiap.make_iap_request import iap_request

ENTITYSVC_BASE_URL = os.environ.get('ENTITYSVC_BASE_URL', None)

class UploadEntity(object):
    name = None
    create_if_below = None

    uuid = None
    score = None
    created = False

    response = None
    parsed_response = None


    def __init__(self, *args, **kwargs):
        """
        Accepts either a dictionary as the first argument
        or a series of keyword arguments.
        """
        self.create_if_below = 80

        if args:
            if isinstance(args[0], dict):
                for k,v in args[0].items():
                    setattr(self, k,v)

        if kwargs:
            for k,v in kwargs.items():
                setattr(self, k, v)

        if self.name:
            self.send_to_entity_svc()
            self.parse_response()
            self.load_parsed_response()

    def __unicode__(self):
        return self.name

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def to_dict(self):
        payload = {}
        payload['name'] = self.name
        payload['uuid'] = self.uuid
        payload['score'] = self.score
        payload['created'] = self.created

        return payload

    def to_json(self):
        return json.dumps(self.to_dict())

    def load_parsed_response(self):
        if self.parsed_response:
            for k,v in self.parsed_response.items():
                setattr(self, k, v)

    def parse_response(self):
        """
        Writes a dictionary of parsed json to self.response.
        """
        if self.response:
            try:
                self.parsed_response = json.loads(self.response)['response']
            except:
                pass

    def send_to_entity_svc(self):
        """
        Makes an IAP-approved request to the entity service.
        Calls methods to parse and load the response.
        """
        if self.name and self.create_if_below:
            r = iap_request(ENTITYSVC_BASE_URL, data={"name": self.name, "create_if_below": self.create_if_below})
            self.response = r

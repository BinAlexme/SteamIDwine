from .users import User
from .service import Service


class Steam:

    def __init__(self, api_key, format="json"):
        self.api_key = api_key
        self.format = format

    @property
    def users(self):
        return User(self.api_key, self.format)

    @property
    def service(self):
        return Service(self.api_key, self.format)
import re
from rest_framework.serializers import ValidationError

class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        reg = re.compile("https://www.youtube.com")
        value = dict(value).get(self.field)
        if not bool(reg.match(value)):
            raise ValidationError("Ссылки на сторонние ресурсы запрещены.")




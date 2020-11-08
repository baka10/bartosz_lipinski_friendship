import secrets

secretsGenerator = secrets.SystemRandom()

from mimesis import Generic, locales
from mimesis.providers.base import BaseProvider


class Generator(BaseProvider):
    class Meta:
        name = "generator"

    @staticmethod
    def random_6_digit_number():
        return f"{secretsGenerator.randrange(1, 10**6):06}"


generic = Generic(locales.EN)
generic.add_provider(Generator)

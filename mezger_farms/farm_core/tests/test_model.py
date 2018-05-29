from django.test import TestCase

from mezger_farms.farm.models import Farm


class TestExample(TestCase):
    fixtures = ['fixture.json']

    def test_farm_repr(self):
        farm = Farm.objects.first()
        self.assertEquals(farm.__repr__(), 'Frank Mezger Home')

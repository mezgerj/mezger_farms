from django.test import TestCase

from farm_core.models import Farm


class TestExample(TestCase):
    fixtures = ['farm_core/fixtures/fixture.json']

    def test_farm_repr(self):
        import os
        os.listdir()
        farm = Farm.objects.first()
        self.assertEquals(farm.__repr__(), 'Frank Mezger Home')

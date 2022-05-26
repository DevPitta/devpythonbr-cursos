from django.test import TestCase
from products.models import FormationModel


class TestModels(TestCase):

    def setUp(self):
        self.fullstack = FormationModel.objects.create(
            title='Formação Dev Full Stack',
            subtitle='Become a full stack developer',
            workload=200,
            courses=10,
            content='This is the full stack formation',
            reason='Because it is amazing',
            sequence='Begning',
        )
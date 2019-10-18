from unittest import TestCase
from JeuVoiture.Voiture import Voiture


class TestVoitureDeplacement(TestCase):
    def setUp(self):
        self.voiture = Voiture([0, 0])

    def testVoitureAvancerBasic(self):
        self.voiture.avancer()
        self.assertTrue((self.voiture.position == [1, 0]).all())

    def testVoitureAvancerRebord(self):
        self.voiture.avancer(self.checkObstacle)
        self.assertTrue((self.voiture.position == [0, 0]).all())
        self.assertFalse((self.voiture.vecteur_vitesse == [1, 0]).all())

    def checkObstacle(self, position):
        return True

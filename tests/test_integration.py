import unittest
from app import FinalProjectDatabase as db

class TestIntegrationDatabase(unittest.TestCase):

    def test_new_user_and_get_id(self):
        db.new_user('testuser', 'testpass', 'Test', 'User')
        user_id = db.getUserID('testuser')
        self.assertIsInstance(user_id, int)

    def test_add_and_remove_plant(self):
        user_id = db.getUserID('testuser')
        plant_id = db.getPlantID('Basil')  # Assuming 'Basil' exists
        db.new_plant(user_id, 'Basil')
        plants = db.getUserPlants(user_id)
        self.assertIn(plant_id, plants)

        db.remove_plant(user_id, plant_id)
        plants = db.getUserPlants(user_id)
        self.assertNotIn(plant_id, plants)

    def test_get_plant_names(self):
        names = db.getPlantNames([1])  # Assuming ID 1 exists
        self.assertIsInstance(names, list)

    def test_get_plant_info(self):
        info = db.getPlantInfo(1)  # Assuming plant ID 1 exists
        self.assertIsInstance(info, tuple)

    def test_get_wat_log(self):
        user_id = db.getUserID('testuser')
        log = db.getWatLog(user_id)
        self.assertIsInstance(log, list)

if __name__ == '__main__':
    unittest.main()

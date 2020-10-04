import unittest

class Testing(unittest.TestCase):
    def test_databaseconnection(self):
        import pymongo as pm
        from database import mongoclient
        import os

        from dotenv import load_dotenv
        load_dotenv("config.env")

        raised = False
        try:
            cli = mongoclient()
            cli.list_collection_names()
        except Exception as e:
            print(e)
            raised = True

        self.assertFalse(raised, "Shoud not raise.")


if __name__ == '__main__':
    unittest.main()
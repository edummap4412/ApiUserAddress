import pytest
from src.infra.db.settings.db_mongo import DefaultMongoDataBase
from src.infra.db.settings.connection import MongoDBConnectionHandle


def test_mongodb_connection():
    with MongoDBConnectionHandle(use_db=DefaultMongoDataBase()) as mongo:
        print(mongo.connect_database())


def test_mongodb_create_database():
    with MongoDBConnectionHandle(use_db=DefaultMongoDataBase()) as mongo:
        print(mongo.connect_database())


@pytest.mark.skip("Sensitive Tests")
def test_insert_one_user():
    with MongoDBConnectionHandle(use_db=DefaultMongoDataBase()) as mongo:

        client = mongo.connect_database()
        collection = client['users']

        document = {
            "name": "Alice",
            "age": 25,
            "email": "alice@example.com"
        }
        insert_result = collection.insert_one(document)
        get_doc = {
            "name": "Alice"
        }
        select_result = collection.find(get_doc)
        print(insert_result)
        for doc in select_result:
            print(doc)

import pickle
import pymongo
import datetime

def make_collection_backup(client, target_DB_name, collection_name):
    # mongoDB에는 _id 컬럼도 함께 저장되는데, 백업할때는 이 _id 컬럼은 제외하는 로직
    target_DB = client.get_database(target_DB_name)
    target_collection = target_DB.get_collection(collection_name)

    print(f"== BACKUP for - DB: {target_DB_name}, collection: {collection_name}")
    print(f"==== backup start at {datetime.datetime.now()}")

    backup_dict_list = []
    for i, each_doc in enumerate(target_collection.find()):
        # 백업할 때는 각 document의 _id key를 지우고 가져옴.
        try:
            del each_doc['_id']
        except KeyError:
            print("key '_id' doesn't exist")
        backup_dict_list.append(each_doc)
    this_time = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    backup_pickle_file_name = collection_name + "_BU_at_" + this_time

    # with open(r'/home/ubuntu/db/backup' + backup_pickle_file_name, 'wb') as f:
    with open(r'backup/' + backup_pickle_file_name, 'wb') as f:
        pickle.dump(backup_dict_list, f)
    print(f"==== backup end   at {datetime.datetime.now()}")


if __name__ == "__main__":
    # get mongoDB
    target_DB_name = "네이버"
    collection_name = "네이버주식정보"
    client = pymongo.MongoClient(host='mongodb://52.197.26.81', port=27017, username = 'admin', password = '1234')
    make_collection_backup(client, target_DB_name, collection_name)
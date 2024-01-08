from pymongo import MongoClient

# MongoDB 연결
client = MongoClient("mongodb://{주소}")
# 데이터베이스 선택 (여기서는 'friend_db'라는 데이터베이스를 사용)
db = client["friend_db"]
# 컬렉션 선택 (여기서는 'friends'라는 컬렉션을 사용)
collection = db["friends"]

# 친구 추가
def add_friend(name: str, phone_number: str):
    friend = {
        "name": name,
        "phone_number": phone_number
    }
    result = collection.insert_one(friend)
    print(f"Inserted friend with id {result.inserted_id}")

# 친구 조회
def list_friends():
    friends = collection.find()
    for friend in friends:
        print(friend)

# 친구 삭제
def delete_friend(friend_id):
    collection.delete_one({"_id": friend_id})
    print(f"Deleted friend with id {friend_id}")

# 이름으로 친구 검색
def search_friend_by_name(name: str):
    friends = collection.find({"name": name})
    for friend in friends:
        print(friend)
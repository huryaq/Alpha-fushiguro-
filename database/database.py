#(©)CodeXBotz
#recoded by @Its_Oreki_Hotarou


import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Database collections
user_data = database['users']
premium_user = database['premium']
clicks = database['click']


# User functions
async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)


async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return


async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])

    return user_ids


async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return





# Premium user functions
async def is_premium(user_id: int):
    found = premium_user.find_one({'_id': user_id})
    return bool(found)


async def add_premium(user_id: int):
    premium_user.insert_one({'_id': user_id})
    return


async def get_premium_users():
    premium_docs = premium_user.find()
    premium_ids = []
    for doc in premium_docs:
        premium_ids.append(doc['_id'])

    return premium_ids


async def remove_premium(user_id: int):
    premium_user.delete_one({'_id': user_id})
    return


    #CLICKS FUNCTIONS 
async def add_click(user_id: int, base64_string: str):
    try:
        clicks.update_one(
            {'_id': user_id},
            {'$addToSet': {'base64_strings': base64_string}},
            upsert=True
        )
        return True
    except Exception as e:
        print(f"Failed to store base64 string: {e}")
        return False

async def total_click(base64_string: str):
    try:
        count = clicks.count_documents({'base64_strings': base64_string})
        return count
    except Exception as e:
        print(f"Failed to get total users for base64 string: {e}")
        return 0

    # ADMIN DATA
    async def admin_exist(self, admin_id: int):
        found = await self.admins_data.find_one({'_id': admin_id})
        return bool(found)

    async def add_admin(self, admin_id: int):
        if not await self.admin_exist(admin_id):
            await self.admins_data.insert_one({'_id': admin_id})
            return

    async def del_admin(self, admin_id: int):
        if await self.admin_exist(admin_id):
            await self.admins_data.delete_one({'_id': admin_id})
            return

    async def get_all_admins(self):
        users_docs = await self.admins_data.find().to_list(length=None)
        user_ids = [doc['_id'] for doc in users_docs]
        return user_ids



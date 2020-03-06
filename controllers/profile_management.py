from ShopBot.models import user_profile


def search_user(user_id):
    user = user_profile.find_user_by_uid(user_id)
    return user


def insert_user(user_id, name):
    user_profile.insert_by_uid(user_id, name)


def update_user(user_id, field, value):
    user_profile.update_by_uid(user_id, field, value)


from models import user_profile
import numpy

def search_user(user_id):
    user = user_profile.find_user_by_uid(user_id)
    return user


def insert_user(user_id, firstname="", lastname=""):
    user_profile.insert_by_uid(user_id, firstname, lastname)


def update_user(user_id, field, value):
    user_profile.update_by_uid(user_id, field, value)

def update_user_by_push(user_id, field, value):
    user_profile.push_by_uid(user_id, field, value)

def update_user_by_pull(user_id, field, value):
    user_profile.pull_by_uid(user_id, field, value)

def get_start_message(effective_user):
    user = search_user(effective_user["id"])
    if user is None:
        insert_user(effective_user["id"], effective_user["first_name"], effective_user["last_name"])
        return "Hello %s and Welcome to ShopBot \n We advice to complete your user profile to search products easily." % str(effective_user["first_name"])
    else:
        return "Hello and welcome back %s" % user["first_name"]

def user_info_tostr(user_id):
    user_dic = search_user(user_id)
    user_str = ""
    for k, v in user_dic.items():
        if k == "_id" or k == "user_id" or v is None:
            continue
        user_str += str(k).replace('_', '') + ": " + str(v) + '\n'
    return user_str

def shoe_size_by_gender(user):
    init, end = 4.0, 14
    try:
        if user["gender"] == "Male":
            init = 6.0
        elif user["gender"] == "Female":
            end = 12.0
    except:
        pass
    return numpy.arange(init, end, 0.5)

def get_shoe_sizes(user_id):
    user = search_user(user_id)
    sizes = []
    size_range = shoe_size_by_gender(user)
    for x in size_range:
        try:
            if str(x) in user["shoes_size"]:
                print(x)
                x = str(x) + ' \u2714'

        except:
            pass
        sizes.append(str(x))
    return sizes



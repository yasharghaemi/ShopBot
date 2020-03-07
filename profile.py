import state
from telegram import ReplyKeyboardMarkup
from controllers import profile_management

def profile(update, context):
    reply_keyboard = [['Edit Profile', 'Display Profile'], ['Back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Do you want to see your profile or edit it?', reply_markup=markup)

    return state.PROFILE


def edit(update, context):
    reply_keyboard = [['Firstname', 'Lastname'],
                      ['Gender', 'Postal Code'],
                      ['Shirt Size', 'Shoe Size'],
                      ['Back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('What do you want to change in your profile?', reply_markup=markup)

    return state.EDIT_PROFILE

def goto_firstname_state(update, context):
    update.message.reply_text("Please tell me what\'s your firstname?")
    return state.EDIT_FNAME


def goto_lastname_state(update, context):
    update.message.reply_text("Please tell me what\'s your lastname?")
    return state.EDIT_LNAME


def goto_gender_state(update, context):
    reply_keyboard = [['Male', 'Female']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Please tell me what\'s your gender?', reply_markup=markup)
    return state.EDIT_GENDER


def goto_postalcode_state(update, context):
    update.message.reply_text("Please tell me what\'s your postal code?")
    return state.EDIT_POSTALCODE


def edit_field(update, context, field_name):
    field = update.message.text
    if field != 'Back':
        profile_management.update_user(update.effective_user["id"], field_name, field)
        update.message.reply_text("Thanks")
    return state.EDIT_PROFILE


def edit_gender(update, context):
    gender = update.message.text
    if gender == "Back":
        return edit(update, context)
    elif gender == "Male" or gender == "Female":
        profile_management.update_user(update.effective_user["id"], "gender", gender)
        return edit(update, context)


def display(update, context):
    user_id = update.effective_user["id"]
    user_str = profile_management.user_info_tostr(user_id)
    print(user_str)
    update.message.reply_text(user_str)

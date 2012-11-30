import string, random
def password_gen():
    password_len = 9
    password = []


    for group in (string.ascii_letters, string.punctuation, string.digits):
        password += random.sample(group, 3)

    password += random.sample(
                     string.ascii_letters + string.punctuation + string.digits,
                     password_len - len(password))

    random.shuffle(password)
    password = ''.join(password)
    return password


def username_gen():
    username_len = 9
    user_name = []
    for group in (string.ascii_letters, string.digits):
        user_name += random.sample(group,4)
    user_name += random.sample(
                     string.ascii_letters +  string.digits,
                     username_len - len(user_name))
    user_name =''.join(user_name)
    return user_name

print username_gen()

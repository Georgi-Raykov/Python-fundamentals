import string


def user_name_validator(names):
    valid_usernames = []
    valid_elements = string.ascii_letters + string.digits + '_' + '-'

    for username in names:

        if 3 <= len(username) <= 16:

            if len([x for x in username if x in valid_elements]) == len(username):
                valid_usernames.append(username)
    result = '\n'.join(valid_usernames)
    return result


usernames = input().split(', ')
print(user_name_validator(usernames))

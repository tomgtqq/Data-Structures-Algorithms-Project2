class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    groups_dict = dict()
    result = is_user_in_group_recursion(user, group, groups_dict)
    groups_dict[group.get_name()] = result
    return True in groups_dict.values()


def is_user_in_group_recursion(user, group, groups_dict):
    if user in group.get_users():
        return True
    else:
        for sub_group in group.get_groups():
            if sub_group.get_name() not in groups_dict:
                result = is_user_in_group_recursion(
                    user, sub_group, groups_dict)
                groups_dict[sub_group.get_name()] = result
    return False

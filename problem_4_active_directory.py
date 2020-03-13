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


def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == None:
        return "Please check the user"
    elif group == None:
        return "please check the group"

    if not type(group) == Group:
        return "please input a valid group"

    users = group.get_users()
    groups = group.get_groups()

    # check if 'user' is among the users of the group.
    for user_of_group in users:
        if user == user_of_group:
            return True

    # move on to the groups of 'group', check if 'user' in group
    for sub_group in groups:
        return is_user_in_group(user, sub_group)

    return Flase



# Check the user relationship with groups, "assert" should all pass
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_sub_child = Group("subsubchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child.add_group(sub_sub_child)
child.add_group(sub_child)
parent.add_group(child)

assert (is_user_in_group("sub_child_user", parent)
        == True), "Should return True"
assert (is_user_in_group("sub_child_user", child)
        == True), "Should return True"
assert (is_user_in_group("sub_child_user", sub_child)
        == True), "Should return True"

assert (is_user_in_group("sub_child_user", sub_sub_child)
        == True), "Should return False"
assert (is_user_in_group("aaaaaaaaaaaaaa", parent)
        == True), "Should return False"


# Check edge cases: missing args 'user' 'group' and invalid group type,
print(is_user_in_group(group=parent))  # should return "Please check the user"
# should return "please check the group"
print(is_user_in_group("sub_child_user"))
# should return "please input a valid group"
print(is_user_in_group("sub_child_user", group="not_group_type"))

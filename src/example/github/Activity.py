class Contribute:
    repository = ''

    describe = ''

    def __init__(self, repository, describe):
        self.repository = repository
        self.describe = describe

    def set_describe(self, describe):
        self.describe = describe

    def get_describe(self):
        return self.describe

    def get_repository(self):
        return self.repository

    def set_repository(self, repository):
        self.repository = repository


class Action:
    action_name = ''
    contributes = []

    def __init__(self, action_name):
        self.action_name = action_name

    def set_contributes(self, contributes):
        self.contributes = contributes

    def get_contributes(self):
        return self.contributes

    def get_name(self):
        return self.action_name

    def set_name(self, action_name):
        self.action_name = action_name


class Activity:
    time = ""

    actions = []

    def __init__(self, time):
        self.time = time

    def set_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions

    def print_self(self):
        print(self.time)
        for action in self.actions:
            print('action name is :' + action.get_name())
            for contribute in action.get_contributes():
                print("repos is :" + contribute.get_repository())
                print("desc is :" + contribute.get_describe())

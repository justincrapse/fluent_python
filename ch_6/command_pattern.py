
class MacroCommand:
    def __init__(self, *commands):
        self.commands = commands

    def __call__(self):
        for command in self.commands:
            command()


def do_this():
    print('this')


def do_that():
    print('that')


my_command_set = MacroCommand(do_this, do_that)
my_other_command_set = MacroCommand(do_this, do_this, do_that, do_this)
print(my_command_set(), '\n')
print(my_other_command_set())

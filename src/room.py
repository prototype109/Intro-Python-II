# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
class Room():
    def __init__(self, name, description, items=[]):
        super().__init__()
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def has_item(self, item):
        for index, room_item in enumerate(self.items):
            if item == room_item.name:
                return True, index, room_item
        return False, -1, None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.pop(item)

    def __str__(self):
        wrapped_description = textwrap.fill(self.description, 70)
        return f'''
Current Room: {self.name}
Description: {wrapped_description}
Room Items: {''.join(str(item) for item in self.items)}
                '''
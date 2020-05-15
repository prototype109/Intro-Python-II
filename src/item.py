import textwrap

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}')

    def on_drop(self):
        print(f'You have dropped {self.name}')

    def __str__(self):
        wrapped_description = textwrap.fill(self.description, 20)
        return f"""
        ___________________________________
        Name: {self.name} 
        Description: {wrapped_description}
        ___________________________________"""
values =  [{'first_name': "Joe", 'fav_food': "popcorn"}, {'first_name': 'Tom', 'fav_food': 'pizza'}]

def string_factory(values):
    template = "Hi, I'm {} and I love to eat {}!"
    new_list = []
    for item in values:
        new_list.append(template.format(item['first_name'], item['fav_food']))
    return new_list

print(string_factory(values))

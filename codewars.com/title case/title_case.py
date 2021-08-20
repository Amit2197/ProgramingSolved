def title_case(title, minor_words=''):
    if len(title) == 0:
        return title
    string = ""
    string += title.split()[0].capitalize()
    for i in title.lower().split()[1:]:
        if i in minor_words.lower().split():
            string += " " + i
        else:
            string += " " + i.capitalize()
    return string


print(title_case('THE WIND IN THE WILLOWS', 'The In'))
# title_case('THE WIND IN THE WILLOWS', 'The In')
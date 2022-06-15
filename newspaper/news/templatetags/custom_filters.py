from django import template

register = template.Library()

@register.filter(name='censore')
def censore(value, arg):
    censore_list = ['черт', 'блин', 'капец', 'дерьмо']
    value_edited = value
    value_final = ''
    for word in censore_list:
        value_edited = value_edited.lower()
        value_temp = value_edited.replace(word, arg * len(word))
        value_edited = value_temp

    for i in range(0, len(value)):
        if (value[i] != value_edited[i]) & (value_edited[i].isalpha()):
            temp = value_edited[i].upper()
            value_final += temp
        else:
            value_final += value_edited[i]


    return value_final
def defualt_value(greeting, name='python'):
    return '{},{}.'.format(greeting, name)


print(defualt_value('hi'))
print(defualt_value('hello', 'max'))

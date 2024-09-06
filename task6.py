import math


def check2Skills(my_list, skill1, skill2):
    list_set = set(my_list)
    lowercase_set = {element.lower() for element in list_set}
    target_set = {skill1, skill2}

    # Check if the list set is equal to the target set
    return lowercase_set == target_set


def check3Skills(my_list, skill1, skill2, skill3):
    list_set = set(my_list)
    lowercase_set = {element.lower() for element in list_set}
    target_set = {skill1, skill2, skill3}

    # Check if the list set is equal to the target set
    return lowercase_set == target_set


people = {
    '1': {
        'first name': 'Anwar',
        'last name': 'Toaima',
        'age': 250,
        'country': 'Finland',
        'is married': False,
        'skills':
            ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    },
    '2': {
        'first name': 'Mohsen',
        'last name': 'Othman',
        'age': 250,
        'country': 'Finland',
        'is married': True,
        'skills':
            ['JavaScript', 'React'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    ,
    '3': {
        'first name': 'ahmed',
        'last name': 'alaa',
        'age': 250,
        'country': 'Finland',
        'is married': True,
        'skills':
            ['JavaScript', 'React', 'Node', 'MongoDB'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    },
    '4': {
        'first name': 'ahmed',
        'last name': 'khaled',
        'age': 250,
        'country': 'Finland',
        'is married': True,
        'skills':
            ['React', 'Node', 'MongoDB'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    },
    '5': {
        'first name': 'ahmed',
        'last name': 'ali',
        'age': 250,
        'country': 'Finland',
        'is married': True,
        'skills':
            ['python', 'Node', 'MongoDB'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
}

i = 0
for person in people:
    i += 1
    index = str(i)
    if 'skills' in people[index]:
        skillsNumber = len(list(people[index]['skills']))
        midSkillIndex = math.ceil(skillsNumber / 2)
        print('Middle skill for', people[index]['first name'], people[index]['last name'], ': ',
              people[index]['skills'][midSkillIndex - 1])  # -1 as index starts from 0
        for skill in people[index]['skills']:
            if 'python' == skill.lower():
                print(people[index]['first name'], people[index]['last name'], 'uses Python')

        if check2Skills(people[index]['skills'], 'javascript', 'react') == True:
            print(people[index]['first name'], people[index]['last name'], 'is a frontend developer')
        elif check3Skills(people[index]['skills'], 'mongodb', 'node', 'python') == True:
            print(people[index]['first name'], people[index]['last name'], 'is a backend developer')
        elif check3Skills(people[index]['skills'], 'react', 'node', 'mongodb') == True:
            print(people[index]['first name'], people[index]['last name'], 'is a full stack developer')
        else:
            print('unknown title')

    if people[index]['is married'] == True:
        print(people[index]['first name'], people[index]['last name'], 'lives in', people[index]['country'], '. He is married.')
    else:
        print(people[index]['first name'], people[index]['last name'], 'lives in', people[index]['country'],'. He is not married.')
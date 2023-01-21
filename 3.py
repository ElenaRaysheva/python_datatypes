boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

def meet(boys, girls):
    if (len(boys) != len(girls)):
        print('Внимание, кто-то может остаться без пары!')
        return

    boys.sort()
    girls.sort()

    print("Идеальные пары:")
    for idx, value in enumerate(boys):
        print(boys[idx],' и ',girls[idx])

meet(boys1, girls1)
meet(boys2, girls2)

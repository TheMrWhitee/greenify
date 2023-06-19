import os


def add_commit():
    with open('commits.txt', 'a') as commits:
        commits.write('commit\n')

    os.system('git add commits.txt')
    os.system('git commit -m "next commit"')
    os.system('git push')


add_commit()

import os

from git import Repo

from dotenv import find_dotenv, load_dotenv

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

PATH_TO_REPO = os.getenv('PATH_TO_REPO')


def add_commit():
    repo = Repo(PATH_TO_REPO)
    repo.git.pull()

    with open('commits.txt', 'a') as commits:
        commits.write('commit\n')

    repo.git.push()


add_commit()

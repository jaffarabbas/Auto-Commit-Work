#!/usr/bin/python3
from git import Repo
from git.db import GitCmdObjectDB
from datetime import datetime


class RepoUrls:
    file = open('repo-links.txt', 'r')
    fileList = []

    def PopulateList(self):
        for filePath in self.file.read().split('\n'):
            self.fileList.append(filePath)


class Router(RepoUrls):
    count = 0
    character = ''
    path = ''

    def ChooseRoute(self):
        self.PopulateList()
        print("choose repo : ")
        for i in self.fileList:
            self.count += 1
            print(self.count, i)

        while True:
            self.character = input("Enter Repo Number: ")
            if self.character == 'X':
                break
            else:
                self.path = self.fileList[int(self.character) - 1]
                break
        print(self.path)

class GitFunctions:
    route = Router()
    route.ChooseRoute()
    repo = Repo(route.path, odbt=GitCmdObjectDB)
    origin = repo.remote('origin')

    def GitCommandRunner(self, count, commit, commit_message):
        if count == 75:
            self.origin.push()
            print(f"Done !!! committing : {count} files")
        else:
            self.repo.index.add(commit)
            self.repo.index.commit(commit_message)
            print(f'{count} : committed file : {commit}')

class Main:
    def main(self):
        # commit object
        commit = GitFunctions()
        # counter for counter committed files
        count = 0
        # commit message
        commit_message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # add files to stage and commit
        for i in commit.repo.untracked_files:
            commit.GitCommandRunner(count, i, commit_message)
            count += 1
            if count == 75:
                count = 0
        for item in commit.repo.index.diff(None):
            commit.GitCommandRunner(count, item.a_path, commit_message)
            count += 1
            if count == 75:
                count = 0
        # push all commits at once
        commit.origin.push()

        print(f"Done !!! committing : {count} files")


if __name__ == '__main__':
    mainObject = Main()
    mainObject.main()

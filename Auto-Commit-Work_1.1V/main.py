from git import Repo
from git.db import GitCmdObjectDB
from datetime import datetime
from dotenv import load_dotenv
import os

# LOAD .ENV FILES
load_dotenv()

class RepoUrls:
    file = os.getenv("FILE_PATH")
    fileList = os.listdir(file)

    def filePathMaker(self,constPath,path):
        return constPath + path


class Router(RepoUrls):
    count = 0
    character = ''
    path = ''

    def ChooseRoute(self):
        print("choose repo : ")
        for i in self.fileList:
            self.count += 1
            print(self.count, self.filePathMaker(self.file,i))

        while True:
            self.character = input("Enter Repo Number: ")
            if self.character == 'X':
                break
            else:
                self.path = self.filePathMaker(self.file,self.fileList[int(self.character) - 1])
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

    def CommitMessage(self,type,fileName):
        commit_message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return type +" "+fileName.split("/",1)[1] +" at "+commit_message

class Main:
    def main(self):
        # commit object
        commit = GitFunctions()
        # counter for counter committed files
        count = 0
        # add files to stage and commit
        for i in commit.repo.untracked_files:
            commit.GitCommandRunner(count, i, commit.CommitMessage("Inserted",str(i)))
            count += 1
            if count == 130:
               commit.origin.push()
               count = 0
        for item in commit.repo.index.diff(None):
            commit.GitCommandRunner(count, item.a_path, commit.CommitMessage("Updated",str(item.a_path)))
            count += 1
            if count == 130:
               commit.origin.push()
               count = 0
        # push all commits at once
        commit.origin.push()

        print(f"Done !!! committing : {count} files")


if __name__ == '__main__':
    mainObject = Main()
    mainObject.main()

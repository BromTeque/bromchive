# Automatic git clone and pull for git repositories to ble deployed with cron

import os
import git
import time
import logging


def main():
    # Variables and initiation
    workDir = '/mnt/ata-ST12000NM001G-2MV103_ZL2B7EE1/Repositories Archive/bromchive'
    # Change working directory if wrong
    if os.getcwd != workDir:
        os.chdir(workDir)
    currentTime = str(int(time.time()))
    if not os.path.exists('./.logs'):
        os.makedirs('./.logs')
    logFile = os.path.join('./.logs/' + currentTime + '.log')
    reposDir = '/mnt/ata-ST12000NM001G-2MV103_ZL2B7EE1/Repositories Archive/repositories'
    logging.basicConfig(filename=logFile, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    repoList = []

    # Read Repo List
    for line in open('./repoList.txt'):
        currentLine = line.strip()
        if not (currentLine.startswith('#') or currentLine == ''):
            repoList.append(currentLine)

    class Progress(git.remote.RemoteProgress):
        def update(self, op_code, cur_count, max_count=None, message=''):
            logging.debug(self._cur_line)

    # Clone or pull repo
    for repo in repoList:
        # Find repo name
        repoName = repo.split('.git')[0].split('/')[-1]
        logging.debug(f"Repo URL: \"{repo}\"")
        logging.debug(f"Repo Directory name: \"{repoName}\"")
        # Define directory 
        repoDir = os.path.join(reposDir + '/' + repoName)
        # Clone if repo doesn't exist
        if not os.path.isdir(repoDir):
            logging.info(f"Cloning: \"{repo}\"")
            repo = git.Repo.clone_from(repo, repoDir, progress=Progress())
            logging.info("Done cloning")
        # Pull
        repo = git.Repo(repoDir)
        repo = repo.remotes.origin
        repo.pull(progress=Progress())
        logging.info("Done pulling")
    logging.info("End of Script")


if __name__ == "__main__":
    main()

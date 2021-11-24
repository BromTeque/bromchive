# Automatic git pull for mod repositories via cron

import os
import git
import time
import logging

def main():
    # Variables and initiation
    getTime = str(int(time.time()))
    logFile = os.path.join('./.logs/' + getTime + '.log')
    repoDir = os.path.join('./.testing/repo-' + getTime)
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

    # Clone repo
    if not os.path.isdir(repoDir):
        logging.info("Cloning: " + repoList[0])
        repo = git.Repo.clone_from(repoList[0], repoDir, progress=Progress())
        logging.info("Done cloning")

    repo = git.Repo(repoDir)
    repo = repo.remotes.origin
    repo.pull()


if __name__ == "__main__":
    main()



# cloned_repo = repo.clone_from("./test")
# assert cloned_repo.__class__ is git.Repo
# assert git.Repo.init("./test/newRepo").__class__ is git.Repo


# with open("./test/repo.tar", "wb") as fp:
#     repo.archive(fp)




# logging.basicConfig(filename=outputFile, level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# logging.debug('This but a test')

# print("am run")

# repo = git.Repo("/mnt/sdc/Repositories Archive/repositories/anbennar-eu4-fork-public-build")
# repo = git.Repo("./test")
# assert not repo.bare
# repo.config_reader()


# # Clone repo
# cloned_repo = repo.clone("./test")
# assert cloned_repo.__class__ is git.Repo
# assert git.Repo.init("./test/newRepo").__class__ is git.Repo


# with open("./test/repo.tar", "wb") as fp:
#     repo.archive(fp)
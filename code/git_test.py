import os
import shutil
import glob
from pathlib import Path
from git import Repo
from git import exc

repo_url = "git@github.com:aidandj/python-git-test-repo.git"
repo_base_path = Path("/repos")
repo_path = Path("/repos/python-git-test-test")

# Clean up
def clean_up():
    files = list(repo_base_path.iterdir())
    for file in files:
        shutil.rmtree(bytes(file)) if file.is_dir() else os.remove(bytes(file))


# Clone a repo
def clone_repo(url, path):
    return Repo.clone_from(repo_url, repo_path)

# Get repo
def get_repo():
    try:
        repo = Repo(repo_path)
    except exc.NoSuchPathError:
        # Then clone it
        repo = clone_repo("","")
    return repo

# checkout a branch
def checkout(repo):
    new_branch = repo.create_head('test1')
    new_branch.checkout()
    assert new_branch == repo.active_branch

# commit an empty message
def commit(repo):
    repo.index.commit("Testing empty commit")

# push current branch to origin
def push_to_origin(repo):
    origin = repo.remotes.origin
    origin.push('test1')

# push to master
def push_to_master(repo):
    origin = repo.remotes.origin
    origin.push('master')

# fetch from master
def fetch_from_master(repo):
    origin = repo.remotes.origin
    print(origin.refs)
    print(origin.urls)
    origin.fetch('master')

def merge_master(repo):
    out = repo.git.merge('FETCH_HEAD')
    print(f'Git Output:\n{out}')

if __name__ == "__main__":
    # for debugging
    os.environ['GIT_PYTHON_TRACE'] = "1"
    repo = clone_repo("","")

    
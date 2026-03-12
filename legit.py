class Commit():
    def __init__(self, id, parent, message):
        self.id = id
        self.parent = parent
        self.message = message

class Legit():
    def __init__(self, name):
        self.name = name # repo name
        self.last_commit_id = 0
        self.HEAD = None # points to the last commit

    def commit(self, message):
        new_commit = Commit(self.last_commit_id, self.HEAD, message)
        # update HEAD and current branch
        self.HEAD = new_commit
        self.last_commit_id += 1
        return new_commit
    
    def log(self):
        commit = self.HEAD
        history = [] # list of commits in reverse order

        while(commit):
            history.append(commit)
            commit = commit.parent

        return history


repo = Legit("my_repo")
# Actual command:
# > git init

repo.commit("Initial commit")
# Actual command:
# > git commit -m "Make commit work"


repo.commit("Add README")
repo.commit("Fix bug")

history = repo.log()

for commit in history:
    print(f"commit {commit.id}")
    print(f"    {commit.message}")
# Actual command:
# > git log
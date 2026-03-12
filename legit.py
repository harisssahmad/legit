class Commit():
    def __init__(self, id, message):
        self.id = id
        self.message = message

class Legit():
    def __init__(self, name):
        self.name = name # repo name
        self.last_commit_id = 0

    def commit(self, message):
        new_commit = Commit(self.last_commit_id, message)
        self.last_commit_id += 1
        return new_commit


repo = Legit("my_repo")
# Actual command:
# > git init

repo.commit("Initial commit")
# Actual command:
# > git commit -m "Make commit work"
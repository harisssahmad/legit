class Commit():
    def __init__(self, id, parent, message):
        self.id = id
        self.parent = parent
        self.message = message

class Branch():
    def __init__(self, name, commit):
        self.name = name
        self.commit = commit

class Legit():
    def __init__(self, name):
        self.name = name # repo name
        self.last_commit_id = 0
        self.branches = []
        self.master = Branch("master", None) # master branch starts with no commits
        self.branches.append(self.master) # store master branch
        self.HEAD = self.master # HEAD points to the current branch (master)

    def commit(self, message):
        new_commit = Commit(self.last_commit_id, self.HEAD.commit, message)
        # update HEAD and current branch
        self.HEAD.commit = new_commit
        self.last_commit_id += 1
        return new_commit
    
    def checkout(self, branch_name):
        # loop through all branches
        for i in range(len(self.branches) - 1, -1, -1):
            # check if branch name matches
            if self.branches[i].name == branch_name:
                # switch to existing branch
                self.HEAD = self.branches[i]
                return self
        
        # branch doesn't exist, create new branch from current HEAD
        new_branch = Branch(branch_name, self.HEAD.commit)
        self.branches.append(new_branch)
        self.HEAD = new_branch

        return self
    
    def log(self):
        commit = self.HEAD.commit
        history = [] # list of commits in reverse order

        while(commit):
            history.append(commit)
            commit = commit.parent

        return history
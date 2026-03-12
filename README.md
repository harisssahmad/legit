# Legit

### A simplified reimplementation of Git written in Python implementing core VCS features.

**Legit** is a minimal Git-like version control system written in Python.  
It supports creating a repository, making commits, branching with `checkout`, and viewing commit history (`log`).

---

## Classes

-   **Commit**: Represents a single commit
-   **Branch**: Represents a branch with a name and latest commit
-   **Legit**: Main repository class with methods:
    -   `commit(message)` → Create a new commit
    -   `checkout(branch_name)` → Switch to or create a branch
    -   `log()` → Return a list of commits from latest to first

---

## Example Usage (Python)

```python
from legit import Legit

# Initialize repository
repo = Legit("my_repo")
# Actual command:
# > git init

# Make commits
repo.commit("Initial commit")
# Actual command:
# > git commit -m "Initial commit"

repo.commit("Add README")
repo.commit("Fix bug")
# Actual command:
# > git commit -m "Add README"
# > git commit -m "Fix bug"

# View commit history
history = repo.log()
for commit in history:
    print(f"commit {commit.id}")
    print(f"    {commit.message}")
# Actual command:
# > git log
```

## Branch Diagram

```
* master
| commit 2: Fix bug
| commit 1: Add README
| commit 0: Initial commit
|
* feature
  commit 3: Add feature X
```

-   `* master` → The main branch (HEAD)
-   `* feature` → Separate feature branch
-   Commits are listed latest to earliest

## Missing Git Features

Legit is minimal and does not yet support:

-   `git merge` (merging branches)
-   `git rebase`
-   Staging area (`git add`)
-   Undoing commits (`git reset`, `git revert`)
-   Remote repositories (`git push`, `git pull`)
-   Tags (`git tag`)
-   Conflict resolution

This makes it ideal for learning Git internals and exploring commit/branch mechanics.

## Notes

-   HEAD points to the current branch.
-   Each branch stores its own latest commit.
-   Commit IDs start at 0 and increment automatically.
-   Branches are created automatically when checking out a new name.
-   `log()` prints commits from the most recent back to the first.

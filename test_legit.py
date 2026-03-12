from legit import Legit

def test_single_commit():
    repo = Legit("test-repo")
    commit = repo.commit("initial commit")

    assert commit.id == 0
    assert commit.message == "initial commit"

def test_multiple_commits():
    repo = Legit("test-repo")

    c1 = repo.commit("first")
    c2 = repo.commit("second")

    assert c1.id == 0
    assert c2.id == 1

def test_empty_log():
    repo = Legit("test_repo")
    history = repo.log()

    assert history == []


def test_single_commit_log():
    repo = Legit("test_repo")

    repo.commit("Initial commit")

    history = repo.log()

    assert len(history) == 1
    assert history[0].message == "Initial commit"
    assert history[0].id == 0


def test_multiple_commits_log():
    repo = Legit("test_repo")

    repo.commit("Initial commit")
    repo.commit("Second commit")
    repo.commit("Third commit")

    history = repo.log()

    assert len(history) == 3
    assert history[0].message == "Third commit"
    assert history[1].message == "Second commit"
    assert history[2].message == "Initial commit"


def test_parent_chain():
    repo = Legit("test_repo")

    c1 = repo.commit("Initial commit")
    c2 = repo.commit("Second commit")

    assert repo.HEAD == c2
    assert repo.HEAD.parent == c1
    assert c1.parent is None

if __name__ == "__main__":
    test_single_commit()
    test_multiple_commits()
    test_empty_log()
    test_single_commit_log()
    test_multiple_commits_log()
    test_parent_chain()
    print("All tests passed.")
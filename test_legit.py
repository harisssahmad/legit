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

    assert repo.HEAD.commit == c2
    assert repo.HEAD.commit.parent == c1
    assert c1.parent is None

def test_create_new_branch():
    repo = Legit("repo")

    repo.commit("initial")
    repo.checkout("feature")

    assert repo.HEAD.name == "feature"
    assert len(repo.branches) == 2
    assert repo.HEAD.commit.message == "initial"


def test_switch_existing_branch():
    repo = Legit("repo")

    repo.commit("initial")
    repo.checkout("feature")
    repo.checkout("master")

    assert repo.HEAD.name == "master"


def test_branch_diverges():
    repo = Legit("repo")

    repo.commit("initial")

    repo.checkout("feature")
    repo.commit("feature commit")

    repo.checkout("master")
    repo.commit("master commit")

    # check master history
    history_master = repo.log()
    assert history_master[0].message == "master commit"
    assert history_master[1].message == "initial"

    # check feature history
    repo.checkout("feature")
    history_feature = repo.log()
    assert history_feature[0].message == "feature commit"
    assert history_feature[1].message == "initial"


def test_checkout_returns_repo():
    repo = Legit("repo")

    result = repo.checkout("feature")

    assert result == repo

if __name__ == "__main__":
    # commits check
    test_single_commit()
    test_multiple_commits()
    # logs check
    test_empty_log()
    test_single_commit_log()
    test_multiple_commits_log()
    test_parent_chain()
    # checkout and branches check
    test_create_new_branch()
    test_switch_existing_branch()
    test_branch_diverges()
    test_checkout_returns_repo()
    print("All tests passed.")
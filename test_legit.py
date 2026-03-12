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


if __name__ == "__main__":
    test_single_commit()
    test_multiple_commits()
    print("All tests passed.")
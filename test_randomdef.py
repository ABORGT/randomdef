import pytest
from randomdef import randomDefinition


def test_noexample_nosubset(capsys):
    testObject = randomDefinition('test', showexample=False, subset=False)
    testObject.get_synset()
    testObject.print_output()
    out, err = capsys.readouterr()
    defstring = "The definition of {0} is:".format(testObject.inword)
    assert defstring in out
    assert testObject.example is None
    assert err == ''


def test_example_nosubset(capsys):
    testObject = randomDefinition('test', showexample=True, subset=False)
    testObject.get_synset()
    testObject.print_output()
    out, err = capsys.readouterr()
    defstring = "The definition of {0} is:".format(testObject.inword)
    assert defstring in out
    assert "Example: " in out or "No examples available" in out
    assert err == ''


def test_noexample_subset(capsys):
    testObject = randomDefinition('test', showexample=False, subset=True)
    testObject.get_synset()
    testObject.print_output()
    out, err = capsys.readouterr()
    defstring = "The definition of {0} is:".format(testObject.inword)
    assert defstring in out
    assert testObject.example is None
    assert err == ''


def test_example_subset(capsys):
    testObject = randomDefinition('test', showexample=True, subset=True)
    testObject.get_synset()
    testObject.print_output()
    out, err = capsys.readouterr()
    defstring = "The definition of {0} is:".format(testObject.inword)
    assert defstring in out
    assert "Example: " in out or "No examples available" in out
    assert err == ''


def test_random_word_exit():
    testObject = randomDefinition('test')
    testObject.word_list = []
    with pytest.raises(SystemExit):
        testObject.random_word()


def test_no_examples(capsys):
    testObject = randomDefinition('test', showexample=True)
    testObject.get_synset()
    testObject.example = "NULLNULLNULL"
    testObject.print_output()
    out, err = capsys.readouterr()
    assert "No examples available" in out
    assert err == ''

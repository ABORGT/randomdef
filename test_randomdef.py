import randomdef


def test_noexample_nosubset():
    testObject = randomdef.randomDefinition('test', showexample=False, subset=False)
    assert testObject.inword == 'test'
    assert len(testObject.word_list) > 1000
    testObject.get_synset()
    assert testObject.syns 
    assert testObject.example == None
    
def test_example_nosubset():
    testObject = randomdef.randomDefinition('test', showexample=True, subset=False)
    assert testObject.inword == 'test'
    assert len(testObject.word_list) > 1000
    testObject.get_synset()

def test_noexample_subset():
    testObject = randomdef.randomDefinition('test', showexample=False, subset=True)
    assert testObject.inword == 'test'
    assert len(testObject.word_list) == 1000
    testObject.get_synset()
    assert testObject.example == None

def test_example_subset():
    testObject = randomdef.randomDefinition('test', showexample=True, subset=True)
    assert testObject.inword == 'test'
    assert testObject.showexample == True
    assert len(testObject.word_list) == 1000
    testObject.get_synset()

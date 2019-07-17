from storyscript.hub.engine.Builtins import builtins


def test_builtins():
    # ensures that the variables doesn't get accidentally renamed
    assert 'contains' in len(builtins)

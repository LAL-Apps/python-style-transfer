import deepdream

def test_can_import_module():
    dream = deepdream.Dream()
    assert dream is not None

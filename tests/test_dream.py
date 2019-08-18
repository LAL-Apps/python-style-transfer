import deepdream
import os

def test_can_import_module():
    dream = deepdream.Dream()
    assert dream is not None

def test_train_with_images_from_file():
    dream = deepdream.Dream()
    cwd = os.getcwd()#This assumes test is run from parent directory with make test
    dream.setContentFromPath(os.path.join(cwd,'tests','content.jpeg'))
    dream.setStyleFromPath(os.path.join(cwd,'tests','style.jpeg'))
    assert dream.contentImage is not None
    assert dream.styleImage is not None
    #TODO test training

def test_train_with_images_from_url():
    dream = deepdream.Dream()
    dream.setContentFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Felis_silvestris_catus_lying_on_rice_straw.jpg/640px-Felis_silvestris_catus_lying_on_rice_straw.jpg')
    dream.setStyleFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tsunami_by_hokusai_19th_century.jpg/640px-Tsunami_by_hokusai_19th_century.jpg')
    assert dream.contentImage is not None
    assert dream.styleImage is not None
    #TODO

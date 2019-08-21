from styletransfer import StyleTransfer
import os

def test_can_import_module():
    styletransfer = StyleTransfer()
    assert styletransfer is not None

def test_train_with_images_from_file():
    styletransfer = StyleTransfer()
    cwd = os.getcwd()#This assumes test is run from parent directory with make test
    styletransfer.setContentFromPath(os.path.join(cwd,'tests','content.jpeg'))
    styletransfer.setStyleFromPath(os.path.join(cwd,'tests','style.jpeg'))
    assert styletransfer.contentImage is not None
    assert styletransfer.styleImage is not None

    #Set the parameters
    styletransfer.setParams(9,9,8,5,2,1,1e6)
    assert styletransfer.styleLayerWeights is not None

    #Run the training loop. Only 1 epoch for the test
    img = styletransfer.apply(1)
    assert img is not None

    styletransfer.writeFinalImage('styletransfer-test.jpg')
    assert os.path.isfile('styletransfer-test.jpg')

    #Delete the file again
    os.remove('styletransfer-test.jpg')


def test_load_images_from_url():
    styletransfer = StyleTransfer()
    styletransfer.setContentFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Felis_silvestris_catus_lying_on_rice_straw.jpg/640px-Felis_silvestris_catus_lying_on_rice_straw.jpg')
    styletransfer.setStyleFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tsunami_by_hokusai_19th_century.jpg/640px-Tsunami_by_hokusai_19th_century.jpg')
    assert styletransfer.contentImage is not None
    assert styletransfer.styleImage is not None

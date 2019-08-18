'''
Module to apply a deep dream to style and content image
'''
import logging
import requests
import io
from PIL import Image

from deepdream.exceptions import ImageLoadException

def loadImageFromUrl(url):
    '''
    Load an image from a URL into a PIL image
    :param url: URL to the picture
    :return: PIL image
    '''
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651'})
        picture  = r.content
    except requests.adapters.SSLError as e:
        raise ImageLoadException('SSL Error on URL {}'.format(url))
    except requests.exceptions.RequestException as e:
        raise ImageLoadException('Requests error {} on URL {}'.format(e,url))
    except (ConnectionResetError, http.client.HTTPException) as e:
        raise ImageLoadException('ConnectionResetError or BadStatusLine Error on URL {}'.format(url))
    #Process the image
    bytesPicture = io.BytesIO(picture)
    if len(bytesPicture.getvalue()) == 0:
        raise ImageLoadException('Received empty image from URL {}'.format(url))
    return Image.open(bytesPicture)


class Dream():
    '''
    Class that encapsulates all components needed to run deep drems on a picture
    '''

    def setContentFromPath(self, path):
        '''
        Set the content image from a path if the content image is stored on the local drive.

        :param path: Path to the image file
        '''
        #Load image and convert to RGB. Standard is RBG
        self.contentImage = Image.open(path).convert('RGB')

    def setContentFromUrl(self, url):
        '''
        Set the content image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        self.contentImage = loadImageFromUrl(url)

    def setStyleFromPath(self, path):
        '''
        Set the style image from a path if the style image is stored on the local drive.

        :param path: Path to the image file
        '''
        #Load image and convert to RGB. Standard is RBG
        self.styleImage = Image.open(path).convert('RGB')

    def setStyleFromUrl(self, url):
        '''
        Set the style image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        self.styleImage = loadImageFromUrl(url)

    def setParams(self):
        '''
        Set the weights for the model
        #TODO add parameters
        '''
        pass #TODO implement me

    def apply(self, epochs):
        '''
        Train the model. Content image, style image and parameters must have been set before.

        :param epochs: Number of iterations to train the model
        '''
        pass #TODO implement me

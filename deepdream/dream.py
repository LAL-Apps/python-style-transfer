'''
Module to apply a deep dream to style and content image
'''
import logging
import requests
import io
import torch
import numpy as np
import torch.optim as optim
from torchvision import transforms, models
from PIL import Image

from deepdream.exceptions import ImageLoadException

def prepImage(image,maxSize=400):
    '''
    Helper function to prepare an image by scaling and transforming
    :param image: PIL image object to scale
    :param maxSize: Max size of the picture. Reduce for faster training
    '''
    #Determine if image should be resized
    size = maxSize if max(image.size) > maxSize else max(image.size)

    #Apply the transformation to scale and normalize the image
    transform = transforms.Compose([
                        transforms.Resize(size),
                        transforms.ToTensor(),
                        transforms.Normalize((0.485, 0.456, 0.406),
                                             (0.229, 0.224, 0.225))])
    image = transform(image)
    #Remove the alpha dimension
    image = image[:3,:,:] #TODO unsqueeze to support batch dimension?
    return image

def loadImageFromUrl(url):
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
        image = Image.open(path).convert('RGB')
        self.contentImage = prepImage(image)

    def setContentFromUrl(self, url):
        '''
        Set the content image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        image = loadImageFromUrl(url)
        self.contentImage = prepImage(image)

    def setStyleFromPath(self, path):
        '''
        Set the style image from a path if the style image is stored on the local drive.

        :param path: Path to the image file
        '''
        #Load image and convert to RGB. Standard is RBG
        image = Image.open(path).convert('RGB')
        self.styleImage = prepImage(image)

    def setStyleFromUrl(self, url):
        '''
        Set the style image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        image = loadImageFromUrl(url)
        self.styleImage = prepImage(image)

    def setParams(self):
        '''
        Set the weights for the model
        #TODO add parameters
        '''
        pass #TODO implement me

    def train(self, epochs):
        '''
        Train the model. Content image, style image and parameters must have been set before.

        :param epochs: Number of iterations to train the model
        '''
        pass #TODO implement me

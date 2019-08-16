'''
Module to apply a deep dream to style and content image
'''
import logging
import torch
import torch.optim as optim
from torchvision import transforms, models
from PIL import Image

def loadImage(path,image,maxSize=400):
    '''
    Helper function to prepare an image by scaling and transforming
    :param path: File path to load the image from
    :param image: PIL image object to scale
    :param maxSize: Max size of the picture. Reduce for faster training
    '''
    #Load image and convert to RGB. Standard is RBG
    image = Image.open(path).convert('RGB')

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
    image = image[:3,:,:] #TODO unsqueeze to support batch dimension
    return image


class Dream():
    '''
    Class that encapsulates all components needed to run deep drems on a picture
    '''

    def setContentFromPath(self, path):
        '''
        Set the content image from a path if the content image is stored on the local drive.

        :param path: Path to the image file
        '''
        self.contentImage = loadImage(path)

    def setContentFromUrl(self, url):
        '''
        Set the content image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        pass #TODO Implement me

    def setStyleFromPath(self, path):
        '''
        Set the style image from a path if the style image is stored on the local drive.

        :param path: Path to the image file
        '''
        self.styleImage = loadImage(path)

    def setStyleFromUrl(self, url):
        '''
        Set the style image from a URL if the image should be downloaded.

        :param url: URL to the image
        '''
        pass #TODO Implement me

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

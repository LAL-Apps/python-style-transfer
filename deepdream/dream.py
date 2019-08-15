'''
Module to apply a deep dream to style and content image
'''

class Dream():
    '''
    Class that encapsulates all components needed to run deep drems on a picture
    '''

    def setContentFromPath(self, path):
        '''
        Set the content image from a path if the content image is stored on the local drive.

        :param path: Path to the image file
        '''
        pass #TODO Implement me

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
        pass #TODO Implement me

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

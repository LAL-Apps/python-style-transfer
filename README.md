# styletransfer
A Python library to transfer the style of one picture to another using PyTorch.

For example:

|Content | Style | Output |
|--------|---------|------------|
|[Cat with Bell by Tamba Budiarsana][1]|[Wood Bark Nature Texture by Free Stock Textures][2]|Generated Image|
|![content image][contentImage]|![style image][styleImage]|![stylized image][stylizedImage]|


## Installation
You can install styletransfer from PyPi using:

`pip install styletransfer`

This package requires Python 3.x

## Basic usage
The easiest way to get started is taking an online image for style transfer and just running with the default parameters:

```python
from styletransfer import StyleTransfer
styleTransfer = StyleTransfer()

#Set the content image from URL
styleTransfer.setContentFromUrl('https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/content.jpg')

#Set the style image from URL
styleTransfer.setStyleFromUrl('https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/style.jpg')

#Use default settings and train the model
#If you do not have a GPU that can take 30-60 minutes
styleTransfer.apply()

#Write the result image to a file
styleTransfer.writeFinalImage('stylized.jpg')
```

## Advanced usage

### Overview
The following methods are available on a style transfer object:

```python
from styletransfer import StyleTransfer
styleTransfer = StyleTransfer()

#Content and style image can be set from local files
styletransfer.setContentFromPath('content.jpg')
styletransfer.setStyleFromPath('style.jpg')

#Or they can be set from URLs. Both are equivalent, just use what is more convenient for you
styleTransfer.setContentFromUrl('https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/content.jpg')
styleTransfer.setStyleFromUrl('https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/style.jpg')

#You can set the parameters to be used in training like this:
styletransfer.setParams(weightLayer1, weightLayer2, weightLayer3, weightLayer4, weightLayer5, contentWeight, styleWeight)

#If you do not set the parameters the default values will be used which is equivalent to calling:
styletransfer.setParams(1.0, 0.75, 0.2, 0.2, 0.5, 1, 1e6)

#Once style, content and parameters are defined you can train the model by calling:
styleTransfer.apply(epochs)

#The epochs show for how long the model should train. If you do not provide epochs the default value is used which is equivalent to calling:
styleTransfer.apply(600)

#Once training has been completed you can save the model using:
styleTransfer.writeFinalImage('stylized.jpg')
#Since Pillow is used for saving the image the following formats are supported: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
```


[contentImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/content.jpg "Content image"
[styleImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/style.jpg "Style image"
[stylizedImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/stylized.jpg "Stylized content image"
[1]: https://www.pexels.com/photo/cat-with-bell-979250/
[2]: https://freestocktextures.com/texture/wood-bark-nature,231.html

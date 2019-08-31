# styletransfer
A Python library to transfer the style of one picture to another using PyTorch.

For example:

|Content | Style | Output |
|--------|---------|------------|
|[Felis silvestris catus lying on rice straw by Basile Morin][1]|[Red Gum Table by Mark Anthony Boyle][2]|Generated Image|
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
styleTransfer.setContentFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Felis_silvestris_catus_lying_on_rice_straw.jpg/640px-Felis_silvestris_catus_lying_on_rice_straw.jpg')

#Set the style image from URL
styleTransfer.setStyleFromUrl('https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/RedGumTable.jpg/320px-RedGumTable.jpg')

#Use default settings and train the model
#If you do not have a GPU that can take 30-60 minutes
styleTransfer.apply()

#Write the result image to a file
styleTransfer.writeFinalImage('stylized.jpg')
```

## Advanced usage
*TBD: Detailed instructions to follow*






[contentImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/content.jpeg "Content image"
[styleImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/style.jpg "Style image"
[stylizedImage]: https://github.com/LAL-Apps/python-style-transfer/raw/master/docs/stylized.jpg "Stylized content image"
[1]: https://commons.wikimedia.org/wiki/File:Felis_silvestris_catus_lying_on_rice_straw.jpg
[2]: https://commons.wikimedia.org/wiki/File:RedGumTable.jpg

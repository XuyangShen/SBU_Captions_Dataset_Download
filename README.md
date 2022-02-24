# SBU_Captions_Dataset_Download

This repo is a python download version for [SBU Captions Dataset](http://www.cs.virginia.edu/~vicente/sbucaptions/). If you want to use the dataset for any purpose, please follow the community/usage rules in [SBU Captions Dataset](http://www.cs.virginia.edu/~vicente/sbucaptions/).


## Usage
1. [Download the meta data](http://www.cs.virginia.edu/~vicente/sbucaptions/SBUCaptionedPhotoDataset.tar.gz), which also can be found in the main page (Resources-Data) of [SBU Captions Dataset](http://www.cs.virginia.edu/~vicente/sbucaptions/).
2. Put the [download.py](./download.py) inside the above 'meta data' folder.
3. Run [download.py](./download.py)

## Requriment
- python3
- additional python package: [pandas](https://pandas.pydata.org/docs/getting_started/install.html) and [tqdm](https://pypi.org/project/tqdm/)
- Linux / MacOS
- Network is accessible to [flickr](http://static.flickr.com/). Run a quick test in bash `$ wget http://static.flickr.com/2723/4385058960_b0f291553e.jpg`

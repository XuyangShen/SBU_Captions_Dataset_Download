import multiprocessing as mp
import os.path
import urllib.request

import pandas as pd
from tqdm import tqdm

BASE_FOLDER = 'sbu_images'
PROCESS = 32

def file2url(url_pth, captions_pth):
    with open(url_pth, 'r') as ufh:
        with open(captions_pth, 'r') as cfh:
            for url, captions in tqdm(zip(ufh.readlines(), cfh.readlines())):

                # mkdir
                urlblocks = url.strip().split('/')
                folder = urlblocks[3]
                if not os.path.exists(os.path.join(BASE_FOLDER, folder)):
                    os.mkdir(os.path.join(BASE_FOLDER, folder))
                
                pth = os.path.join(BASE_FOLDER, urlblocks[-2], urlblocks[-1])
                yield url.strip(), captions.strip(), pth

def url2file(args):
    url, captions, pth = args
    if os.path.exists(pth):
        return pth, captions

    try:
        urllib.request.urlretrieve(url, pth)
        return pth, captions
    except:
        return None


if __name__ == '__main__':
    PATHS = []
    CAPTIONS = []

    if not os.path.exists(BASE_FOLDER):
        os.mkdir(BASE_FOLDER)

    # mp pool
    pool = mp.Pool(PROCESS)

    # download
    for rst in pool.imap(url2file, file2url('SBU_captioned_photo_dataset_urls.txt', 'SBU_captioned_photo_dataset_captions.txt')):
        if rst is not None:
            pth, captions = rst
            PATHS.append(pth)
            CAPTIONS.append(captions)
    
    # save meta data
    df = pd.DataFrame({'path': PATHS, 'captions': CAPTIONS})
    df.to_csv('meta.csv', index=None)

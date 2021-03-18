

# import the necessary packages
from SearchDescriptors.colordescriptor import ColorDescriptor
from SearchDescriptors.texturedescriptor import TextureDescriptor
from SearchDescriptors.ShapeDescriptor import ShapeDescriptor
import argparse
import glob
import cv2
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "lien pour dataset")
ap.add_argument("-i", "--index", required = True,
	help = "lien pour index.csv")
args = vars(ap.parse_args())

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))
td= TextureDescriptor()
sd= ShapeDescriptor()

# open the output index file for writing
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):f
    imageID = imagePath[imagePath.rfind("\\") + 1:]
    image = cv2.imread(imagePath)
    features = list(np.array(cd.describe(image)))
    features = np.concatenate([features, td.TXD(image_gry)])
    features = np.concatenate([features, sd.ShapeD(image_gry)])

    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()
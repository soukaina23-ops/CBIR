import mahotas as mt
import cv2

class TextureDescriptor:
    def TXD(self,image):
        """ Calculate Local Binary Pattern for a grayscale image
            :param im: grayscale image
            :param n_points: number of points considered in a circular neighborhood
            :param rad: radius of neighborhood
            :return: histogram of local binary pattern
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # calculate haralick texture features for 4 types of adjacency
        textures = mt.features.haralick(gray)
        # take the mean of it and return it
        TD_mean = textures.mean(axis=0)
        norm=[(float(i)-min(TD_mean))/(max(TD_mean)-min(TD_mean)) for i in TD_mean]
        return norm
        



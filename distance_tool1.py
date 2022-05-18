import cv2
import numpy as np
import math

def cal_distance(estim_distance):
    # hyperparameter
    y_offset=35
    z_offset=16.5
    distance = math.sqrt((estim_distance[0]+y_offset)**2+abs(estim_distance[1])**2+z_offset**2)
    
    return distance

def draw_distance(image, homography,image_points):
    #for image_point in append_image_points:
    DATA_SIZE=len(image_points)
    append_image_points = np.append(image_points.reshape(DATA_SIZE,2), np.ones([1,DATA_SIZE]).T,axis=1)

    for image_point,append_image_point in zip(image_points,append_image_points):
        # estimation point(object_point) -> homography * src(image_point)
        estimation_distance = np.dot(homography, append_image_point)
        x= estimation_distance[0]
        y= estimation_distance[1]
        z= estimation_distance[2]
        distance = cal_distance([x/z,y/z,z/z])

        img_x,img_y = image_point
        cv2.putText(image, f"{int(distance)}cm", (int(img_x),int(img_y)-5), 1, 1, (255, 255, 0), 1)
        cv2.circle(image, (int(img_x),int(img_y)),1,(0,0,0),3)

    return image




import cv2
import numpy as np
import time
import os

# Requesting for scan input image
scanned_input_image_count= input('Total number of input scan images:')
scanned_input_image_count=int(scanned_input_image_count);

# Requesting for scanned character name
character_image_name=input('Character name in short form: ');
character_image_name=str(character_image_name)

# Output directory to store image
output_dir = input('Enter output directory:')
os.makedirs(output_dir, exist_ok=True)



# import image
for image_identifier in range(1,scanned_input_image_count+1):
    image = cv2.imread(character_image_name + '{}.tif'.format(image_identifier))
    # cv2.imshow('image',image)
    # cv2.waitKey(0)


    print('*******************IMAGE SIZE AND CHANNELS******************')
    # get dimension of image
    dimension = image.shape

    # height, width, number of channels in image
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('Image Dimension    : ',dimension)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray-image',gray)
    # cv2.waitKey(0)
    (thresh, thresh_image) = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    # cv2.imshow('thereshed_image',thresh_image)
    # cv2.waitKey(0)
    binary_image = 255 - thresh_image
    # cv2.imshow('binary_image',binary_image)
    # cv2.waitKey(0)
    v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated_image = cv2.dilate(binary_image, v_kernel)
    # print(v_ker)
    # cv2.imshow('dilated_image',dilated_image)
    # cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(
        dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    # print(f'Total number of contours{len(contours)}')
    # print('..................................')
    # print(hierarchy)
    table_boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        contour_box = [x, y, x + w, y + h]
        # # Drawing rectangle over original
        # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

        #Avoiding contour of full page rectangle 
        if w * h >= 0.5 * (image.shape[0] * image.shape[1]):
            # print(w,h,'larger_single_box')

            # # Drawing rectangle over original
            # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            continue
        if w > 100 and h > 100:  # Minimum area check
            # print(w,h,'box_13*8')
            # # Drawing rectangle over original
            # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            table_boxes.append(contour_box)

        else:
            # print(w,h,'contour_box inside box_13*8')
            # Drawing rectangle over original
            # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            pass

    # cv2.imshow('Contours in image',image)
    # cv2.waitKey(0)



    for i, contour_box in enumerate(table_boxes):
        w1,h1,w2,h2 = contour_box
        box_image = image[h1:h2,w1:w2]
        # cv2.imshow('Original box image with character',box_image)
        # cv2.waitKey(0)

        box_gray= cv2.cvtColor(box_image,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Grayscale box image with character',box_gray)
        # cv2.waitKey(0)

        thresh_,thresh_box = cv2.threshold(box_gray,220,255,cv2.THRESH_BINARY)
        # cv2.imshow('Threshed box image with character',thresh_box)
        # cv2.waitKey(0)

        binary_box = 255 - thresh_box
        # cv2.imshow('binary box-image with character',binary_box)
        # cv2.waitKey(0)

        # v_kernel_ = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        # dilated_box = cv2.dilate(binary_box,v_kernel_)

        v_kernel_ = np.ones((3,3),np.uint8)
        dilated_box = cv2.dilate(binary_box,v_kernel_,iterations =1)

        # cv2.imshow('dilated box image with character',dilated_box)
        # cv2.waitKey(0)


        # Find contours inside each box
        contours_,hierarchy_ = cv2.findContours(dilated_box,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours_:
            x_,y_,w_,h_ = cv2.boundingRect(cnt)
            contour_box_ =[x_, y_, x_+w_, y_+h_]
            a=35
            b=35
            c=35
            d =35
            if w_>20 and h_>20:
                # cv2.rectangle(box_image,(x_, y_),(x_+w_, y_+h_),(0,255,0),2)

                # for initial height
                if h1>(y_- a):
                    a=30
                    if h1>(y_- a):
                        a=25
                        if h1>(y_- a):
                            a=20
                            if h1>(y_- a):
                                a=15
                                if h1>(y_- a):
                                    a=10
                                    if h1>(y_- a):
                                        a=5
                                        if h1>(y_- a):
                                            a=0
                        
                # for initial width
                if w1>(x_- b):
                    b=30
                    if w1>(x_- b):
                        b=25
                        if w1<(x_- b):
                            b=20
                            if w1<(x_- b):
                                b=15
                                if w1<(x_- b):
                                    b=10
                                    if w1<(x_- b):
                                        b=5
                                        if w1<(x_- b):
                                            b=0



                # for final height
                if h2<(h_+ c):
                    c=30
                    if h2<(h_+ c):
                        c=25
                        if h2>(h_+ c):
                            c=20
                            if h2>(h_+ c):
                                c=15
                                if h2>(h_+ c):
                                    c=10
                                    if h2>(h_+ c):
                                        c=5
                                        if h2>(h_+ c):
                                            c=0

                
                # for final width
                if w2<(w_+ d):
                    d=30
                    if w2>(w_+ d):
                        d=25
                        if w2<(w_+ d):
                            d=20
                            if w2<(w_+ d):
                                d=15
                                if w2<(w_+ d):
                                    d=10
                                    if w2<(w_+ d):
                                        d=5
                                        if w2<(w_+ d):
                                            d=0
                    
                char_image = box_image[y_-a:y_+h_+c,x_-b:x_+w_+d]
                # cv2.imshow('Character Image',char_image)
                # cv2.waitKey(0)

                # Save image
                cv2.imwrite(os.path.join(output_dir,character_image_name+'_'+str(time.time())+str(i)+'.jpeg'),char_image)


        # cv2.imshow('Contours in box-image',box_image)
        # cv2.waitKey(0)

        


            # char_img = image[y_:h_,x_:h_]










# # import image
# for img in range(1,scanned_input_image_count+1):
#     image = cv2.imread(character_image_name + '{}.jpg'.format(img))

#     # grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     #cv2.imshow('gray', gray)

#     # binary
#     ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
#     #cv2.imshow('threshold', thresh)

#     # dilation
#     kernel = np.ones((10, 1), np.uint8)
#     img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#     #cv2.imshow('dilated', img_dilation)

#     # find contours
#     # cv2.findCountours() function changed from OpenCV3 to OpenCV4: now it have only two parameters instead of 3
#     cv2MajorVersion = cv2.__version__.split(".")[0]
#     # check for contours on thresh
#     if int(cv2MajorVersion) >= 4:
#         ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     else:
#         im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # sort contours
#     sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

#     for i, ctr in enumerate(sorted_ctrs):
#         # Get bounding box
#         x, y, w, h = cv2.boundingRect(ctr)

#         # Getting ROI
#         roi = image[y:y + h, x:x + w]

#         # resizing
#         resize = cv2.resize(roi, (128, 128))

#         # inverting images
#         #case2
#         #img_invert = (255 - resize)
#         img_invert = cv2.bitwise_not(resize)


#         # show ROI
#         # cv2.imshow('segment no:'+str(i),roi)
#         # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         if w > 15 and h > 15:
#             cv2.imwrite(str(i) + str(time.time())+'{}.png'.format(i), img_invert)

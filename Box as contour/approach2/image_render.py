import cv2
import numpy as np
import time
import os


current_directory = os.getcwd()
print(current_directory)

identifier=1;# identifier -1 = image count
character_image_name=input('Character name in short form: ');
character_image_name=str(character_image_name)


for file in  os.listdir(current_directory):
    if file.endswith('.tif'):
        os.rename(file,character_image_name+"{}.tif".format(identifier))
        #print(file)
        identifier += 1
	        

scanned_input_image_count=identifier - 1 
character_image_name=character_image_name

# Output directory to store image
output_dir = character_image_name
os.makedirs(output_dir, exist_ok=True)
print('**********************************************************')
print('Wait a seconds image are generating...')



# import imagecharacter_image_name
for image_identifier in range(1,scanned_input_image_count+1):
    image = cv2.imread(character_image_name + '{}.tif'.format(image_identifier))
    # cv2.imshow('image',image)
    # cv2.waitKey(0)
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    (thresh, thresh_image) = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)

    binary_image = 255 - thresh_image

    v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated_image = cv2.dilate(binary_image, v_kernel)

    contours, hierarchy = cv2.findContours(
        dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)

    table_boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        contour_box = [x, y, x + w, y + h]

        if w * h >= 0.5 * (image.shape[0] * image.shape[1]):

            continue
        if w > 100 and h > 100:  # Minimum area check

            table_boxes.append(contour_box)

        else:
            pass



    for i, contour_box in enumerate(table_boxes):
        w1,h1,w2,h2 = contour_box
        image_box = image[h1+8:h2-8,w1+5:w2-5]
  
        image_128 = cv2.resize(image_box, (128, 128))

        gray_image= cv2.cvtColor(image_128, cv2.COLOR_BGR2GRAY)

        ret, thresh_image = cv2.threshold(
            gray_image, 180, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((3,3), np.uint8) 
        dilated_image= cv2.dilate(thresh_image, kernel, iterations=1)
        cv2.imwrite(os.path.join(output_dir,character_image_name+'_'+str(image_identifier)+str(i)+'.jpg'),dilated_image)

if identifier == 1:
    print("You don't have any images now..")
elif identifier <12:
    print("You don't have complete scanned image")
else:
    print(f'Image generation completed,check your folder  named "{output_dir}"')

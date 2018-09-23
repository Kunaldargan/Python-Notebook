import os
import cv2

path_to_images = input("Path to Images : " )
path_to_blurry = input("Path to blurred images : " )
threshold = 100 // to be tested

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

for img in os.listdir(path_to_images):
	test_image = cv2.imread(os.path.join(path_to_images,img))
	var = variance_of_laplacian(test_image)
	if var < threshold:
		print("blurred image : ",os.path.join(path_to_images,img))
		os.rename(os.path.join(path_to_images,img), os.path.join(path_to_blurry,img))
		cv2.putText(test_image, "{}: {:.2f}".format("blurry", var), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
		cv2.imshow("Image", test_image)
		key = cv2.waitKey(1)
	else : 
		cv2.putText(test_image, "{}: {:.2f}".format("not blurry", var), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
		cv2.imshow("Image", test_image)
		key = cv2.waitKey(1)

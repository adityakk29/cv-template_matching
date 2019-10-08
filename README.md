# Template matching
Template matching is a technique for finding areas of an image that are similar to a patch (template).
A patch is a small image with certain features. The goal of template matching is to find the patch/template in an image.
To find it, the user has to give two input images: **Source Image (S)** – The image to find the template in and **Template Image (T)**

## How does it work?

* The template image simply slides over the input image (as in 2D convolution)
* The template and patch of input image under the template image are compared.
* The result obtained is compared with the threshold.
* If the result is greater than threshold, the portion will be marked as detected.
* In the function cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) the first parameter is the mainimage, second parameter is the template to be matched and third parameter is the method used for matching.

### Example:
*    We need two primary components:
        1. Source image (I): The image in which we expect to find a match to the template image
        2. Template image (T): The patch image which will be compared to the template image
        
        Our goal is to detect the highest matching area:
    
       ![alt text](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Summary.jpg)

*    To identify the matching area, we have to compare the template image against the source image by sliding it:

      ![alt text](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Sliding.jpg)
      
*    By sliding, we mean moving the patch one pixel at a time (left to right, up to down). At each location, a metric is calculated so it represents how "good" or "bad" the match at that location is (or how similar the patch is to that particular area of the source image).

 *   For each location of T over I, you store the metric in the result matrix R. Each location (x,y) in R contains the match metric:
      ![alt text](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Result.jpg)
      
the image above is the result R of sliding the patch with a metric TM_CCORR_NORMED. The brightest locations indicate the highest matches. As you can see, the location marked by the red circle is probably the one with the highest value, so that location (the rectangle formed by that point as a corner and width and height equal to the patch image) is considered the match.
 *   In practice, we locate the highest value (or lower, depending of the type of matching method) in the R matrix, using the function minMaxLoc()

| Enumerator                       |   | NORMED                                         |
|----------------------------------|---|------------------------------------------------|
| TM_SQDIFF   Python: cv.TM_SQDIFF |   | TM_SQDIFF_NORMED   Python: cv.TM_SQDIFF_NORMED |
| TM_CCORR   Python: cv.TM_CCORR   |   | TM_CCORR_NORMED   Python: cv.TM_CCORR_NORMED   |
| TM_CCOEFF   Python: cv.TM_CCOEFF |   | TM_CCOEFF_NORMED  Python: cv.TM_CCOEFF_NORMED  |

More details here: https://docs.opencv.org/master/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d

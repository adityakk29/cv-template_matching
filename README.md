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

| Enumerator                                   |                                                                                                                                                      |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| TM_SQDIFF Python: cv.TM_SQDIFF               | R(x,y)= \sum \_{x',y'} (T(x',y')-I(x+x',y+y'))^2                                                                                                                |
| TM_SQDIFF_NORMED Python: cv.TM_SQDIFF_NORMED | R(x,y)=∑x′,y′(T(x′,y′)−I(x+x′,y+y′))2∑x′,y′T(x′,y′)2⋅∑x′,y′I(x+x′,y+y′)2−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√                                            |
| TM_CCORR Python: cv.TM_CCORR                 | R(x,y)=∑x′,y′(T(x′,y′)⋅I(x+x′,y+y′))                                                                                                                 |
| TM_CCORR_NORMED Python: cv.TM_CCORR_NORMED   | R(x,y)=∑x′,y′(T(x′,y′)⋅I(x+x′,y+y′))∑x′,y′T(x′,y′)2⋅∑x′,y′I(x+x′,y+y′)2−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√                                             |
| TM_CCOEFF Python: cv.TM_CCOEFF               | R(x,y)=∑x′,y′(T′(x′,y′)⋅I′(x+x′,y+y′)) where T′(x′,y′)=T(x′,y′)−1/(w⋅h)⋅∑x′′,y′′T(x′′,y′′)I′(x+x′,y+y′)=I(x+x′,y+y′)−1/(w⋅h)⋅∑x′′,y′′I(x+x′′,y+y′′)  |

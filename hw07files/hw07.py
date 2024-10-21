import copy, bmp_edit

#Problem A: Grayscale
def grayscale(img_matrix):
    '''
    Purpose:
      The function takes in an image matrix, looping through every pixel, 
      each pixel has three passages(RGB) to represent the color. So the function
      caculates the average for sum of the values of passages and reassign the result
      to each passage so that the őixel would be converted to grayscale.
      Therefore, finally the function would return a image matrix that is totally
      converted into grayscale.
    Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            red = img_matrix[y][x][0]
            green = img_matrix[y][x][1]
            blue = img_matrix[y][x][2]
            avg = (red+green+blue)//3
            img_matrix[y][x][0] = avg
            img_matrix[y][x][1] = avg
            img_matrix[y][x][2] = avg
    return img_matrix

    
#Problem B: Rotate Quadrants
def rotate_quadrants(img_matrix):
    '''
    Purpose:
      Split the image into four equally sized quadrants, and rotate
      them clockwise to form the output image.
    Input Parameter(s):
      (see grayscale) - plus, it can be assumed the img_matrix will have
      an even number of rows and columns.
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.  
    '''
    #TODO: Fix the logic error in the code
    height = len(img_matrix)  
    width = len(img_matrix[0]) 
    for y in range(height//2):
        for x in range(width//2):
            temp=img_matrix[y][x]
            img_matrix[y][x] = img_matrix[y+height//2][x]
            img_matrix[y+height//2][x] = img_matrix[y+height//2][x+width//2]
            img_matrix[y+height//2][x+width//2] = img_matrix[y][x+width//2]
            img_matrix[y][x+width//2] = temp
    return img_matrix


#Problem C: Lossy Compression
def lossy(img_matrix):
    '''
    Purpose:
      Sets all color component values in the image matrix to 0, 100, or 200,
      by rounding down to the nearest 100.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    #TODO: Finish this function
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            red = img_matrix[y][x][0]
            if red>=100:
                red-=red%100
            else:
                red=0
            green = img_matrix[y][x][1]
            if green>=100:
                green-=green%100
            else:
                green=0            
            blue = img_matrix[y][x][2]
            if blue>=100:
                blue-=blue%100
            else:
                blue=0
            img_matrix[y][x][0] = red
            img_matrix[y][x][1] = green
            img_matrix[y][x][2] = blue
    return img_matrix
import copy
#Problem D: Zoom
def zoom(img_matrix):
    '''
    Purpose:
      Doubles the size of the upper-left quadrant of the input
      image, so that it takes up the entire output image.
      Each pixel in the upper-left quadrant of the input is copied
      to a 2x2 block of pixels in the output.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    new_matrix = copy.deepcopy(img_matrix)
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height//2):
        for x in range(width//2):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            red = img_matrix[y][x][0]
            green = img_matrix[y][x][1]  
            blue = img_matrix[y][x][2]
            new_matrix[2*y][2*x][0]=red
            new_matrix[2*y][2*x+1][0]=red
            new_matrix[2*y+1][2*x][0]=red
            new_matrix[2*y+1][2*x+1][0]=red
            new_matrix[2*y][2*x][1]=green
            new_matrix[2*y][2*x+1][1]=green
            new_matrix[2*y+1][2*x][1]=green
            new_matrix[2*y+1][2*x+1][1]=green
            new_matrix[2*y][2*x][2]=blue
            new_matrix[2*y][2*x+1][2]=blue
            new_matrix[2*y+1][2*x][2]=blue
            new_matrix[2*y+1][2*x+1][2]=blue
    return new_matrix 
                

#Problem E: Your Own Filter
def custom_filter(img_matrix):
    '''
    Purpose:
      Set the entire image to a solid blue rectangle.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            img_matrix[y][x][0] = 0
            img_matrix[y][x][1] = 0
            img_matrix[y][x][2] = 225
    return img_matrix


if __name__ == '__main__':
    print(grayscale([[[127, 127, 127], [0, 0, 0]],
                    [[255, 255, 0], [50, 128, 255]],
                    [[0, 0, 255], [0, 255, 0]],
                    [[255, 0, 0], [255, 255, 255]]]))

    #[[[127, 127, 127], [0, 0, 0]],
    #[[170, 170, 170], [144, 144, 144]],
    #[[85, 85, 85], [85, 85, 85]],
    #[[85, 85, 85], [255, 255, 255]]]
    
if __name__ == '__main__':
    print(rotate_quadrants([[[127, 127, 127], [0, 0, 0]],
                           [[255, 255, 0], [50, 128, 255]],
                           [[0, 0, 255], [0, 255, 0]],
                           [[255, 0, 0], [255, 255, 255]]]))

    #[[[0, 0, 255], [127, 127, 127]],
    #[[255, 0, 0], [255, 255, 0]],
    #[[0, 255, 0], [0, 0, 0]],
    #[[255, 255, 255], [50, 128, 255]]]


if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', rotate_quadrants)
    bmp_edit.transform('cat.bmp', rotate_quadrants)
    bmp_edit.transform('connector.bmp', rotate_quadrants)

if __name__ == '__main__':
    print(lossy([[[127, 127, 127], [0, 0, 0]],
    [[255, 255, 0], [50, 128, 255]],
    [[0, 0, 255], [0, 255, 0]],
    [[255, 0, 0], [255, 255, 255]]]))

    #[[[100, 100, 100], [0, 0, 0]], 
    #[[200, 200, 0], [0, 100, 200]], 
    #[[0, 0, 200], [0, 200, 0]], 
    #[[200, 0, 0], [200, 200, 200]]]


    print(lossy([[[36, 155, 90], [63, 208, 208], [151, 3, 14]],
    [[53, 204, 53], [99, 103, 10], [94, 138, 216]]]))

    #[[[0, 100, 0], [0, 200, 200], [100, 0, 0]],
    #[[0, 200, 0], [0, 100, 0], [0, 100, 200]]]

if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', lossy)
    bmp_edit.transform('cat.bmp', lossy)
    bmp_edit.transform('connector.bmp', lossy)


if __name__ == '__main__':
    print(zoom([[[127, 127, 127], [0, 0, 0]],
                 [[255, 255, 0], [50, 128, 255]],
                 [[0, 0, 255], [0, 255, 0]],
                 [[255, 0, 0], [255, 255, 255]]]))

    #[[[127, 127, 127], [127, 127, 127]],
    #[[127, 127, 127], [127, 127, 127]],
    #[[255, 255, 0], [255, 255, 0]],
    #[[255, 255, 0], [255, 255, 0]]]
	
    print(zoom(
     [[ [255, 0, 0], [255,153,0], [255,255,0],[255,204,51]],
      [ [0, 255, 0], [0,255,255],[50,128,255],[255,204,51]],
      [ [0, 0, 255], [153,0,255], [255,0,255],[255,204,51]],
      [   [0, 0, 0],[255,204,51], [122,0,25] , [122,0,25] ],
      [[255,204,51], [122,0,25] , [122,0,25] , [122,0,25] ],
      [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ],
      [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ],
      [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ]]))

    #[[ [255, 0, 0], [255, 0, 0], [255,153,0], [255,153,0]],
    # [ [255, 0, 0], [255, 0, 0], [255,153,0], [255,153,0]],
    # [ [0, 255, 0], [0, 255, 0], [0,255,255], [0,255,255]],
    # [ [0, 255, 0], [0, 255, 0], [0,255,255], [0,255,255]],
    # [ [0, 0, 255], [0, 0, 255], [153,0,255], [153,0,255]],
    # [ [0, 0, 255], [0, 0, 255], [153,0,255], [153,0,255]],
    # [   [0, 0, 0],   [0, 0, 0],[255,204,51],[255,204,51]],
    # [   [0, 0, 0],   [0, 0, 0],[255,204,51],[255,204,51]]]



if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', zoom)
    bmp_edit.transform('cat.bmp', zoom)
    bmp_edit.transform('connector.bmp', zoom)

if __name__ == '__main__':
    bmp_edit.transform('dice.bmp', custom_filter)
    bmp_edit.transform('cat.bmp', custom_filter)
    bmp_edit.transform('connector.bmp', custom_filter)

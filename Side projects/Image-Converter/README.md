# Image transformation minute project
Here are the results of applying the transformations to an example image:

### Original Image
<img src="./assets/cat.jpg" alt="Original image" width="300" />

### 1. Grayscale Conversion
<img src="./assets/grayscale.jpg" alt="Grayscale image" width="300"/>

    New R = (R + G + B)/3
    New G = (R + G + B)/3
    New B = (R + G + B)/3

### 2. Color Inversion
<img src="./assets//color-inversion.jpg" alt="Inverted image" width="300" />

    New R = 255 - R
    New G = 255 - G
    New B = 255 - B

### 3. Brightness Adjustment
<img src="./assets/brightness-adjustment.jpg" alt="Brightness adjusted image" width="300" />

    New R = R * level
    New G = G * level
    New B = B * level
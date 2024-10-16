
## **1. `image_prep(path)`**
This function loads an image from a given path, **preprocesses it**, and **labels individual cells**.

### **Steps:**
1. **Load Image in Grayscale:**  
   ```python
   img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
   ```
   The input image is read in **grayscale mode** using `cv2`.

2. **Edge Detection using Canny:**  
   ```python
   edges = canny(img / 255.)
   ```
   Canny edge detection is applied to detect the boundaries of objects (cells) in the image.

3. **Fill Holes:**  
   ```python
   fill_img = ndi.binary_fill_holes(edges)
   ```
   The detected edges are filled to create complete shapes for each cell.

4. **Labeling Objects:**  
   ```python
   label_objects, nb_labels = ndi.label(fill_img)
   ```
   This step assigns **labels** to each connected component (cell) in the binary image.

5. **Filtering Small Objects:**  
   ```python
   mask_sizes = sizes > mask_size
   mask_sizes[0] = 0
   img_cleaned = mask_sizes[label_objects]
   ```
   It filters out small objects (noise) by keeping only the ones **greater than a given size threshold (400 pixels)**.

6. **Label the Cleaned Image:**  
   ```python
   labeled_img, num_features = ndi.label(img_cleaned)
   return labeled_img, num_features
   ```
   Finally, the cleaned image is labeled again, and the **number of detected features** (cells) is returned along with the labeled image.

---

## **2. `numofneighbour(mat, i, j, searchValue)`**
This function **counts the number of neighboring pixels** around a given pixel `(i, j)` that match a specified value (`searchValue`).

### **How it works:**
- **Checks the four neighbors** (up, down, left, right) of the pixel `(i, j)`.
- If a neighbor has the same value as the **`searchValue`**, it increments the counter.

This function is used to help calculate the **perimeter** of cells.

---

## **3. `findperimeter(mat, num_features)`**
This function calculates the **perimeter** of each labeled cell in the matrix.

### **How it works:**
- It loops through all pixels in the matrix.  
- If a pixel belongs to a cell (i.e., it has a non-zero value), it adds to the perimeter based on the **number of empty neighbors** around it.  
  ```python
  perimeter[mat[i][j]] += (4 - numofneighbour(mat, i, j, mat[i][j]))
  ```
- Each pixel can contribute up to **4 units** to the perimeter. For every neighboring pixel with the same value, the contribution is reduced by **1 unit**.

---

## **4. `extract_area_perim(img, num_features)`**
This function calculates the **area and perimeter** for each detected cell in the labeled image.

### **How it works:**
1. **Calculate Area:**  
   - For each pixel in the matrix, it increments the **area** of the corresponding labeled cell.

2. **Calculate Perimeter:**  
   - Calls `findperimeter()` to calculate the **perimeter** for each labeled cell.

3. **Return Area and Perimeter:**  
   - The function returns two lists: one with the **areas** and one with the **perimeters** of the cells.

---

## **5. `extract_circularity(area, perimeter)`**
This function calculates the **circularity** of each cell using the formula:

   \[
   \text{circularity} = \frac{4 \times \pi \times \text{area}}{\text{perimeter}^2}
   \]

### **How it works:**
1. **Iterate over each cell** to compute its circularity using the above formula.
2. **Return a list** with the circularity values for all the cells.

**Note:**  
A **circularity close to 1** indicates a perfect circle. Sickle cells will typically have **lower circularity** values compared to healthy circular red blood cells.

---

## **6. `convert_to_relative(cellAreas, cellPerims)`**
This function **normalizes the areas and perimeters** of the cells by converting them to **relative values** based on the average size.

### **How it works:**
1. **Calculate the average area and perimeter:**  
   ```python
   averageCellSize = np.mean(cellAreas)
   averagePerimSize = np.mean(cellPerims)
   ```
2. **Normalize each area and perimeter:**  
   Each value is divided by the corresponding average:
   ```python
   relativeArea[i] = cellAreas[i] / averageCellSize
   relativePerim[i] = cellPerims[i] / averagePerimSize
   ```
3. **Return the normalized (relative) values** as lists.

---

## **7. `removeFromImg(img, feature)`**
This function **removes a specific labeled cell** from the image by setting its pixel values to **0** (background).

### **How it works:**
1. **Iterate over all pixels** in the matrix.
2. **Set to 0** (background) if the pixel value matches the given `feature` label.

This function is useful for **removing outliers** from the image.

---

## **8. `removeOutliers(area, perim, img)`**
This function **removes outlier cells** based on their **area**.

### **How it works:**
1. **Calculate the mean and standard deviation** of the areas:
   ```python
   mean = np.mean(area)
   std = np.std(area)
   ```
2. **Identify and remove outliers:**  
   - If a cell’s area is greater than `mean + 3.5 * std`, it is considered an **outlier**.
   - The corresponding **area, perimeter**, and **labeled cell in the image** are removed.
   - It uses the `removeFromImg()` function to remove the outlier from the image.

3. **Return the updated lists** (areas, perimeters) and the modified image.

---

## **Summary of Functions**

1. **`image_prep(path)`**:  
   - Loads, preprocesses, and labels cells in the input image.

2. **`numofneighbour(mat, i, j, searchValue)`**:  
   - Counts neighboring pixels with a specific value.

3. **`findperimeter(mat, num_features)`**:  
   - Calculates the perimeter of each labeled cell.

4. **`extract_area_perim(img, num_features)`**:  
   - Extracts the area and perimeter of each cell.

5. **`extract_circularity(area, perimeter)`**:  
   - Computes the circularity of each cell.

6. **`convert_to_relative(cellAreas, cellPerims)`**:  
   - Normalizes areas and perimeters relative to their averages.

7. **`removeFromImg(img, feature)`**:  
   - Removes a specific labeled cell from the image.

8. **`removeOutliers(area, perim, img)`**:  
   - Removes outliers based on area size.

This code provides all the necessary tools to **preprocess images, extract features, classify cells, and remove outliers**, forming the backbone of the Sickle Cell detection system.
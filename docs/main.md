## **1. Importing Modules and Files**

```python
from FeatureExtraction import *
from Tools import *
from LabelledData import *
from Classify import *
import sys
```

- **Imports:**  
  This script imports various modules that contain functions to perform **feature extraction, labeling, classification, and data processing.**

---

## **2. Handling Command-Line Arguments**

```python
if(len(sys.argv) < 2):
    print("Error: Please include image path in argument")
    exit()
if(len(sys.argv) > 2):
    print("Error: Only one argument allowed")
    exit()
imagePath = str(sys.argv[1])
```

- **Command-Line Arguments:**  
  The script expects **one argument**: the **path to the image** to be analyzed.  
  - If no path or more than one argument is provided, the program exits with an error message.

---

## **3. Displaying the Original Image**

```python
plt.figure("Original Image")
try:
    plt.imshow(cv2.imread(imagePath))
except:
    print("Error: Image path is not valid")
    exit()
```

- **Display Original Image:**  
  It tries to **load and display the original image** using `cv2.imread()` and `matplotlib`. If the **image path is invalid**, it prints an error and exits the program.

---

## **4. Image Preprocessing**

```python
result, num_features = image_prep(imagePath)
plt.figure("Prepped Image")
plt.imshow(result)
```

- **Image Preprocessing:**  
  The **`image_prep()`** function prepares the image by **converting it to grayscale, detecting edges, and labeling individual cells**.  
  - The **processed image** and the **number of detected cells (features)** are returned.
  - The processed image is displayed using `plt.imshow()`.

---

## **5. Feature Extraction: Area and Perimeter**

```python
areaArray, perimArray = extract_area_perim(result, num_features)

# Remove empty first elements
areaArray.pop(0)
perimArray.pop(0)
```

- **`extract_area_perim()`** extracts the **area and perimeter** of each labeled cell in the image.
- The **first element (corresponding to background pixels)** is removed from both arrays using `pop(0)`.

---

## **6. Calculating Circularity**

```python
circularityArray = extract_circularity(areaArray, perimArray)
```

- **`extract_circularity()`** calculates the **circularity** of each cell using the formula:

  \[
  \text{Circularity} = \frac{4 \times \pi \times \text{Area}}{\text{Perimeter}^2}
  \]

---

## **7. Normalizing Area and Perimeter**

```python
relativeAreaArray, relativePerimArray = convert_to_relative(areaArray, perimArray)
```

- **`convert_to_relative()`** normalizes the **area and perimeter values** by dividing each by their **average size**. This ensures that the values are **comparable across different cells.**

---

## **8. Loading Predefined Data**

```python
sickleData = getSickleData()
healthyData = getHealthyData()

combinedHealthySickle = sickleData
for i in range(len(healthyData)):
    combinedHealthySickle.append(healthyData[i])
```

- **`getSickleData()` and `getHealthyData()`** provide **preloaded datasets** containing feature vectors for known sickle and healthy cells.
- These datasets are **combined** to form a **training set** for the classifier.

---

## **9. Classifying the Cells**

```python
classified = KNNClassifier(combinedHealthySickle,
                           [1] * 12 + [0] * 40,
                           convertTo3D(relativeAreaArray, relativePerimArray, circularityArray),
                           3)
```

- **`KNNClassifier()`** uses the **K-Nearest Neighbors (KNN)** algorithm to classify each cell.
  - The combined training data (`combinedHealthySickle`) is used.
  - The labels are:  
    - **1** for sickle cells (12 known samples)  
    - **0** for healthy cells (40 known samples)
  - The features (area, perimeter, circularity) are converted into **3D feature vectors** using `convertTo3D()`.
  - **K=3** nearest neighbors are used for the classification.

---

## **10. Creating a 3D Plot**

```python
fig = plt.figure("Classified Graph")
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Circularity')
```

- **3D Plot Setup:**  
  A **3D scatter plot** is created to visualize the cells based on **area, perimeter, and circularity.**

---

## **11. Plotting the Classified Cells**

```python
numSickleCells = 0
for i in range(len(classified) - 1, -1, -1):
    if classified[i] == 1:
        numSickleCells += 1
        ax.scatter(relativeAreaArray.pop(i), relativePerimArray.pop(i), circularityArray.pop(i), c="red")

# Plot remaining healthy cells
ax.scatter(relativeAreaArray, relativePerimArray, circularityArray)
```

- **Counting and Plotting Sickle Cells:**  
  - The **sickle cells (classified as 1)** are plotted in **red** and counted.
  - The remaining **healthy cells** are plotted in the default color.

---

## **12. Displaying the Sickle Cells in the Image**

```python
displaySickleImage(result, classified)
```

- **`displaySickleImage()`** highlights the **sickle cells** in the image based on the classification results and displays the image.

---

## **13. Printing Statistics**

```python
print("Total Cells: ", num_features)
print("Sickle Cells: ", numSickleCells)
print("Healthy Cells: ", num_features - numSickleCells)
print("Percent Sickle: ", (numSickleCells / num_features) * 100, "%")
print("Percent Healthy: ", ((num_features - numSickleCells) / num_features) * 100, "%")
```

- **Statistics Output:**  
  The program prints:
  - Total number of cells
  - Number of sickle and healthy cells
  - Percentage of sickle and healthy cells

---

## **14. Displaying All Plots**

```python
plt.show()
```

- **`plt.show()`** displays all the figures generated during the program's execution.

---

### **Summary**

This **main script** loads an image, preprocesses it to detect individual cells, extracts relevant features (area, perimeter, circularity), and classifies the cells as either **sickle or healthy** using a **KNN classifier**. The results are displayed through **3D plots, images, and printed statistics**, helping the user understand the distribution of sickle and healthy cells in the sample.
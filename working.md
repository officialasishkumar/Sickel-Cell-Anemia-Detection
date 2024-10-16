# **Sickle Cell Anemia Detection System**

## **Overview**

This project provides a **computer vision-based solution** for detecting and classifying red blood cells from microscopic images. The goal is to identify **sickle cells** among healthy red blood cells, offering diagnostic insights into **Sickle Cell Disease (SCD)**. The system utilizes feature extraction, classification, and visualization to quantify the number and type of cells.

---

## **Features**

- **Image Analysis:** Automatically analyzes a provided image of blood cells.
- **Cell Classification:** Differentiates between healthy cells and sickle-shaped cells.
- **Percentage Calculation:** Computes and displays the percentage of sickle and healthy cells.
- **Visualization:** Generates multiple visualizations to provide deeper insights into the analyzed data.

---

## **How It Works**

The system is executed with the following command:

```bash
python3 src/main.py /path/to/image/sickle4.jpg
```

This command triggers a series of operations, including image processing, classification, and visualization. The system outputs four key visualizations in separate dialog boxes.

---

## **Generated Visualizations**

Here is a breakdown of the **four visual outputs** generated when you run the code:

### 1. **Original Image**
![Original Image](image.png)

- **Description:** This is the unprocessed input image of red blood cells as captured from the microscope.
- **Purpose:** Provides a baseline to visually inspect the raw state of the cells before further processing.
- **Inference:** From this image, you can manually identify the cells that appear sickle-shaped and compare them with the automated results.

---

### 2. **Preprocessed Image**
![Preprocessed Image](image.png)

- **Description:** This image shows the result of the preprocessing stage, where individual cells are segmented and labeled with different colors.
- **Purpose:** Helps ensure that the segmentation process is working correctly by visually separating individual cells.
- **Inference:** Cells are isolated based on their boundaries, allowing the feature extraction algorithm to calculate shape parameters like area, perimeter, and circularity.

---

### 3. **Classified Image**
![Classified Image](image.png)

- **Description:** This image highlights only the **classified sickle cell(s)** in bright yellow, distinguishing them from other cells.
- **Purpose:** Provides a focused view of detected sickle cells to verify the classification accuracy.
- **Inference:** This helps the user visually confirm that the correct cells are flagged as sickle-shaped.

---

### 4. **3D Scatter Plot (Classified Graph)**
![3D Scatter Plot](image.png)

- **Axes:**
  - **X-Axis:** Area of the cell
  - **Y-Axis:** Perimeter of the cell
  - **Z-Axis:** Circularity of the cell

- **Description:** This scatter plot shows the distribution of individual cells based on key geometric properties (area, perimeter, and circularity). Sickle cells are highlighted in **red**.
- **Purpose:** Offers deeper insights into the dataset by visualizing how cells cluster based on their shape properties.
- **Inference:** 
  - **Blue points**: Healthy red blood cells with circular shapes.
  - **Red points**: Sickle-shaped cells detected by the algorithm.
  - This visualization helps assess the feature space used for classification.

---

## **How to Interpret the Results**

After running the command, the following outputs are printed on the terminal along with the visualizations:

```
Total Cells: 12
Sickle Cells: 1
Healthy Cells: 11
Percent Sickle: 8.33%
Percent Healthy: 91.67%
```

- **Total Cells:** The total number of cells detected in the image.
- **Sickle Cells:** The number of cells identified as sickle-shaped.
- **Healthy Cells:** The number of cells identified as normal.
- **Percent Sickle:** Percentage of sickle cells out of the total.
- **Percent Healthy:** Percentage of healthy cells out of the total.

### **Inference from Results:**

- **High percentage of sickle cells:** Indicates the presence of Sickle Cell Disease.
- **Low percentage of sickle cells:** Suggests a healthy sample, or a mild occurrence of sickle cells.
- **3D Graph interpretation:** The outliers in red (sickle cells) show distinctive differences in circularity and shape, explaining why they are flagged as abnormal.

---

## **How It Works Internally**

1. **Preprocessing:** The input image is preprocessed by converting it to grayscale and applying filters to isolate individual cells.
2. **Feature Extraction:** Key properties such as **area**, **perimeter**, and **circularity** are computed for each cell.
3. **Classification:** A machine learning classifier uses the extracted features to distinguish between healthy and sickle cells.
4. **Visualization:** Four images are generated to assist in verifying the analysis.


## **Conclusion**

This project provides a comprehensive solution for detecting and classifying sickle cells from blood smear images. With its multiple visual outputs and automated classification, it offers a valuable tool for medical professionals working on **Sickle Cell Disease** diagnosis. The 3D scatter plot provides further insights into the distribution of cells based on shape properties, making it a powerful visualization tool for researchers.

---

This documentation covers the entire project functionality, including how to install, use, and interpret the results. Let me know if you need any more customization!
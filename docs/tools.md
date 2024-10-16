

### **1. `printArray(message, array)`**
This function prints a given **array** along with a **custom message**.

#### **How it works:**
- It prints the `message` followed by each element in the `array` with its **index**.
- All elements are printed in a **single line** separated by commas.

#### **Example Output:**
```plaintext
Array: 0 1.23, 1 3.45, 2 5.67, 
```

---

### **2. `highlightCell(img, number)`**
This function **highlights a specific labeled cell** in the given image by setting all its pixels to **240** (bright value).

#### **How it works:**
- It takes an **image matrix** (`img`) and a **cell label** (`number`).
- It **iterates over every pixel** in the matrix. If the pixel belongs to the specified cell (i.e., the pixel value equals the `number`), it **sets that pixel value to 240**.
- The modified matrix is returned.

#### **Usage:**
- This function helps in **highlighting a specific labeled cell** by changing its pixel values to a bright value (240), making it stand out in the image.

---

### **3. `displayAllImages(img, num_features)`**
This function **displays each labeled cell separately** using `matplotlib`.

#### **How it works:**
- It loops over all the **cell labels** from `1` to `num_features`.
- For each label, it calls `highlightCell()` to highlight the specific cell.
- It then **displays the highlighted cell** using `plt.imshow()`.

#### **Usage:**
- This function is useful for **visualizing all cells one by one** to inspect them individually.

---

### **4. `displaySickleImage(img, array)`**
This function **highlights only the sickle cells** from the labeled image based on an input **array of classifications**.

#### **How it works:**
- It iterates over the `array` of classifications (where **1** indicates a sickle cell and **0** indicates a healthy cell).
- For each **sickle cell (1)**, it calls `highlightCell()` to highlight it in the image.
- After processing all cells, it **displays the modified image** using `plt.imshow()`.

#### **Usage:**
- This function is useful for **visualizing only the sickle cells**, helping to validate the classification visually.

---

### **5. `convertTo3D(areaArray, perimArray, circularityArray)`**
This function **converts multiple 1D arrays into a 3D array** of feature vectors.

#### **How it works:**
- It takes three 1D arrays: `areaArray`, `perimArray`, and `circularityArray`.
- It **combines corresponding elements** from each array into a **3D feature vector** (a list with three values).
- The result is a **list of 3D vectors**, where each vector contains:
  - **Area**  
  - **Perimeter**  
  - **Circularity**

#### **Example Output:**
```python
[[1.2, 3.4, 0.5], [2.3, 4.5, 0.6], [1.8, 3.1, 0.7]]
```

#### **Usage:**
- This function prepares the data for the **KNN classifier** by organizing the features into 3D vectors.

---

## **Summary**

- **`printArray()`**: Prints an array with a custom message.
- **`highlightCell()`**: Highlights a specific cell by changing its pixel values to 240.
- **`displayAllImages()`**: Displays all labeled cells one by one.
- **`displaySickleImage()`**: Displays only the **sickle cells** in the image.
- **`convertTo3D()`**: Converts multiple feature arrays into a list of **3D feature vectors** for classification.

These functions form the **visualization and data preparation components** of the system, making it easy to inspect individual cells and prepare data for further processing.
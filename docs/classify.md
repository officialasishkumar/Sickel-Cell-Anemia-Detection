### **1. `findShortestDistance(array, outputSize)`**
This function finds the **smallest values** from a given list (`array`), and it keeps only the **smallest `outputSize` elements**. 

#### **How it works:**
- It loops over each element in the input `array`.
- For each element, it tries to insert it into the right position within the **result list** (sorted based on the smallest values).
- If the **result list** becomes too big (larger than `outputSize`), it removes the extra elements to keep it at the right size.

#### **What it does:**
- It’s used to **pick the closest distances** (smallest numbers) from a list of distances between points.

---

### **2. `KNNClassifier(features, labels, predictionSet, nNeighbors)`**
This function is an **implementation of the K-Nearest Neighbors (KNN) algorithm**. It compares some new data points (called the `predictionSet`) with a set of **existing points** (called `features`) to classify them as **sickle cells (1)** or **healthy cells (0)**.

#### **How it works:**
1. **Calculate distances**:  
   For every new point in the `predictionSet`, it calculates the **distance** to all the known points in `features`.  
   - It uses the **Euclidean distance formula** (distance between two points in 3D space).

2. **Find the nearest neighbors**:  
   For each point in `predictionSet`, it picks the **`nNeighbors` closest points** using the `findShortestDistance()` function.

3. **Classify the point**:  
   - For the nearest points, it counts how many are labeled as **healthy (0)** and how many as **sickle (1)**.
   - If more neighbors are healthy, the point is classified as **healthy (0)**.  
   - If more neighbors are sickle, the point is classified as **sickle (1)**.

4. **Return the results**:  
   It gives back a list where each element is **0 or 1** indicating whether the corresponding point in the `predictionSet` is healthy or sickle.

---

### **Summary:**
1. **`findShortestDistance()`**:  
   Finds the smallest (closest) distances and keeps only the required number.

2. **`KNNClassifier()`**:  
   Uses **KNN logic** to classify new points based on their distances to known points, assigning them as **healthy (0)** or **sickle (1)**.
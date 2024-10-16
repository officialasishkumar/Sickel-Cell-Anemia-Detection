
# Sickle Cell Anemia Detection

This project provides an automated solution for detecting and classifying red blood cells from images. It identifies healthy and sickle cells, offering percentage-based results. The solution leverages computer vision and machine learning for fast and accurate analysis, aiding in the diagnosis of Sickle Cell Disease (SCD).

## Installation

Follow the steps below to set up and run the project:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Sickel-Cell-Anemia-Detection
   ```

2. **Create a virtual environment:**
   ```bash
   virtualenv sickel-cell
   ```

3. **Activate the virtual environment:**
   - **Linux/macOS:**
     ```bash
     source sickel-cell/bin/activate
     ```
   - **Windows:**
     ```cmd
     .\sickel-cell\Scripts\activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install .
   ```

---

## Usage

Once installed, you can run the project with the following command:

```bash
python3 src/main.py <path-to-image>
```

### Example:

```bash
python3 src/main.py image/sickle4.jpg        
```

#### Output:

```
Total Cells: 12
Sickle Cells: 1
Healthy Cells: 11
Percent Sickle: 8.33%
Percent Healthy: 91.67%
```

---

## Dependencies

The project uses the following Python libraries:
- `numpy`
- `opencv-python`
- `matplotlib`
- `scikit-image`
- `scikit-learn`
- `Pillow`

These dependencies are automatically installed when you run `pip install .` within the virtual environment.


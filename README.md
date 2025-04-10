Here you go, Aswin! Below is a complete and clean `README.md` for a GitHub repository that provides **DICOM to NIfTI conversion using `dcm2niix`** via Python. It includes a proper title, description, installation, usage instructions, and a special note on using **Kaggle** for DICOM datasets.

---

```markdown
# 🧠 DICOM to NIfTI Converter using dcm2niix

Convert medical imaging files from **DICOM (.dcm)** format to **NIfTI (.nii / .nii.gz)** using Python and the powerful **dcm2niix** tool. Ideal for MRI, CT scan research, and preprocessing pipelines in AI/ML models.

---

## 📦 Features

- Converts entire DICOM folders into compressed NIfTI files
- Python script powered by `subprocess` calling `dcm2niix`
- Supports both `.nii` and `.nii.gz` outputs
- Clean and user-friendly CLI-like behavior
- Works on **local**, **Google Colab**, and even **Kaggle Notebooks**

---

## 🛠 Installation

### ✅ If you're using **Anaconda** (recommended):

```bash
conda install -c conda-forge dcm2niix
```

### ✅ Or using **pip + system package (Linux/Colab)**:

```bash
# On Ubuntu / Colab:
!apt-get install -y dcm2niix
```

---

## 💻 Python Usage

```python
import subprocess
import os

def convert_dicom_to_nifti(input_dicom_folder, output_nifti_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_nifti_folder, exist_ok=True)

    # dcm2niix command configuration
    command = [
        'dcm2niix',
        '-z', 'y',                   # Compress to .nii.gz (use 'n' for .nii)
        '-o', output_nifti_folder,  # Output directory
        '-f', '%p_%s',              # Output filename format
        input_dicom_folder          # Input DICOM folder
    ]

    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Display output
    print("Output:\n", result.stdout)
    print("Errors:\n", result.stderr)

# Example
convert_dicom_to_nifti('/path/to/dicom_folder', '/path/to/output_folder')
```

---

## 📁 Directory Structure

```
your-project/
├── dicom_to_nifti.py     # Python script
├── README.md
├── input_dicom/          # Put your DICOM files here
└── output_nifti/         # NIfTI files will be saved here
```

---

## 🧪 Testing on Google Colab

```python
!apt install -y dcm2niix

from google.colab import drive
drive.mount('/content/drive')

# Example usage after mounting
convert_dicom_to_nifti('/content/drive/MyDrive/DICOMs', '/content/drive/MyDrive/NIfTI_Converted')
```

---

## 📌 Kaggle Note

If you're working with **Kaggle DICOM datasets**, such as:

- RSNA Pneumonia Detection Challenge
- Brain MRI segmentation datasets

You can download and unzip datasets using:

```python
!pip install kaggle

# Upload kaggle.json for API
from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Download example dataset
!kaggle datasets download -d milesh1/brain-tumor-mri-dataset
!unzip brain-tumor-mri-dataset.zip -d dicom_input/
```

Then use the script to convert as shown above.

---

## 📚 References

- [dcm2niix GitHub](https://github.com/rordenlab/dcm2niix)
- [NIfTI Format Info](https://nifti.nimh.nih.gov/)
- [Kaggle DICOM Datasets](https://www.kaggle.com/datasets?search=dicom)

---

## 🧑‍💻 Author

**Aswin Thulasi R**  
_Full Stack | Medical Imaging Enthusiast | MERN & Python Dev_

---

## 📜 License

MIT License - Free for personal and commercial use

```

---

Let me know if you'd like a ready-to-push folder with the Python script + `README.md` or want this as a Colab notebook instead.

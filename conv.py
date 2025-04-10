import subprocess
import os

def convert_dicom_to_nifti(input_dicom_folder, output_nifti_folder):
    # Make sure output folder exists
    os.makedirs(output_nifti_folder, exist_ok=True)

    # Construct the dcm2niix command
    command = [
        'dcm2niix',
        '-z', 'y',                  # Compress output as .nii.gz
        '-o', output_nifti_folder,  # Output folder
        '-f', '%p_%s',              # Output filename format
        input_dicom_folder          # Input DICOM folder
    ]

    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print output and error (if any)
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)

# Example usage
dicom_folder = './dicom'        
output_folder = './nifti'

convert_dicom_to_nifti(dicom_folder, output_folder)

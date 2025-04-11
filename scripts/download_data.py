#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script downloads the Anthropic Economic Index dataset from Hugging Face
and organizes it into the appropriate directories.
"""

import os
import shutil
from pathlib import Path
from huggingface_hub import hf_hub_download, snapshot_download

# Define repository information
REPOSITORY_ID = "Anthropic/EconomicIndex"
FILES_TO_DOWNLOAD = [
    # 2025-03-27 Release
    "release_2025_03_27/automation_vs_augmentation_by_task.csv",
    "release_2025_03_27/SOC_Structure.csv",
    "release_2025_03_27/onet_task_statements.csv",
    "release_2025_03_27/task_thinking_fractions.csv",
    "release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv",
    "release_2025_03_27/v2_report_replication.ipynb",
]

# Define output directory structure
BASE_DIR = Path("data")
RAW_DIR = BASE_DIR / "raw"
PROCESSED_DIR = BASE_DIR / "processed"


def main():
    """Main function to download dataset files."""
    # Create directories if they don't exist
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    print(f"Downloading files from {REPOSITORY_ID}...")
    
    # Download individual files
    for file_path in FILES_TO_DOWNLOAD:
        target_path = RAW_DIR / os.path.basename(file_path)
        
        # Download the file
        downloaded_path = hf_hub_download(
            repo_id=REPOSITORY_ID,
            filename=file_path,
            repo_type="dataset",
            cache_dir=".cache"
        )
        
        # Copy to our data directory
        shutil.copy(downloaded_path, target_path)
        print(f"Downloaded {file_path} to {target_path}")
    
    print("\nDownload complete!")
    print(f"Files saved to {RAW_DIR}")
    print("\nNext steps:")
    print("1. Explore the raw data in the Jupyter notebooks")
    print("2. Run data processing scripts to prepare the data for analysis")


if __name__ == "__main__":
    main()

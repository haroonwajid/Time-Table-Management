import pandas as pd

# File paths
file_paths = {
    'echonest': 'fma_metadata/echonest.csv',
    'features': 'fma_metadata/features.csv',
    'genres': 'fma_metadata/genres.csv',
    'raw_albums': 'fma_metadata/raw_albums.csv',
    'raw_artists': 'fma_metadata/raw_artists.csv',
    'raw_echonest': 'fma_metadata/raw_echonest.csv',
    'raw_genres': 'fma_metadata/raw_genres.csv',
    'raw_tracks': 'fma_metadata/raw_tracks.csv',
    'tracks': 'fma_metadata/tracks.csv'
}

# Dictionary to hold DataFrames
data = {}

# Read CSV files into DataFrames
for key, path in file_paths.items():
    try:
        # Specify dtype as object to avoid DtypeWarning
        data[key] = pd.read_csv(path, dtype=object)
        print(f"Read {path}")
    except FileNotFoundError:
        print(f"File {path} not found")

# Print the first few rows of each DataFrame
for key, df in data.items():
    print(f"\n{key}:")
    print(df.head())

import os
import random

# Path to the chosen fma_large folder
fma_large_folder = "fma_large"

# Number of subfolders to select
num_subfolders = 63

# List to hold paths to selected audio files
selected_audio_files = []

# Iterate through subfolders and select a subset
subfolders = random.sample(os.listdir(fma_large_folder), num_subfolders)
for subfolder in subfolders:
    subfolder_path = os.path.join(fma_large_folder, subfolder)
    for root, dirs, files in os.walk(subfolder_path):
        for file in files:
            if file.endswith(".mp3"):
                selected_audio_files.append(os.path.join(root, file))

# Print the number of selected audio files
print(f"Total selected audio files: {len(selected_audio_files)}")

import os
import librosa
import numpy as np

# Function to extract features from an audio file
def extract_features(file_path):
    try:
        # Load audio file
        y, sr = librosa.load(file_path, duration=30)
        
        # Extract features
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
        
        # Flatten features
        mfcc_flat = mfcc.flatten()
        spectral_centroid_flat = spectral_centroid.flatten()
        zero_crossing_rate_flat = zero_crossing_rate.flatten()
        
        # Concatenate features
        features = np.concatenate((mfcc_flat, spectral_centroid_flat, zero_crossing_rate_flat))
        
        return features
    except Exception as e:
        # If there's an error, return None
        return None

# Path to the chosen fma_large folder
fma_large_folder = "fma_large"

# List to hold paths to selected audio files
selected_audio_files = []

# Iterate through each subfolder and collect all MP3 files
for root, dirs, files in os.walk(fma_large_folder):
    for file in files:
        if file.endswith(".mp3"):
            selected_audio_files.append(os.path.join(root, file))

# Print the number of selected audio files
print(f"Total selected audio files: {len(selected_audio_files)}")

# List to hold features of all audio files
all_features = []

# Keep track of the current subfolder being processed
current_subfolder = None

# Iterate through each audio file and extract features
for audio_file in selected_audio_files:
    # Get the subfolder name
    subfolder = os.path.basename(os.path.dirname(audio_file))
    
    # If subfolder changes, print a message
    if current_subfolder != subfolder:
        if current_subfolder is not None:
            print(f"|----Features extracted for fma_large1/{current_subfolder} folder----|")
        current_subfolder = subfolder
    
    features = extract_features(audio_file)
    if features is not None:
        all_features.append(features)

# Print the final message for the last subfolder
if current_subfolder is not None:
    print(f"|----Features extracted for fma_large1/{current_subfolder} folder----|")

# Convert the list of features to a numpy array
all_features = np.array(all_features)

# Print the size of all_features
print(f"Features of {len(all_features)} files have been extracted successfully.")


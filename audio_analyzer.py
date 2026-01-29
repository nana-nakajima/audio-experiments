#!/usr/bin/env python3
"""
🎵 Nana's Simple Audio Analyzer
Audio waveform and basic analysis tool
"""

import sys
import os

try:
    import librosa
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("📦 Installing dependencies...")
    os.system("pip install librosa matplotlib numpy -q")
    import librosa
    import matplotlib.pyplot as plt
    import numpy as np

def analyze_audio(file_path, output_dir="output"):
    """Analyze audio file and create visualization"""
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🎵 Analyzing: {file_path}")
    
    # Load audio
    y, sr = librosa.load(file_path, duration=30)  # Load first 30 seconds
    
    # Get basic info
    duration = librosa.get_duration(y=y, sr=sr)
    print(f"📊 Duration: {duration:.2f} seconds")
    print(f"🎚️ Sample rate: {sr} Hz")
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Waveform
    plt.subplot(2, 2, 1)
    plt.plot(y, color='purple', alpha=0.7)
    plt.title('🎵 Waveform')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    
    # Spectrogram
    plt.subplot(2, 2, 2)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='viridis')
    plt.colorbar(format='%+2.0f dB')
    plt.title('🔊 Spectrogram')
    
    # MFCC (Mel-frequency cepstral coefficients)
    plt.subplot(2, 2, 3)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    librosa.display.specshow(mfccs, sr=sr, x_axis='time', cmap='coolwarm')
    plt.colorbar()
    plt.title('🎤 MFCC Features')
    
    # Zero crossing rate
    plt.subplot(2, 2, 4)
    zcr = librosa.feature.zero_crossing_rate(y)
    plt.plot(zcr[0], color='green')
    plt.title('🔄 Zero Crossing Rate')
    plt.xlabel('Frames')
    plt.ylabel('Rate')
    
    plt.tight_layout()
    
    # Save
    output_file = os.path.join(output_dir, os.path.basename(file_path).replace('.', '_') + '.png')
    plt.savefig(output_file, dpi=100, bbox_inches='tight')
    print(f"💾 Saved: {output_file}")
    
    # Print summary
    print(f"\n✨ Analysis Complete!")
    print(f"📁 Output: {output_file}")
    
    # Cleanup
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🎵 Nana's Audio Analyzer")
        print("Usage: python audio_analyzer.py <audio_file>")
        print("Example: python audio_analyzer.py mysong.mp3")
        print("\n💡 Drop audio files in the 'samples' folder and run!")
    else:
        analyze_audio(sys.argv[1])

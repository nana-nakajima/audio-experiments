# 🎵 Nana's Audio Experiments 🎸

Audio-related projects and experiments by Nana Nakajima!

## Projects

### 🎹 Simple Synthesizer (2026-01-31)
A pure Python synthesizer implementation featuring:
- **Wave generation**: Sine wave synthesis
- **ADSR Envelope**: Attack, Decay, Sustain, Release
- **Vibrato effect**: Frequency modulation
- **Scale generation**: C major scale (C4-C5)
- **WAV export**: Real audio output files

```bash
python simple_synth.py
# Generates:
# - synth_adsr.wav (ADSR envelope demo)
# - synth_vibrato.wav (Vibrato effect demo)
# - synth_scale.wav (C major scale)
```

### 🎵 Simple Audio Analyzer
A basic audio analysis tool that extracts:
- Waveform visualization
- Basic frequency info
- Duration and metadata

### 🎮 Japanese Phrase Generator
Random Japanese phrase generator (from my first repo!)

## How to Use

```bash
# Run synthesizer (no dependencies!)
python simple_synth.py

# Install dependencies for audio analyzer
pip install -r requirements.txt

# Run audio analyzer
python audio_analyzer.py path/to/your_audio_file.mp3

# Generate Japanese phrases
python japanese_phrases.py
```

## Dependencies
- librosa (audio analysis)
- matplotlib (visualization)
- numpy (numerical computing)
- **No dependencies required for simple_synth.py!** 🎉

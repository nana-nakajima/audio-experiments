#!/usr/bin/env python3
"""
Simple Synthesizer - 基础合成器实践
学习内容：ADSR包络、音色合成、基本音频生成
"""

import math
import struct
import wave

# 配置
SAMPLE_RATE = 44100  # 采样率
DURATION = 2.0       # 持续时间（秒）
FREQUENCY = 440.0    # A4音高

def generate_sine_wave(freq, duration, sample_rate=44100):
    """生成正弦波"""
    samples = []
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        value = math.sin(2 * math.pi * freq * t)
        samples.append(int(value * 32767))
    return samples

def apply_adsr_envelope(samples, sample_rate, attack=0.1, decay=0.2, sustain=0.7, release=0.3):
    """应用ADSR包络"""
    length = len(samples)
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = length - attack_samples - decay_samples - release_samples
    
    result = []
    for i, sample in enumerate(samples):
        # ADSR计算
        if i < attack_samples:
            # Attack: 0 -> 1
            envelope = i / attack_samples
        elif i < attack_samples + decay_samples:
            # Decay: 1 -> sustain
            progress = (i - attack_samples) / decay_samples
            envelope = 1 - (1 - sustain) * progress
        elif i < attack_samples + decay_samples + sustain_samples:
            # Sustain: 保持sustain水平
            envelope = sustain
        else:
            # Release: sustain -> 0
            progress = (i - attack_samples - decay_samples - sustain_samples) / release_samples
            envelope = sustain * (1 - progress)
        
        result.append(int(sample * envelope))
    
    return result

def apply_vibrato(samples, sample_rate, freq=5.0, depth=0.02):
    """应用颤音效果"""
    result = []
    for i, sample in enumerate(samples):
        t = i / sample_rate
        modulation = 1 + depth * math.sin(2 * math.pi * freq * t)
        result.append(int(sample * modulation))
    return result

def save_wav(filename, samples, sample_rate=44100):
    """保存为WAV文件"""
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # 单声道
        wav_file.setsampwidth(2)  # 16位
        wav_file.setframerate(sample_rate)
        for sample in samples:
            wav_file.writeframes(struct.pack('<h', sample))

def main():
    print("🎹 Simple Synthesizer Practice")
    print("=" * 40)
    print(f"生成参数:")
    print(f"  - 频率: {FREQUENCY} Hz (A4)")
    print(f"  - 时长: {DURATION} 秒")
    print(f"  - 采样率: {SAMPLE_RATE} Hz")
    print()
    
    # 1. 生成基础正弦波
    print("1. 生成正弦波...")
    sine_wave = generate_sine_wave(FREQUENCY, DURATION)
    
    # 2. 应用ADSR包络
    print("2. 应用ADSR包络...")
    print("   Attack: 0.1s, Decay: 0.2s, Sustain: 0.7, Release: 0.3s")
    adsr_wave = apply_adsr_envelope(sine_wave, SAMPLE_RATE)
    
    # 3. 应用颤音
    print("3. 应用颤音效果...")
    print("   颤音频率: 5Hz, 深度: 2%")
    vibrato_wave = apply_vibrato(adsr_wave, SAMPLE_RATE)
    
    # 4. 生成不同频率的音阶
    print("4. 生成C大调音阶...")
    notes = {
        'C4': 261.63,
        'D4': 293.66,
        'E4': 329.63,
        'F4': 349.23,
        'G4': 392.00,
        'A4': 440.00,
        'B4': 493.88,
        'C5': 523.25
    }
    
    scale_samples = []
    for note_name, freq in notes.items():
        note_samples = generate_sine_wave(freq, 0.5)
        note_samples = apply_adsr_envelope(note_samples, SAMPLE_RATE, 
                                           attack=0.05, decay=0.1, 
                                           sustain=0.6, release=0.2)
        scale_samples.extend(note_samples)
        print(f"   {note_name}: {freq} Hz")
    
    # 保存文件
    print()
    print("5. 保存音频文件...")
    save_wav('/tmp/synth_adsr.wav', adsr_wave)
    save_wav('/tmp/synth_vibrato.wav', vibrato_wave)
    save_wav('/tmp/synth_scale.wav', scale_samples)
    print("   ✅ /tmp/synth_adsr.wav")
    print("   ✅ /tmp/synth_vibrato.wav")
    print("   ✅ /tmp/synth_scale.wav")
    
    print()
    print("🎵 合成器实践完成！")
    print()
    print("学到的内容:")
    print("  1. 正弦波生成 - 基础波形")
    print("  2. ADSR包络 - Attack, Decay, Sustain, Release")
    print("  3. 颤音效果 - 频率调制")
    print("  4. 音阶生成 - 音乐理论实践")

if __name__ == "__main__":
    main()

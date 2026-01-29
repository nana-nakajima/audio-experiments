#!/usr/bin/env python3
"""
🎵 Nana's Simple Audio Visualizer
A fun audio visualization using pure Python!
"""

import random
import time
import os

def generate_waveform(length=50):
    """Generate a random waveform pattern"""
    return [random.randint(-20, 20) for _ in range(length)]

def generate_equalizer(bars=20):
    """Generate equalizer-style visualization"""
    return [random.randint(0, 30) for _ in range(bars)]

def display_visualizer(message="🎵 Nana's Audio Visualizer"):
    """Display ASCII audio visualizer"""
    print("\n" + "=" * 60)
    print(f"  {message}")
    print("=" * 60)
    print()
    
    for i in range(10):  # 10 frames
        eq = generate_equalizer()
        waveform = generate_waveform()
        
        # Draw equalizer
        bar_chars = " ▁▂▃▄▅▆▇█"
        eq_display = ""
        for height in eq:
            char_idx = min(height // 4, len(bar_chars) - 1)
            eq_display += bar_chars[char_idx]
        
        # Draw waveform
        wave_display = ""
        for amp in waveform:
            if amp > 10:
                wave_display += "▄"
            elif amp > 5:
                wave_display += "▁"
            elif amp < -10:
                wave_display += "▀"
            else:
                wave_display += "─"
        
        print(f"  {eq_display}")
        print(f"  {wave_display}")
        print()
        time.sleep(0.3)
    
    print("✨ Boom! 🎉")
    print()

def main():
    print("\n🎵 Nana's Simple Audio Visualizer 🎸")
    print("-" * 40)
    print("Press Enter to start visualization...")
    input()
    
    display_visualizer("🎧 Now Playing: Unknown Track 🎧")
    
    print("💡 Try creating your own audio visualization!")
    print("📁 Nana's GitHub: github.com/nana-nakajima/my-creations")

if __name__ == "__main__":
    main()

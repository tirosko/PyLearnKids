"""Generate a short 'bounce' sound effect and save it as bounce.wav.

Usage (PowerShell):
& C:/path/to/python.exe tools/generate_bounce_wav.py

This script creates a 16-bit PCM WAV file (44.1 kHz) named bounce.wav
in the current working directory.
"""
import math
import wave
import struct

OUTPUT = 'bounce.wav'
SAMPLE_RATE = 44100
DURATION = 0.28  # seconds

# Create a short decaying sine burst with a slight frequency glide
start_freq = 900.0
end_freq = 550.0

num_samples = int(SAMPLE_RATE * DURATION)

# Envelope: quick attack, exponential decay


def envelope(t):
    # t in [0,1]
    if t < 0.02:
        return t / 0.02  # linear attack 20 ms
    return math.exp(-6.0 * (t - 0.02))  # decay


frames = []
for n in range(num_samples):
    t = n / num_samples
    # linear frequency glide
    freq = start_freq + (end_freq - start_freq) * t
    phase = 2.0 * math.pi * freq * (n / SAMPLE_RATE)
    amp = envelope(n / num_samples)
    # Add a tiny amount of high-frequency "click" by mixing a short noise burst
    noise = (0.6 * (2.0 * (math.sin(8000.0 * (n / SAMPLE_RATE))))
             ) if n < 200 else 0.0
    sample = 0.7 * amp * math.sin(phase) + 0.03 * noise
    # clamp
    if sample > 1.0:
        sample = 1.0
    if sample < -1.0:
        sample = -1.0
    frames.append(int(sample * 32767.0))

with wave.open(OUTPUT, 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)  # 16-bit
    wf.setframerate(SAMPLE_RATE)
    wf.setnframes(num_samples)
    # pack frames as little-endian signed shorts
    wf.writeframes(struct.pack('<' + 'h'*len(frames), *frames))

print(f"Wrote {OUTPUT} — {DURATION}s, {SAMPLE_RATE} Hz")

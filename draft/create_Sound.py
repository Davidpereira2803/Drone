from pydub.generators import Sine
from pydub import AudioSegment

# Generate a 1-second sine wave tone at 440 Hz (A4 note)
tone = Sine(440).to_audio_segment(duration=500)  # duration in milliseconds

# Export the tone as an .mp3 file
tone.export("tone.mp3", format="mp3")

print("tone.mp3 has been created!")

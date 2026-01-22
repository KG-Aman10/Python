import pyjokes as PJ
import pyttsx3 as PT

# Initialize text-to-speech engine
engine = PT.init()

# Get a joke
joke = PJ.get_joke()

# Print joke
print(f"Joke:= {joke}")

# Speak joke
engine.say(f"Joke{joke}")
engine.runAndWait()

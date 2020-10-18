C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

noteAndOctave = input("Inserisci nota musicale: ")

# Notes are written in the form note, octave eg. C4
note = noteAndOctave[0].upper()
octave = int(noteAndOctave[1])

frequency = -1

if note == "C":
	frequency = C4
elif note == "D":
	frequency = D4
elif note == "E":
	frequency = E4
elif note == "F":
	frequency = F4
elif note == "G":
	frequency = G4
elif note == "A":
	frequency = A4
elif note == "B":
	frequency = B4
	
frequency /= 2 ** (4 - octave) # Formula to find the frequency in a different octave
	
print("La frequenza della nota è {0} Hz".format(frequency))


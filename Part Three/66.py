A = 4.0
A_MINUS = 3.7
B_PLUS = 3.5
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0

somma_voti = 0
n_voti = 0

line = None

while(line!=''):
    line = input("Inserisci voto(invio per uscire): ").upper()

    if line == 'A':
        somma_voti += A
        n_voti += 1
    elif line == 'A-':
        somma_voti += A_MINUS
        n_voti += 1
    elif line == 'B+':
        somma_voti += B_PLUS
        n_voti += 1
    elif line == 'B':
        somma_voti += B
        n_voti += 1
    elif line == 'B-':
        somma_voti += B_MINUS
        n_voti += 1
    elif line == 'C+':
        somma_voti += C_PLUS
        n_voti += 1
    elif line == 'C':
        somma_voti += C
        n_voti += 1
    elif line == 'C-':
        somma_voti += C_MINUS
        n_voti += 1
    elif line == 'D+':
        somma_voti += D_PLUS
        n_voti += 1
    elif line == 'D':
        somma_voti += D
        n_voti += 1
    elif line == 'F':
        somma_voti += F
        n_voti += 1



print("La media dei voti è: %.2f" %(somma_voti/n_voti))
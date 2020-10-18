BASE = 15.00
SMS_INCLUDED = 50
MINUTE_INCLUDED = 50
SMS_COST = 0.15
MINUTE_COST = 0.25
CALL_CENTER_COST  =0.44

minutes = int(input("Inserisci il numero di minuti di chiamate effettuate: "))
sms = int(input("Inserisci il numero degli sms: "))

extra_minutes_cost = 0
extra_sms_cost = 0

if minutes > 0:
    extra_minutes_cost = (minutes - MINUTE_INCLUDED) * MINUTE_COST

if sms > 0:
    extra_sms_cost = (sms - SMS_INCLUDED) * SMS_COST

subtotal = BASE + extra_sms_cost + extra_minutes_cost + CALL_CENTER_COST

tax = (subtotal * 5) /100
total = subtotal + tax 

print()
print("Costo base = $%.2f" %BASE)

if extra_minutes_cost > 0:
	print("Minuti aggiuntivi = $%.2f" %extra_minutes_cost)
if extra_sms_cost > 0:
	print("Sms aggiuntivi = $%.2f" %extra_sms_cost)

print("Costo call center = $%.2f" %CALL_CENTER_COST)
print("Tasse = $%.2f" %tax)
print()
print("Totale = $%.2f" %total)


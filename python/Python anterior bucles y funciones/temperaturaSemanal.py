temperaturaS=[]
tdiaria=""
td_l=tdiaria.lower()
media=0
while td_l!="fin":
    tdiaria=input("Agrega la temperatura. Escribe fin para terminar.\nSe mostraran aquellos días que superen los 25ºC\n")
    td_l= tdiaria.lower()
    if td_l!="fin":
        tdiaria=float(tdiaria)
        temperaturaS.append(tdiaria)
        media+=tdiaria
        n=0
        n+=1
media=media/n
print(f"La temperatura media es {media}")
m=0
for t in temperaturaS:
 m+=1
 if t>25:
    print(f"La {m}º=¨{t}ºC  es superior a 25ºC")
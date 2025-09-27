temperature = (int(input("какая у вас температура?")))
cloudy = (int(input("у вас солнечно? : 1-да, 2-нет")))
windy = (int(input("у вас ветренно?: 1-да, 2-нет")))
if temperature <= 10:
    jacket = "вам нужна куртка"
elif temperature > 10:
    jacket = "вам не нужна куртка"

if cloudy == 1:
    cap = "вам нужна кепка"
elif cloudy == 2:
    cap = "вам не нужна кепка"

if windy == 2:
    trousers = "вам нужны шорты"
elif windy == 1:
    trousers = "вам нужны штаны"

print(jacket)
print(cap)
print(trousers)
def noteiktDiapazonu(d1, d2, d3):
  rezultats = "skaitlis nav diapazona!"
  if d1 >= sk <= d2:
    rezultats = "Skaitlis ir diapazona!"
  return rezultats


d1 = int(input("Ievadi diapazona sakumu: "))
d2 = int(input("Ievadi diapazona beigas: "))
sk = int(input("Ievadi skaitli: "))
rez = noteiktDiapazonu(d1, d2, sk)
print(rez)
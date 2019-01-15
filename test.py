import re

string = "Ciao sono lorenzo"
saluto,verbo,nome = re.split(" ",string)
print(saluto)
print(verbo)
print(nome)

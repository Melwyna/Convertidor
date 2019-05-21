#Funciones de conversion de Decimal a Binario/Octal/Hexadecimal
def decimalabinario(a):

 binario = []

 while a > 0:
    binario.insert(0, a % 2)
    a = a // 2
 binario = "".join(str(i) for i in binario)
 return(binario)


def decimalaoctal(b):

 octal = []

 while b > 0:
    octal.insert(0, b % 8)
    b = b // 8
 octal = "".join(str(i) for i in octal)
 return(octal)


def decimalahexadecimal(b):

 hexadecimal = []
 while b > 0:
  hexadecimal.insert(0, b % 16)
  b = b // 16

 e=[]
 for h in hexadecimal:
  if h == 10:
    h = "A"
  if h == 11:
    h = "B"
  if h == 12:
    h = "C"
  if h == 13:
    h = "D"
  if h == 14:
    h = "E"
  if h == 15:
    h = "F"
  e.append(h)
 e="".join(str(i) for i in e)
 return (e)

#Funciones de conversion de Binario a Decimal/Octal/Hexadecimal
def binariodecimal(b):

    binario = []
    for i in b:
     binario.append(int(i))
    binario.reverse()
    x = len(binario)
    e = 0
    for i in range(0, x):
     h = binario[i] * (2 ** i)
     e = e + h
    return(e)


def binariooctal(b):

  binario = []
  for i in b:
   binario.append(int(i))
  binario.reverse()
  x = len(binario)
  e = 0
  for i in range(0, x):
   h = binario[i] * (2 ** i)
   e = e + h
  octal = []
  while e > 0:
   octal.insert(0, e % 8)
   e = e // 8
  octal = "".join(str(i) for i in octal)
  return (octal)


def binariohexadecimal(b):

  binario = []
  for i in b:
    binario.append(int(i))
  binario.reverse()
  x = len(binario)
  o = 0
  for i in range(0, x):
    v = binario[i] * (2 ** i)
    o = o + v
  hexadecimal = []

  while o > 0:
    hexadecimal.insert(0, o % 16)
    o = o // 16

  e = []
  for h in hexadecimal:
    if h == 10:
      h = "A"
    if h == 11:
      h = "B"
    if h == 12:
      h = "C"
    if h == 13:
      h = "D"
    if h == 14:
      h = "E"
    if h == 15:
      h = "F"
    e.append(h)
  e = "".join(str(i) for i in e)
  return (e)

#Funciones de conversion de Octal a Decimal/Binario/Hexadecimal
def octaldecimal(b):

 octal = []
 for i in b:
  octal.append(int(i))
 octal.reverse()
 x = len(octal)
 e = 0
 for i in range(0, x):
  h = octal[i] * (8 ** i)
  e = e + h
 return (e)


def octalbinario(b):

    octal = []
    for i in b:
        octal.append(int(i))
    octal.reverse()
    x = len(octal)
    e = 0
    for i in range(0, x):
        h = octal[i] * (8 ** i)
        e = e + h
    binario = []

    while e > 0:
        binario.insert(0, e % 2)
        e = e // 2
    binario = "".join(str(i) for i in binario)
    return (binario)


def octalhexadecimal(b):

    octal = []
    for i in b:
        octal.append(int(i))
    octal.reverse()
    x = len(octal)
    z = 0
    for i in range(0, x):
        q = octal[i] * (8 ** i)
        z = z + q

    hexadecimal = []
    while z > 0:
        hexadecimal.insert(0, z % 16)
        z = z // 16

    e = []
    for h in hexadecimal:
        if h == 10:
            h = "A"
        if h == 11:
            h = "B"
        if h == 12:
            h = "C"
        if h == 13:
            h = "D"
        if h == 14:
            h = "E"
        if h == 15:
            h = "F"
        e.append(h)
    e = "".join(str(i) for i in e)
    return (e)

#Funciones de conversion de Hexadecimal a Decimal/Binario/Octal
def hexadecimaldecimal(b):
 hexadecimal = []
 for i in b:
  if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
   hexadecimal.append(i)
  else:
   hexadecimal.append(int(i))

 d = []
 for h in hexadecimal:
  if h == "A":
    h = 10
  if h == "B":
    h = 11
  if h == "C":
    h = 12
  if h == "D":
    h = 13
  if h == "E":
    h = 14
  if h == "F":
    h = 15
  d.append(h)

  octal = []
  for i in d:
   octal.append(int(i))
  octal.reverse()
  x = len(octal)
  p = 0
  for i in range(0, x):
   j = octal[i]*(16 ** i)
   p = p + j
 return (p)


def hexadecimaloctal(b):
 hexadecimal = []
 for i in b:
  if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
    hexadecimal.append(i)
  else:
    hexadecimal.append(int(i))

 d = []
 for h in hexadecimal:
  if h == "A":
    h = 10
  if h == "B":
    h = 11
  if h == "C":
    h = 12
  if h == "D":
    h = 13
  if h == "E":
    h = 14
  if h == "F":
    h = 15
  d.append(h)

 octal = []
 for i in d:
  octal.append(int(i))
 octal.reverse()
 x = len(octal)
 p = 0
 for i in range(0, x):
  j = octal[i] * (16 ** i)
  p = p + j
 octal = []

 while p > 0:
  octal.insert(0, p % 8)
  p = p // 8
 octal = "".join(str(i) for i in octal)
 return (octal)


def hexadecimalbinario(b):

    hexadecimal = []
    for i in b:
        if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
            hexadecimal.append(i)
        else:
            hexadecimal.append(int(i))

    d = []
    for h in hexadecimal:
        if h == "A":
            h = 10
        if h == "B":
            h = 11
        if h == "C":
            h = 12
        if h == "D":
            h = 13
        if h == "E":
            h = 14
        if h == "F":
            h = 15
        d.append(h)

    octal = []
    for i in d:
        octal.append(int(i))
    octal.reverse()
    x = len(octal)
    p = 0
    for i in range(0, x):
        j = octal[i] * (16 ** i)
        p = p + j

    binario = []

    while p > 0:
        binario.insert(0, p % 2)
        p = p // 2
    binario = "".join(str(i) for i in binario)
    return (binario)


#Inicio Programa

while True:

 try:
  print("Bienvenido al Conversor de Numeros!")

  desc=input("En que base se encuentra su numero? decimal / binario / octal / hexadecimal : ")

  if desc==("hexadecimal") or desc==("binario") or desc==("octal"):
   n=input("Ingrese su valor a convertir : ").upper()

  else:
   n=int(input("Ingrese su valor a convertir : "))
  desc2=input("A que base quiere convertir el valor ingresado? decimal / binario / octal / hexadecimal : ")

  if desc=="decimal" and desc2=="binario":
   y=decimalabinario(n)
   print("La conversion de su valor a binario es: ", y, "\n")

  if desc == "decimal" and desc2 == "octal":
   y = decimalaoctal(n)
   print("La conversion de su valor a octal es: ", y, "\n")

  if desc == "decimal" and desc2 == "hexadecimal":
   y = decimalahexadecimal(n)
   print("La conversion de su valor a hexadecimal es: ", y, "\n")

  if desc == "binario" and desc2 == "decimal":
   y = binariodecimal(n)
   print("La conversion de su valor a decimal es: ", y, "\n")

  if desc == "binario" and desc2 == "octal":
   y = binariooctal(n)
   print("La conversion de su valor a octal es: ", y, "\n")

  if desc == "binario" and desc2 == "hexadecimal":
   y = binariohexadecimal(n)
   print("La conversion de su valor a hexadecimal es: ", y, "\n")

  if desc == "hexadecimal" and desc2 == "decimal":
   y = hexadecimaldecimal(n)
   print("La conversion de su valor a decimal es: ", y, "\n")

  if desc == "hexadecimal" and desc2 == "octal":
   y = hexadecimaloctal(n)
   print("La conversion de su valor a octal es: ", y, "\n")

  if desc == "hexadecimal" and desc2 == "binario":
   y = hexadecimalbinario(n)
   print("La conversion de su valor a binario es: ", y, "\n")

  if desc == "octal" and desc2 == "decimal":
   y = octaldecimal(n)
   print("La conversion de su valor a decimal es: ", y, "\n")

  if desc == "octal" and desc2 == "hexadecimal":
   y = octalhexadecimal(n)
   print("La conversion de su valor a octal es: ", y, "\n")

  if desc == "octal" and desc2 == "binario":
   y = octalbinario(n)
   print("La conversion de su valor a binario es: ", y, "\n")

  decs3=input("quiere seguir convirtiendo valores? si / no : ")
  if decs3=="no":
   break

 except:
  print("Se acaba de cometer algun error a la hora de ingresar valores, Recuerde que solo puede ingresar numeros y letras", "\n")
  decs3 = input("quiere intentar convertir un valor otra vez? si / no : ")
  if decs3 == "no":
      break
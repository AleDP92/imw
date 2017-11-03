



```python
import sys

dinero = int(sys.argv[1])

cincuenta_pavitos = 50
veinte_pavitos = 20
diez_pavitos = 10
entrada_andana = 5
dos_pavos = 2
pobreza_total = 1

if ((dinero//cincuenta_pavitos) >= 1):
    print(dinero//cincuenta_pavitos, "billetes de 50 €")
    dinero = dinero%cincuenta_pavitos

if ((dinero//veinte_pavitos) >= 1):
    print(dinero//veinte_pavitos, "billetes de 20 €")
    dinero = dinero%veinte_pavitos

if ((dinero//diez_pavitos) >= 1):
    print(dinero//diez_pavitos, "billetes de 10 €")
    dinero = dinero%diez_pavitos   

if ((dinero//entrada_andana) >= 1):
    print(dinero//entrada_andana, "billetes de 5 €")
    dinero = dinero%entrada_andana  

if ((dinero//dos_pavos) >= 1):
    print(dinero//dos_pavos, "billetes de 2 €")
    dinero = dinero%dos_pavos  

if ((dinero//pobreza_total) >= 1):
    print(dinero//pobreza_total, "billetes de 1 €")
    dinero = dinero%pobreza_total  
```

from clase_05_05_26.calculadora import Calculadora

if __name__ == '__main__':
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    res = Calculadora(a, b)

    print("Resultado de la suma: ", res.add())
    print("Resultado de la resta: ", res.subst())
    print("Resultado de la multiplicacion: ", res.mult())
    print("Resultado de la division: ", res.div())
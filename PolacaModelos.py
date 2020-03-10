#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Andresw
#
# Created:     06/03/2020
# Copyright:   (c) Andresw
# Licence:     <->
#-------------------------------------------------------------------------------

class Expresion:
    def interpretar(self, contexto: list):
        pass

class ExpresionNumero(Expresion):
    def __init__(self, numerito: int):
        self.__num = numerito

    def getNum(self) -> int:
        return self.__num

    def interpretar(self, contexto: list):
        contexto.append(self.__num)

class ExpresionOperacion(Expresion):
    def __init__(self, oper: str):
        self.__oper = oper

    def getOper(self) -> str:
        return self.__oper

    def confirmar(self, contexto: list):
        contexto.pop(-3)
        contexto.pop(-2)

    def interpretar(self, contexto: list):
        if self.__oper == "+":
            contexto.append(contexto[-2] + contexto[-1])
            self.confirmar(contexto)
        elif self.__oper == "-":
            contexto.append(contexto[-2] - contexto[-1])
            self.confirmar(contexto)
        elif self.__oper == "*":
            contexto.append(contexto[-2] * contexto[-1])
            self.confirmar(contexto)
        elif self.__oper == "/":
            contexto.append(contexto[-2] / contexto[-1])
            self.confirmar(contexto)
        elif self.__oper == "^":
            contexto.append(contexto[-2] ** contexto[-1])
            self.confirmar(contexto)
        else:
            print("operador", self.__oper, "no valido.")

def main():
    opers= ["+", "-", "*", "/", "^"]
    while True:
        expr = input("Dame una expresion!")
        if expr == "":
            break
        result = []
        for ter in expr.split():
            if ter.strip() in opers:
                termm = ExpresionOperacion(ter)
            else:
                termm = ExpresionNumero(int(ter))
            termm.interpretar(result)
        print(result)
    pass

if __name__ == '__main__':
    main()

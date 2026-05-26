import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        # RAIZ QUADRADA
        if operacao == "sqrt":

            if num1 < 0:
                return render_template(
                    "calculadora.html",
                    etapas=f"Não existe raiz real de {num1}.",
                    resultados="Erro: número negativo"
                )

            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

        else:
            num2_valor = request.form.get("num2", "").strip()

            if not num2_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número.",
                    resultados=""
                )

            num2 = float(num2_valor)

            # SOMA
            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            # SUBTRAÇÃO
            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"

            # MULTIPLICAÇÃO
            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} × {num2} = {resultado}"

            # DIVISÃO
            elif operacao == "/":

                if num2 == 0:
                    return render_template(
                        "calculadora.html",
                        etapas="Não é possível dividir por zero.",
                        resultados="Erro"
                    )

                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

            # POTÊNCIA
            elif operacao == "**":
                resultado = math.pow(num1, num2)
                etapas = f"{num1}^{num2} = {resultado}"

            # LOGARITMO
            elif operacao == "log":

                if num1 <= 0:
                    return render_template(
                        "calculadora.html",
                        etapas="O logaritmo só existe para números positivos.",
                        resultados="Erro"
                    )

                resultado = math.log(num1, num2)
                etapas = f"log de {num1} na base {num2} = {resultado}"

            else:
                return render_template(
                    "calculadora.html",
                    etapas="Operação inválida.",
                    resultados="Erro"
                )

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado
        )

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Digite valores válidos.",
            resultados="Erro"
        )
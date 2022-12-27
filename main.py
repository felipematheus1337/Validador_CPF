# CPF = VALUE WITH DOTS FOR EXAMPLE 746.824.890-70
# CPF = VALUE WITHOUT DOTS FOR EXAMPLE 74682489070
import re
import sys


def main():
    entrada = input("CPF: ")

    def validate_cpf_input(cpf):
        entrada_e_sequencial = cpf == cpf[0] * len(cpf)

        if entrada_e_sequencial:
            print("Você enviou dados sequenciais")
            sys.exit()
        else:
            cpf_enviado_usuario = re.sub(
                r'[^0-9]',
                '',
                entrada, )
            return cpf_enviado_usuario

    cpf_enviado = validate_cpf_input(entrada)
    nove_digitos = cpf_enviado[:9]

    def generate_first_digit(n_digitos):
        contador_regressivo_1 = 10
        resultado_digito_1 = 0

        for digito in n_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        return digito_1

    first_digit = generate_first_digit(nove_digitos)

    def generate_second_digit(digito, n_digitos):
        dez_digitos = n_digitos + str(digito)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0

        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        return digito_2

    second_digit = generate_second_digit(first_digit, nove_digitos)


    cpf_gerado_calculo = f'{nove_digitos}{first_digit}{second_digit}'

    if cpf_enviado == cpf_gerado_calculo:
        print(f'{cpf_enviado} é valido')
    else:
        print("CPF invalido")

if __name__ == '__main__':
    main()

import re

def matricula(*matriculas):
    patron = r"^[0-9]{4}(()|( )?|(-)?)[B-DF-HJ-NP-PR-TV-Za-df-hj-np-pr-tv-z]{3}$"
    matriculaValidas = 0
    matriculasInvalidas = 0
    for i in matriculas:
        if re.fullmatch(patron, i):
            print(i,"es valida")
            matriculaValidas += 1
        else:
            print(i," no es valida")
            matriculasInvalidas += 1

    print("Matriculas validas: ", matriculaValidas)
    print("Matriculas invalidas: ", matriculasInvalidas)

matricula("22CDR", "7521-MXP","1224MN")
matricula("54732 - BCF", "3456BAC")
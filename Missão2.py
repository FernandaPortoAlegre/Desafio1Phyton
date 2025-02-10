# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).


def elegibilidade():
    idade = int(input("Digite a idade do usuário:"))

    if idade < 16:
        print("o usuário não pode votar")
    else:
        print("O usuário pode votar!")
    
elegibilidade()
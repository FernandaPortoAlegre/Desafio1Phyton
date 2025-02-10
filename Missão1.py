# Você é um(a) estudante 🎓 apaixonado(a) por tecnologia que acaba de ser aceito(a) no Vai na Web, uma super escola de tecnologia onde os alunos resolvem desafios de programação para avançar nos estudos.

# Mas há um problema! ⚠️ Um vírus misterioso invadiu o sistema, bagunçando notas, permissões de acesso 🔐 e até a segurança da escola. O diretor, Professor Byte, precisa da sua ajuda para restaurar tudo antes que a situação piore!
# Resolva os desafios abaixo para recuperar o controle do sistema. Boa sorte, Dev!🚀

# (Deve ser feito em Python!)

# Instruções do Desafio: 🚨

# Missão 1: Restaurando as Regras Escolares 📝 
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).


def verificar_aprovacao(nota):

    if nota >= 6:
        print(f"O aluno foi aprovado!")
    else:
       print(f"O aluno foi reprovado.")

nota_aluno = float(input("Digite a nota do aluno: "))
result = verificar_aprovacao(nota_aluno)







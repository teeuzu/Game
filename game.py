# Importando a classe Calcular do arquivo calcular.py 
from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

# Informando o nível de dificuldade do jogo
def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado: [1, 2, 3 ou 4]: '))

    # Recebendo a variável com o nível de dificuldade informado
    calc: Calcular = Calcular(dificuldade)
    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao() 

    resultado: int = int(input())

    #Checando se o resultado esperado está correto ou não
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos(s).\n')
    
    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')



# Executando o projeto 
if __name__ == '__main__':
    main()
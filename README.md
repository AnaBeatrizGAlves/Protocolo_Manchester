
# Sistema de Triagem - Protocolo de Manchester

Este projeto simula o processo de triagem hospitalar utilizando o **Protocolo de Manchester**, 
que classifica os pacientes por nível de urgência (Vermelho, Laranja, Amarelo, Verde e Azul).  
O sistema foi feito com **Python e Tkinter**, e usa uma **estrutura de dados em fila** 
para organizar o atendimento de forma justa.

# Sobre o projeto

Quando um paciente chega, o programa faz perguntas (como se fosse uma mini triagem automatizada) 
e decide em qual **cor de urgência** ele se encaixa.

Depois disso:
- Ele entra na **fila da cor correspondente**.
- Os pacientes são chamados **na ordem de prioridade** (Vermelho → Laranja → Amarelo → Verde → Azul).
- O sistema mostra quantos pacientes existem em cada fila e quem será o próximo.

Tudo isso com uma interface, feita em **Tkinter**, para facilitar o uso.

# Estrutura do projeto

O código foi dividido em duas partes principais dentro do mesmo arquivo:

1. **Parte lógica** — responsável pela árvore de decisão e filas. 
    O sistema utiliza duas estruturas principais:
    - Árvore de Decisão: Cada nó representa uma pergunta ou uma cor de triagem (Vermelho, Laranja, Amarelo, Verde ou Azul).Dependendo das respostas do paciente ("sim" ou "não"), o sistema percorre a árvore até chegar em um nó folha, que define a cor de prioridade.
    - Filas (FIFO): Cada cor possui sua fila independente, organizada pelo princípio FIFO (First In, First Out). O primeiro paciente a entrar na fila é o primeiro a ser atendido.

2. **Parte gráfica** — interface com o usuário feita com Tkinter.

# Como rodar o projeto

1. Ter o **Python 3** instalado na sua máquina.  
   Você pode verificar com:
   ```bash
   python --version

2.Salve este arquivo como triagem.py.
3.Execute no terminal:  python triagem.py
4.A janela do sistema vai abrir e você já pode cadastrar pacientes.

# Tecnologias usadas
- Python 3
- Tkinter (interface gráfica)
- Collections.deque (para as filas de pacientes)

Aluno: Ana Beatriz Gonçalves Alves
Disciplina: Estrutura de Dados

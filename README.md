# Urban Bike: A Python OOP system

![Tela real capturada em 16/11/2024.](https://drive.google.com/uc?export=view&id=1d94KSVcpha2qa6h4sHLTIy8iTxKFYWoO)

> Sistema de gerência de usuários e bicicletas compartilhadas, desenvolvido em arquitetura Orientada a Objetos para a disciplina de Lógica de Programação e Desenvolvimento de User Interface da Pós-graduação em UX Design da Universidade La Salle em Canoas - RS.

## ⚙️ Detalhamento do Projeto
O projeto Urban Bike consiste em um sistema de gerenciamento de contas para ciclistas, implementado em Python. Ele possibilita a criação e o gerenciamento de dois tipos de contas, `PedalPop` e `PedalPremium`, que possuem diferentes funcionalidades relacionadas ao uso de créditos em pedais. Além disso, o sistema oferece um menu interativo para que os usuários possam gerenciar suas contas de uma maneira mais prática.

#### **Estrutura do Projeto**
O projeto foi desenvolvido através da POO, separando as responsabilidades do sistema em diferentes diretórios e arquivos:
- **`classes`**: Contém as classes `PedalPop` e `PedalPremium`.
- **`interfaces`**: Define a interface `Imprimivel`, responsável por garantir que as classes possam exibir suas informações.
- **`models`**: Contém a classe abstrata `ContaUrbanBike` e a classe `Ciclistas`, responsável pelo gerenciamento das contas.
- **Inicializador `Main.py`**: Implementa o menu interativo para o gerenciamento das funcionalidades do sistema.

#### **Classes e Funcionalidades Desenvolvidas**
1. **Classe Abstrata `ContaUrbanBike`**
   - Contém os atributos `numeroConta` e `saldo`.
   - Define os métodos abstratos `pedalar` e `creditar`.
   - Implementa o método `transferir`, permitindo transferências de créditos entre contas, respeitando as regras de saldo e taxas.

2. **Classes `PedalPop` e `PedalPremium`**
   - Ambas herdam de `ContaUrbanBike` e implementam os seus métodos abstratos.
   - **`PedalPop`**: Possui o atributo adicional `taxaOperacao`, aplicado em todas as operações de pedalar e transferir.
   - **`PedalPremium`**: Possui o atributo adicional `limite`, permitindo que o saldo fique negativo até o limite especificado.
   - Ambas implementam a interface `Imprimivel`, exibindo informações detalhadas sobre as contas.

3. **Interface `Imprimivel`**
   - Garante que todas as classes que a implementam forneçam o método `mostrarDados`, utilizado para exibir os detalhes das contas.

4. **Classe `Ciclistas`**
   - Gerencia uma lista de pedais (`PedalPop` e `PedalPremium`), oferecendo métodos para:
     - **Inserir**: Adiciona novos pedais à lista, evitando duplicidade.
     - **Remover**: Remove um pedal existente da lista.
     - **Procurar**: Localiza pedais com base no número da conta.
     - **Listar**: Exibe todos os pedais cadastrados utilizando o método `mostrarDados`.

5. **Inicializador (`Main.py`)**
   - Implementa um menu interativo com as opções:
     - **Criar Pedal**: Permite ao usuário criar uma conta `PedalPop` ou `PedalPremium`.
     - **Remover Pedal**: Remove uma conta específica, se existir.
     - **Gerar Relatório**: Exibe todos os pedais cadastrados.
     - **Selecionar Pedal**: Permite acessar ações específicas de uma conta (creditar, pedalar, transferir e gerar relatório).
     - **Finalizar**: Encerra o programa.

#### **Destaques do Desenvolvimento**
- **Modularidade**: A estrutura do projeto promoveu a reutilização de código por meio da herança (`ContaUrbanBike`) e da interface (`Imprimivel`).
- **Validações**: Todas as operações, como criação de contas, transferências e remoções, possuem validações para evitar erros e inconsistências.
- **Menu Interativo**: Facilita a interação do usuário com o sistema, permitindo o gerenciamento completo de contas e pedais.
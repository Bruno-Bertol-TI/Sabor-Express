
# 🍽️ Sistema de Cadastro e Avaliação de Restaurantes

Este é um sistema de gerenciamento de restaurantes feito em Python. Ele permite cadastrar, ativar/desativar e avaliar restaurantes. O projeto é modularizado e estruturado para fins educacionais, com foco em boas práticas de organização de código, uso de classes, métodos, menus interativos e operações em terminal.

---

## 🚀 Funcionalidades

- 📋 Cadastrar restaurantes manualmente ou em massa
- 🗂️ Listar restaurantes com status (Ativo/Inativo)
- 🔄 Ativar ou desativar restaurantes em masa ou manualmente
- 📝 Avaliar restaurantes manualmente ou com geração em massa
- ⭐ Visualizar todas as avaliações cadastradas
- 💡 Interface de terminal limpa e interativa (compatível com Windows/Linux/macOS)
- 📦 Código separado por módulos para melhor organização

---

## 💻 Como Executar

1. Tenha o **Python 3.x** instalado na sua máquina.
2. Clone este repositório ou copie os arquivos do projeto para uma pasta local.
3. No terminal, navegue até essa pasta e execute:

```bash
python main.py
```

---

## 📂 Estrutura de Arquivos

```
|- modelos/
|  |- avaliacao.py        # Classe que representa uma avaliação (cliente + nota)
|  |- restaurante.py      # Classe Restaurante com métodos para cadastro, status e avaliações
|  |- utils.py            # Funções utilitárias para terminal
|- main.py                # Arquivo principal: menu e fluxo principal do sistema
|- README.md              # Documentação do projeto
```

---

## 🧱 Classes

### 📍 `Restaurante` (`modelos/restaurante.py`)
| Método / Propriedade       | Descrição                                                                  |
|----------------------------|----------------------------------------------------------------------------|
| `__init__(nome, categoria)`| Cria um novo restaurante com nome, categoria e status inativo              |
| `ativo`                    | Retorna string "Ativo" ou "Inativo" com base no status booleano            |
| `is_ativo` / `set_ativo()` | Propriedades para manipular o status do restaurante                        |
| `avaliacao`                | Lista de avaliações recebidas                                              |
| `receber_avaliacao()`      | Adiciona uma nova avaliação à lista                                        |
| `exibir_restaurantes()`    | Lista todos os restaurantes com ID, nome, categoria, status e classificação|
| `exibir_avaliacoes()`      | Exibe avaliações de todos os restaurantes                                  |
| `media`                    | Calcula a clasificação media e retorna a nota média do restaurante         |

---

### ⭐ `Avaliacao` (`modelos/avaliacao.py`)
| Método / Propriedade  | Descrição                                        |
|-----------------------|--------------------------------------------------|
| `__init__(cliente, nota)` | Inicializa a avaliação com cliente e nota   |
| `__str__()`           | Retorna a avaliação formatada                   |
| `cliente`             | Nome do cliente                                 |
| `nota`                | Nota atribuída ao restaurante (0 a 10)          |

---

## 🔧 Utilitários (`modelos/utils.py`)

| Função               | Descrição                                                             |
|----------------------|----------------------------------------------------------------------|
| `limpar_tela()`      | Limpa a tela do terminal conforme o sistema operacional              |
| `exibir_titulo()`    | Exibe o cabeçalho estilizado do sistema                              |
| `exibir_menu()`      | Mostra as opções do menu principal                                   |
| `pausar()`           | Aguarda o usuário pressionar ENTER antes de continuar                |
| `em_massa()`         | Menu para cadastro em massa ou unitario                              |
| `quantidade_funcao_em_massa()`| retornar quantos salvamentos em massa o usuario deseja      |

---

## 🎮 Menu Interativo (`main.py`)

| Opção                     | Ação Realizada                                            |
|--------------------------|-----------------------------------------------------------|
| 1. Cadastrar restaurante | Cadastra restaurantes manualmente e em massa               |
| 2. Listar restaurantes   | Exibe todos os restaurantes registrados                   |
| 3. Listar avaliações     | Exibe todas as avaliações feitas nos restaurantes         |
| 4. Ativar / Desativar    | Altera o status (ativo/inativo) de um restaurante em massa ou unitariamente|
| 5. Avaliar restaurantes  | Avalia restaurantes manualmente (avaliacao em massa somente para testes) |
| 6. Sair                  | Finaliza o sistema                                         |

---

## 🤓 Observações

- O sistema foi desenvolvido com fins educacionais e simula funcionalidades básicas de um sistema de cadastro e avaliação.
- Avaliações podem ser feitas manualmente ou com dados fictícios gerados automaticamente (nome e nota aleatória).

---

## 📌 Requisitos

- Python 3.7+
- Sistema operacional com terminal (Windows, Linux ou macOS)

## ⭐ Autor

📎 Me encontre no [LinkedIn](https://www.linkedin.com/in/seu-usuario)  
🐙 Veja meus projetos no [GitHub](https://github.com/seu-usuario)

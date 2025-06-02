# 🍽️ Sistema de Cadastro e Gerenciamento de Restaurantes

Este é um aplicativo em Python para cadastro, listagem e ativação/desativação de restaurantes. O projeto é modularizado em múltiplos arquivos, ideal para fins educacionais e para aprender princípios de organização de código em Python com importações, classes, funções e menu interativo no terminal.

---

## 🧠 Funcionalidades

- ✅ Exibe o nome do programa com um banner ASCII estilizado  
- ✅ Limpa a tela automaticamente (compatível com Windows, Linux e macOS)  
- ✅ Menu interativo com as opções:
  - Cadastrar novo restaurante
  - Listar restaurantes cadastrados
  - Ativar/Desativar restaurante
  - Sair
- ✅ Código organizado em múltiplos arquivos com importações
- ✅ Classe `Restaurante` com atributos e métodos para controle de dados

---

## 💻 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou copie os arquivos para uma pasta local.
3. No terminal, navegue até a pasta onde estão os arquivos.
4. Execute com:

```bash
python main.py
```

---

## 📂 Estrutura de Arquivos

| Arquivo           | Função Principal                                                  |
|-------------------|-------------------------------------------------------------------|
| `main.py`         | Ponto de entrada. Gerencia o menu e o fluxo principal             |
| `restaurante.py`  | Define a classe `Restaurante` e seus métodos                      |
| `utils.py`        | Funções utilitárias para limpar tela, exibir títulos e menus      |

---

## 📦 Classe `Restaurante`

| Método                        | Descrição                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `__init__()`                 | Inicializa restaurante com nome, categoria e status                       |
| `listar_restaurantes()`     | Mostra todos os restaurantes registrados                                  |
| `alternar_status()`         | Ativa ou desativa um restaurante                                          |
| `exibir_restaurante()`      | Retorna representação formatada do restaurante                            |

---

## 🔧 Utilitários (`utils.py`)

| Função                        | Descrição                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `limpar_tela()`              | Limpa a tela do terminal                                                  |
| `exibir_nome_do_programa()` | Exibe o nome do sistema com arte ASCII                                    |
| `exibir_opcoes()`           | Mostra o menu principal com as opções disponíveis                         |
| `exibir_subtitulo()`        | Mostra um subtítulo formatado                                             |
| `voltar_ao_menu_principal()`| Aguarda entrada do usuário para voltar ao menu                            |
| `opcao_invalida()`          | Informa erro e volta ao menu principal                                    |

---

## ⚙️ Compatibilidade

✅ Windows  
✅ Linux  
✅ macOS

Uso de `os.system('cls' if os.name == 'nt' else 'clear')` para limpar a tela de forma compatível.

---

## 📌 Melhorias Futuras

- [ ] Armazenamento persistente (arquivo/banco de dados)
- [ ] Interface gráfica com Tkinter ou web com Flask/Django
- [ ] Testes automatizados com `pytest`

---

## 🧑‍💻 Autor

Desenvolvido por **Bruno Bertol**  
🔗 [LinkedIn](https://www.linkedin.com/in/bruno-bertol-894267209)
# 🍽️ Sistema de Cadastro e Gerenciamento de Restaurantes

Este é um aplicativo simples em Python para cadastro e listagem de restaurantes. Ele funciona no terminal e é ideal para fins educacionais, aprendendo conceitos básicos de Python como listas, funções, entrada do usuário e estruturas condicionais.

---

## 🧠 Funcionalidades

- ✅ Exibe o nome do programa com um banner ASCII estilizado  
- ✅ Limpa a tela automaticamente (compatível com Windows, Linux e macOS)  
- ✅ Menu interativo com as opções:
  - Cadastrar novo restaurante
  - Listar restaurantes cadastrados
  - Ativar restaurante
  - (Planejado) Desativar restaurante
  - Sair

---

## 💻 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou copie o código para um arquivo chamado, por exemplo, `app.py`.
3. No terminal, navegue até a pasta onde está o arquivo.
4. Execute com:

```bash
python app.py
```

---

## 📂 Estrutura do Código

| Função                         | Descrição                                                                |
|-------------------------------|---------------------------------------------------------------------------|
| `main()`                      | Ponto de entrada do app                                                   |
| `exibir_nome_do_programa()`   | Exibe o banner ASCII com o nome do programa                               |
| `exibir_opcoes()`             | Mostra o menu principal com as opções disponíveis                         |
| `limpar_tela()`               | Limpa a tela do terminal (Windows: `cls`, Linux/macOS: `clear`)           |
| `voltar_ao_menu_principal()`  | Aguarda entrada e retorna ao menu principal                               |
| `opcao_invalida()`            | Exibe mensagem de erro e retorna ao menu principal                        |
| `exibir_subtitulo()`          | Mostra um subtítulo formatado para cada operação                          |
| `cadastrar_novo_restaurante()`| Solicita nome, categoria e condicao do restaurante e o adiciona à uma lista de dicionarios|
| `listar_restaurante()`        | Exibe nome, categoria e condicao detodos os restaurantes cadastrados      |
| `ativar_restaurante()`        | Exibe nome, categoria e condicao detodos os restaurantes cadastrados e solicita indice para ativar restaurant|
| `finalizar_app()`             | Exibe mensagem de finalização do app                                      |
| `escolher_opcoes()`           | Lê a escolha do usuário e chama a função correspondente                   |

---

## ⚙️ Compatibilidade

✅ Windows  
✅ Linux  
✅ macOS

O código usa a função `os.system()` com verificação de sistema operacional para limpar a tela corretamente:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

---

## 📌 Melhorias Futuras

- [ ] Implementar funcionalidade de desativar restaurantes  -  EM DESENVOLVIMENTO
- [ ] Armazenamento persistente em arquivo ou banco de dados
- [ ] Interface gráfica com Tkinter ou web com Flask/Django

---

## 🧑‍💻 Autor

Desenvolvido por **Bruno Bertol**  
🔗 Contato: [LinkedIn](https://www.linkedin.com/in/bruno-bertol-894267209)

---
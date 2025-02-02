# Processador de Arquivos OTDR

## 📌 Descrição
Este programa processa arquivos `.sor` de medição OTDR e extrai informações importantes para preencher automaticamente uma planilha Excel. Ele conta com uma interface gráfica para facilitar a seleção dos arquivos e a configuração do processamento.

---

## 🛠 Requisitos
Antes de instalar e executar o programa, certifique-se de que possui os seguintes requisitos instalados:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Dependências listadas em `requirements.txt`

---

## 📥 Instalação
### 1️⃣ Clone o repositório:
```bash
 git clone https://github.com/seuusuario/processador-otdr.git
 cd processador-otdr
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso do Programa
### 1️⃣ Execute o programa:
```bash
python main.py
```

### 2️⃣ Utilize a interface gráfica:
- **Selecione a pasta** onde estão os arquivos `.sor`.
- **Escolha a planilha** onde os dados serão inseridos.
- **Defina o sentido do troço** (A-B ou B-A).
- Clique em **"Processar"** para iniciar o preenchimento da planilha.
- Após a finalização, clique em **"Concluído"** para encerrar o programa.

---

## 📂 Estrutura de Diretórios
```
OTDR_PY/
│
├── main.py                  # Arquivo principal do programa
├── interface/
│   └── interface.py         # Interface gráfica com CustomTkinter
├── processamento/
│   ├── conversor.py         # Conversão e extração de dados dos arquivos .sor
│   ├── Cancelar_Concluir.py # Funções para cancelar e concluir o processo
├── data/
│   ├── arquivos_sor/        # Pasta com arquivos .sor a serem processados
│   ├── planilhas/           # Pasta onde a planilha processada será salva
├── requirements.txt         # Lista de dependências
└── README.md                # Este arquivo
```

---

## ⚙ Funcionalidades
✅ Conversão automática de arquivos `.sor` para JSON
✅ Extração de informações OTDR para a planilha
✅ Interface intuitiva com seleção de pasta e planilha
✅ Suporte a diferentes sentidos de medição (A-B e B-A)

---

## 🛑 Como Cancelar o Processo
Se desejar interromper o processamento antes da conclusão:
- Clique no botão **"Cancelar"**.
- Todos os arquivos temporários serão excluídos automaticamente.

---

## ❓ Dúvidas?
Caso tenha alguma dúvida ou encontre problemas, entre em contato com o desenvolvedor ou abra uma issue no repositório GitHub.

---

📌 **Desenvolvido para automação de processamento de arquivos OTDR.**


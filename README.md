# HydroSizer

A aplicação **HydroSizer** é um software com interface gráfica em **Tkinter** para o **dimensionamento de sistemas de água fria**. Ela permite calcular a perda de carga e o diâmetro necessário para tubulações com base na quantidade de pontos de consumo (vasos sanitários, chuveiros, pias, etc.). Além disso, oferece a opção de **exportar os resultados para um arquivo PDF**, utilizando a biblioteca **ReportLab**. O design inclui suporte para **temas claro e escuro**, tornando a experiência mais intuitiva para o usuário.

## Recursos
- Interface gráfica intuitiva desenvolvida com **Tkinter**.
- Cálculo automático da **perda de carga** e **diâmetro** de tubulações.
- **Exportação dos resultados** para um arquivo **PDF**.
- Suporte para **temas claro e escuro**.

## Tecnologias Utilizadas
- **Python 3**
- **Tkinter** (Interface Gráfica)
- **ReportLab** (Geração de PDF)
- **python-docx** (Manipulação de arquivos DOCX, se necessário)

## Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/HydroSizer.git
   cd HydroSizer
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv .venv
   # Ativar no Windows
   .venv\Scripts\activate
   # Ativar no Linux/macOS
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Como Usar
1. Execute o arquivo principal:
   ```sh
   python app.py
   ```
2. Insira a quantidade de pontos de consumo (vasos sanitários, chuveiros, pias, etc.).
3. Clique em "Calcular" para obter os resultados.
4. Opçionalmente, exporte os resultados para **PDF**.

## Contribuição
Se desejar contribuir, siga os passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade:
   ```sh
   git checkout -b minha-nova-funcionalidade
   ```
3. Faça suas alterações e envie um pull request.

---
Desenvolvido por **Marcus Torres** 🚀


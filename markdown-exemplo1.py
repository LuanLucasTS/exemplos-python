from flask import Flask, render_template_string
import markdown2

app = Flask(__name__)

@app.route('/')
def index():
    # Seu texto em Markdown
    markdown_text = """
    # Título Principal

    ## Subtítulo

    **Negrito** ou __Negrito__

    *Itálico* ou _Itálico_

    - Lista não ordenada
      - Item 1
      - Item 2
        - Subitem 2.1
        - Subitem 2.2

    1. Lista ordenada
    2. Item 2
    3. Item 3

    [Link para o OpenAI](https://openai.com)

    ![Imagem de exemplo](https://exemplo.com/imagem.png)

    `Código em linha`

    ```
    Bloco de código
    em múltiplas
    linhas
    ```

    > Bloco de citação

    Tabela:

    | Coluna 1 | Coluna 2 |
    |----------|----------|
    | Dado 1   | Dado 2   |
    | Dado 3   | Dado 4   |
    """

    # Convertendo o Markdown para HTML
    html_text = markdown2.markdown(markdown_text)

    # Renderizando o template com o HTML convertido
    return render_template_string(html_text)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import markdown2

app = Flask(__name__)

@app.route('/')
def index():
    # Carregar o conteúdo do arquivo Markdown
    with open('conteudo.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Converter o Markdown para HTML
    html_content = markdown2.markdown(markdown_content)

    # Renderizar o template com o HTML convertido
    return render_template('index.html', content=html_content)

if __name__ == '__main__':
    app.run(debug=True)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Viewer</title>
</head>
<body>
    <!-- O conteúdo Markdown convertido em HTML será inserido aqui -->
    {{ content | safe }}
</body>
</html>
'''
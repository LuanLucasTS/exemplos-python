
from flask import Flask, render_template, request, redirect, url_for
from modulo import UsuarioDao, VeiculoioDao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbd7ea2f0f4ea484525828a5b0116aa6acd2adef8d9eec8125c51b1a112a85b7'

usuariodao = UsuarioDao()
veiculodao = VeiculoioDao()

@app.route('/')
def home():
    usuario = usuariodao.listar()
    return render_template('tabela.html', usuario=usuario)

@app.route('/ordemU/<ordemU>')
def ordenadoU(ordemU):
    usuario = usuariodao.ordena_por(ordemU)
    return render_template('tabela.html', usuario=usuario)

@app.route('/pesquisaU', methods=["GET", "POST"])
def pesquisaU():
    if request.method == "POST":
        pesquisa = request.form['pesquisa']
        usuario = usuariodao.pesquisa(pesquisa)
        return render_template('tabela.html', usuario=usuario)
    else:
        return redirect(url_for("home"))

@app.route('/veiculo')
def veiculo():
    veiculo = veiculodao.listar()
    return render_template('veiculos.html', veiculo=veiculo)

@app.route('/ordemV/<ordemV>')
def ordenadoV(ordemV):
    veiculo = veiculodao.ordena_por(ordemV)
    return render_template('veiculos.html', veiculo=veiculo)

@app.route('/pesquisaV', methods=["GET", "POST"])
def pesquisaV():
    if request.method == "POST":
        pesquisa = request.form['pesquisa']
        veiculo = veiculodao.pesquisa(pesquisa)
        return render_template('veiculos.html', veiculo=veiculo)
    else:
        return redirect(url_for("veiculo"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('faz_marido.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profissionais')
def profissionais():
    conn = get_db()
    profs = conn.execute('SELECT * FROM profissionais WHERE aprovado = 1 ORDER BY plano DESC').fetchall()
    conn.close()
    return render_template('profissionais.html', profissionais=profs)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/salvar_cadastro', methods=['POST'])
def salvar_cadastro():
    dados = request.form
    conn = get_db()
    conn.execute('''
        INSERT INTO profissionais (nome, whatsapp, servicos, cidade, raio, descricao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (dados['nome'], dados['whatsapp'], ','.join(request.form.getlist('servicos')), 
          dados['cidade'], dados['raio'], dados.get('descricao', '')))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
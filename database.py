import sqlite3

def criar_banco():
    conn = sqlite3.connect('faz_marido.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profissionais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            whatsapp TEXT NOT NULL,
            servicos TEXT NOT NULL,
            cidade TEXT NOT NULL,
            raio INTEGER NOT NULL,
            descricao TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco criado!")

if __name__ == "__main__":
    criar_banco()
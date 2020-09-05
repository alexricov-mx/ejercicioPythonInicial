from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/')
def hello_wolrd():
    return 'hola amigos, esto es python'

@app.route('/primer_html')
@app.route('/primer_html/<fecha>')
def primer_html(fecha='define una fecha'):
   return '''
        <html>
            <body>
                <h1>Panbol app</h1>
                <h2></h2>
                <p>Seleccion de Torneo</p>
                <ul>
                    <li>LIGAMX</li>
                    <li>La Liga España</li>
                    <li>Serie A Italia</li>
                    <li>Premier League Inglaterra</li>
                </ul>
            </body>
        </html>
   '''%fecha

@app.route('/pagina_render/')
@app.route('/pagina_render/<torneo>')
def pagina_render(torneo='LIGAMX'):
   return render_template('views/pagina_index.html',nomTorneo=torneo)

if __name__ == '__main__':
    app.run()
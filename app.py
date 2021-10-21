from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("formulario.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operacion = request.form.get("operacion")

        if operacion == 'sumar':
            res= float(num1) + float(num2)
            return render_template("formulario.html", res=res)

        elif operacion == 'restar':
            res= float(num1) - float(num2)
            return render_template("formulario.html", res=res)

        elif operacion == 'multiplicar':
            res= float(num1) * float(num2)
            return render_template("formulario.html", res=res)

        elif operacion == 'dividir':
            try:
                res= float(num1) / float(num2)
                return render_template("formulario.html", res=res)
            except Exception as Ex:
                res1=("divisiones por cero no se realizan")
                return render_template("formulario.html",res1=res1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
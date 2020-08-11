from flask import Flask, render_template, request

app = Flask(__name__)


def createtable(text):
    row = text.count('\r\n')
    col = text.count(',') // row

    textable = "\\begin{table}[htb]\n"
    textable += "  \\begin{center}\n"
    textable += "    \\caption{}\n"
    textable += "      \\begin{tabular}{|"
    for i in range(col+1):
        textable += "c"
        if i == col:
            textable += "|} \\hline \n      "
        else:
            textable += " | "
    text = text.replace(',', ' & ')
    text = text.replace('\r\n', ' \\\\ \\hline \n      ')
    textable += text

    textable += "\\end{tabular} \n"
    textable += "    \\label{} \n"
    textable += "  \\end{center} \n"
    textable += "\\end{table}"

    return textable


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def read_csv():
    f = request.files['send_data']
    fstring = f.read()
    file_data = fstring.decode('UTF-8')
    text = createtable(file_data)
    return render_template('index.html', text=text)

    return 'OK'


if __name__ == '__main__':
    app.run()

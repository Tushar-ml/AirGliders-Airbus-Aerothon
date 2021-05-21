from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def search():

    if request.method == 'POST':
        query = request.form.get('query')
        print(query)

    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
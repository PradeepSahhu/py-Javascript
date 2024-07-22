from os import sendfile
from flask import Flask, jsonify, render_template,request
from flask import send_file
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import io
import base64




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiplication_table/<int:number>')
def multiplication_table(number):
    table = {i: i * number for i in range(1, 11)}
    return jsonify(table)


@app.route('/plot.png')
def plot_png():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title('Sample Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png', as_attachment=False)

@app.route('/coordinates', methods=['POST'])
def coordinates():
    try:
        data = request.json
        if not data or 'x' not in data or 'y' not in data:
            return jsonify({"error": "No data provided"}), 400
        
        x_data = data['x']
        y_data = data['y']
        
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)

        ax.set_title('Custom Plot')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        return send_file(img, mimetype='image/png', as_attachment=False)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/pradeep")
def greetings():
    message = {"name":"Pradeep Sahu","uid":"22BCS10284"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)

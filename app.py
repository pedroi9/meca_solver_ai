from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
import es_core_news_sm
nlp = es_core_news_sm.load()


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    description = data.get('description', '')
    doc = nlp(description)
    return jsonify({"result": "Análisis completado", "description": description})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

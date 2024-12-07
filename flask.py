from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/scrape', methods=['GET'])
def scrape_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Please provide a URL"}), 400

    data = scrape_website(url)
    if data is None:
        return jsonify({"error": "Failed to scrape the website"}), 500

    processed_data = process_data(data)
    return jsonify(processed_data.to_dict(orient='records'))

if _name_ == '_main_':
    app.run(debug=True)
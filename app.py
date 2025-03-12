from flask import Flask, request, jsonify
from version_finder import compare_packages

app = Flask(__name__)

@app.route('/packages', methods=['POST'])
def check_packages():
    data = request.get_json()
    
    if not data or 'package1' not in data or 'package2' not in data:
        return jsonify({'error': 'Invalid payload. Expecting package1 and package2 with versions'}), 400
    
    package1 = data['package1']
    package2 = data['package2']
    print(data)
    
    result = compare_packages(package1.get('name', 'Unknown'),package2.get('name', 'Unknown'),package1.get('version', 'Unknown'), package2.get('version', 'Unknown'))
    
    # response = {
    #     'package1': {
    #         'name': package1.get('name', 'Unknown'),
    #         'version': package1.get('version', 'Unknown')
    #     },
    #     'package2': {
    #         'name': package2.get('name', 'Unknown'),
    #         'version': package2.get('version', 'Unknown')
    #     }
    # }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == '__main__':
#     result = compare_packages("bnlearn", "numpy", "==0.0.0","^2.2.3")
#     print(result)

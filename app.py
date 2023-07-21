from main import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['msg']
    print(f"Received message: {message}")
    with open('ERC-neurotransmitters/new_file_path.txt', 'r') as file:
        new_file_path = file.read()
        if new_file_path == '':
            new_file_path = None
    [new_file_path, response_ERC1, response_ERC2, response_ERC3, plan, dopamine_level, endorphin_level, oxytocin_level, adrenaline_level, ntv, num, status] = RUN(run_conversation(new_file_path, nt4, message))
    with open('ERC-neurotransmitters/new_file_path.txt', 'w') as file:
        if new_file_path ==None:
            file.write('')
        else:
            file.write(new_file_path)
    # You can replace the line below with the logic of your chat application
    response = {'response_ERC1' : response_ERC1, 'response_ERC2' : response_ERC2, 'response_ERC3' : response_ERC3, 'plan' : str(plan), 'dopamine_level_user' : dopamine_level, 'endorphin_level_user' : endorphin_level, 'oxytocin_level_user' : oxytocin_level, 'adrenaline_level_user' : adrenaline_level, 'ntv1' : ntv[0], 'ntv2' : ntv[1], 'ntv3' : ntv[2], 'ntv4' : ntv[3], 'num' : num, 'status' : status}

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)

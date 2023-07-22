from new_main import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

nt4=Neurotransmitter(10,20,30,20)

@app.route('/refresh', methods=['POST'])
def refresh():
    restore_memory()
    return '', 200
@app.route('/ntv', methods=['POST'])
def getntv():
    response = {'nt1' : nt4.array[0] , 'nt2' : nt4.array[1] , 'nt3' : nt4.array[2] , 'nt4' : nt4.array[3]}
    return(jsonify(response))
@app.route('/writememory', methods=['POST'])
def writememory():
    data = request.get_json()
    message = data['msg']
    write_to_memory(message)
    return '', 200

@app.route('/get_user_ntv', methods=['POST'])
def get_ntv():
    data = request.get_json()
    message = data['msg']
    [dopamine_level_user, endorphin_level_user, oxytocin_level_user, adrenaline_level_user, chat_synopsis3] = RUN(get_user_ntv(message))
    response = {'dopamine_level_user': dopamine_level_user, 'endorphin_level_user': endorphin_level_user, 'oxytocin_level_user': oxytocin_level_user, 'adrenaline_level_user': adrenaline_level_user, 'chat_synopsis3': chat_synopsis3}
    return jsonify(response)

@app.route('/num_mem_objects', methods=['POST'])
def num_mem_obj():
    num = get_num_mem_objects()
    response = {'num': num}
    return jsonify(response)

@app.route('/status', methods=['POST'])
def status():
    data = request.get_json()
    message = data['msg']
    status = get_status(message, nt4)
    response = {'status': status}
    return jsonify(response)

@app.route('/plan', methods=['POST'])
def plan():
    plan = update_plan(nt4)
    response = {'plan': plan}
    return jsonify(response)

@app.route('/erc1_chat', methods=['POST'])
def erc1_chat():
    data = request.get_json()
    message = data['msg']
    erc1_response = RUN(ERC1_response(message))
    response = {'erc1_response': erc1_response}
    return jsonify(response)

@app.route('/erc2_chat', methods=['POST'])
def erc2_chat():
    data = request.get_json()
    message = data['msg']
    erc2_response = RUN(ERC2_response(message, nt4))
    response = {'erc2_response': erc2_response}
    return jsonify(response)

@app.route('/erc3_chat', methods=['POST'])
def erc3_chat():
    data = request.get_json()
    message = data['msg']
    chat_synopsis3 = data['chat_synopsis3']
    with open('ERC-neurotransmitters/new_file_path.txt', 'r') as file:
        new_file_path = file.read()
        if new_file_path == '':
            new_file_path = None
    erc3_response = RUN(ERC3_response(new_file_path, message, chat_synopsis3))

    response = {'erc3_response': erc3_response}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)

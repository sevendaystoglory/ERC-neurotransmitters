from new_main import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from history import construct_history
from neurotransmitters import Neurotransmitter
from companion.Juan.memory import *

application = Flask(__name__)
CORS(application)  # This will enable CORS for all routes

nt4=Neurotransmitter(40,20,30,20)
history_stream = construct_history()
restore_memory(temp_memory1, temp_memory2, temp_memory3, memory,chat_memory)  
@application.route('/load', methods=['POST'])
def loadmemory():
    global history_stream
    history_stream = construct_history()
    return '', 200

@application.route('/refresh', methods=['POST'])
def refresh():
    restore_memory(temp_memory1, temp_memory2, temp_memory3, memory,chat_memory)
    return '', 200
@application.route('/ntv', methods=['POST'])
def getntv():
    response = {'nt1' : nt4.array[0] , 'nt2' : nt4.array[1] , 'nt3' : nt4.array[2] , 'nt4' : nt4.array[3]}
    return(jsonify(response))
@application.route('/writememory', methods=['POST'])
def writememory():
    data = request.get_json()
    message = data['msg']
    write_to_memory(memory, temp_memory1, temp_memory2, temp_memory3, message)
    return '', 200

@application.route('/get_user_ntv', methods=['POST'])
def get_ntv():
    data = request.get_json()
    message = data['msg']
    [dopamine_level_user, endorphin_level_user, oxytocin_level_user, adrenaline_level_user, chat_synopsis3] = RUN(get_user_ntv(temp_memory3, message))
    response = {'dopamine_level_user': dopamine_level_user, 'endorphin_level_user': endorphin_level_user, 'oxytocin_level_user': oxytocin_level_user, 'adrenaline_level_user': adrenaline_level_user, 'chat_synopsis3': chat_synopsis3}
    return jsonify(response)

@application.route('/num_mem_objects', methods=['POST'])
def num_mem_obj():
    data = request.get_json()
    num = RUN(get_num_mem_objects(history_stream))
    response = {'num': num}
    return jsonify(response)

@application.route('/status', methods=['POST'])
def status():
    data = request.get_json()
    message = data['msg']
    status = RUN(get_status(nt4, message))
    response = {'status': status}
    return jsonify(response)

@application.route('/plan', methods=['POST'])
def plan():
    [reason, plan] = RUN(update_plan(temp_memory3, nt4))
    response = {'plan': plan, 'reason' : reason}
    return jsonify(response)

@application.route('/erc1_chat', methods=['POST'])
def erc1_chat():
    data = request.get_json()
    message = data['msg']
    erc1_response = RUN(ERC1_response(memory, chat_memory,message))
    response = {'erc1_response': erc1_response}
    return jsonify(response)

@application.route('/erc2_chat', methods=['POST'])
def erc2_chat():
    data = request.get_json()
    message = data['msg']
    erc2_response = RUN(ERC2_response(temp_memory2, nt4, message))
    response = {'erc2_response': erc2_response}
    return jsonify(response)

@application.route('/erc3_chat', methods=['POST'])
def erc3_chat():
    data = request.get_json()
    message = data['msg']
    chat_synopsis3 = data['chat_synopsis3']
    with open('new_file_path.txt', 'r') as file:
        new_file_path = file.read()
        if new_file_path == '':
            new_file_path = None
    erc3_response = RUN(ERC3_response(temp_memory3, history_stream,new_file_path, message, chat_synopsis3))

    response = {'erc3_response': erc3_response}
    return jsonify(response)

# if __name__ == '__main__':
#     application.run(port=5000)
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)

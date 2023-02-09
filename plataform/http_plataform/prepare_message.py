import json

def prepare_response(data):
    return json.loads(data)

def prepare_message_send_wss(name, data, request_id):
    return json.dumps(dict(
        name=name,
        msg=data,
        request_id=request_id
    )).replace("'", '"')


def prepare_message_list_ready(data):
    return json.dumps(data).replace("'", '"')
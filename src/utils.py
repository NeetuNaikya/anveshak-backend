def load_config(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config(file_path, config):
    import json
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

def format_response(data):
    return {
        "status": "success",
        "data": data
    }

def handle_error(error_message):
    return {
        "status": "error",
        "message": error_message
    }
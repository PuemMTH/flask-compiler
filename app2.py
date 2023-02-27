from flask import Flask, request, jsonify
import base64
import subprocess

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    def runCode(code, _input) -> str:
        try:
            if _input == "js" or _input == "javascript":
                p = subprocess.Popen(['node', '-e', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = p.communicate()
                if err:
                    return "Failed to run code"
                else:
                    return str(output)
            elif _input == "py" or _input == "python":
                p = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = p.communicate()
                if err:
                    return "Failed to run code"
                else:
                    return str(output)
            else:
                print("Invalid input")
        except Exception as e:
            print("Error: An error occured while running the code")
            return "Error: An error occured while running the code"
    try:
        if request.method == 'POST':
            data = request.get_json()
            code_b64 = data['code']
            language = data['lang']
            code = base64.b64decode(code_b64).decode('utf-8')
            return jsonify({ "output": runCode(code, language) })
    except Exception as e:
        print("Error: An error occured while running the code")
        return jsonify({ "output": "Error: An error occured while running the code" })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
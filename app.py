from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<filename>')
def display_file_content(filename='file1.txt'):
    try:
        start_line = int(request.args.get('start_line', 1))
        end_line = request.args.get('end_line', None)

        # Get the full path to the file
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if end_line is not None:
            end_line = int(end_line)
            content = ''.join(lines[start_line - 1:end_line])
        else:
            content = ''.join(lines[start_line - 1:])

        return render_template('file_content.html', filename=filename, content=content)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

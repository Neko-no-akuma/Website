from Flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/terms/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms/tos')
def tos():
    return render_template('tos.html')

@app.route('/invited')
def invited():
    return render_template('invited.html')

@app.route('/voted', methods=['POST'])
async def voted():
    if request.method == 'POST':
        if request.headers['Authorization'] == 'DYBTSVOTE':
            data = reequest.json
            print(data)
            return "ok"
        else:
            return "unknown vote"
    else:
        return "not a vaild method"

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.73', port=8000)
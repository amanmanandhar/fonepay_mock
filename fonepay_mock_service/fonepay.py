from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

USERS = {
    "admin": "admin123",
}

MERCHANTS = {
    "M001": {'name': 'ShopA', 'balance': 0},
    "M002": {'name': 'ShopB', 'balance': 0},
}

TRANSACTIONS = {}

@app.route('/')
def home():
    html = """
            <h2>Mock Fonepay Merchants</h2>
            <ul>
                {% for id, m in MERCHANTS.items() %}
                    <li>
                        <b>{{ id }}</b> - {{ m.name }} |
                        Balance: {{ m.balance }}
                        <a href="/merchant/{{ id }}">View</a>
                    </li>
                {% endfor %}
            </ul>
    """
    return render_template_string(html, MERCHANTS=MERCHANTS)

@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        return jsonify({
            "status": "success",
            "message": "Authenticated",
        })
    return jsonify({
        "status": "failed",
        "message": "Incorrect username or password",
    }), 401

@app.route("/merchant/<mid>", methods=["GET"])
def get_merchant(mid):
    merchant = MERCHANTS.get(mid)
    if not merchant:
        return jsonify({'status': 'Not found'}), 404
    return jsonify(merchant)

@app.route("/merchant/<mid>/view", methods=["GET"])
def merchant_view(mid):
    merchant = MERCHANTS.get(mid)
    if not merchant:
        return "Not found", 404

    html = """
    <h2>{{ mid }} - {{ merchant.name }}</h2>
    <h3>Balance: {{ merchant.balance }}</h3>
    <form method="post" action="/ui/pay/{{ mid }}">
        <input name="amount" class="form-control" placeholder="Enter amount"/>
        <button type="submit">Pay</button>
    </form>
    <form method="post" action="/ui/add/{{ mid }}">
        <button type="submit">Add +100</button>
    </form>
    <form method="post" action="/ui/reset/{{ mid }}">
    <button type="submit">Reset</button>
    </form>
    <a href="/">Back</a>
    """

    return render_template_string(html, mid=mid, merchant=merchant)

@app.route("/ui/pay/<mid>", methods=["POST"])
def ui_pay(mid):
    amount = float(request.form['amount'])
    MERCHANTS[mid]['balance'] += amount
    return f"Paid {amount}. <a href='/merchant/{mid}/view'>Back</a>"

@app.route("/ui/add/<mid>", methods=["POST"])
def ui_add(mid):
    MERCHANTS[mid]['balance'] += 100
    return  f"Added 100. <a href='/merchant/{mid}/view'>Back</a>"

@app.route("/ui/reset/<mid>", methods=["POST"])
def ui_reset(mid):
    MERCHANTS[mid]['balance'] = 0
    return f"Reset done. <a href='/merchant/{mid}/view'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
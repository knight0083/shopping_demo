from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret-key"  # 세션 사용

# 전역 데이터
users = {"test_user": "1234"}  # 기본 사용자
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 100},
]
cart = []


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for("index"))


@app.route("/cart")
def view_cart():
    return render_template("cart.html", cart=cart)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        # 결제 완료 후 장바구니 비우고 cart 페이지로 이동
        cart.clear()
        return redirect(url_for("view_cart"))
    return render_template("checkout.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        app.logger.info(f"[SIGNUP] created user={username}")
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ok = users.get(username) == password
        app.logger.info(f"[LOGIN] user={username} ok={ok}")
        if ok:
            session["user"] = username
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=False)

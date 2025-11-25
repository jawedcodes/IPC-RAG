# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.config import SQLALCHEMY_DATABASE_URI
from backend.database import db
from backend.models import QueryLog
from rag_system.pipeline import rag_answer


app = Flask(__name__)
CORS(app)

# Configure PostgreSQL DB
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init SQLAlchemy
db.init_app(app)

# Create tables if not exist
with app.app_context():
    db.create_all()


# -------------------------------------
#          RAG ENDPOINT
# -------------------------------------

@app.route("/", methods=["GET", "POST"])
def query_rag():

    answer = None
    
    if request.method == "POST":
        query = request.form.get("query", "")

        # Run RAG engine
        answer = rag_answer(query)   # return dict or tuple

        # Save query + answer into PostgreSQL
        entry = QueryLog(
            query_text=query,
            final_answer=answer
        )
        db.session.add(entry)
        db.session.commit()

    return render_template(
        "index.html",
        answer=answer
    )



if __name__ == "__main__":
    app.run(debug=True)

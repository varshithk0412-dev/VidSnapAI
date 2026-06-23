from flask import Flask, render_template, request,flash
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "wrp923rpfweownewioehrh3wr"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed(filename):
    return ('.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid4()
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text","").strip()
        input_files = []
        for key, value in request.files.items():

            file = request.files[key]
            if file and allowed(file.filename):
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  filename))
                input_files.append(filename)
        if not(input_files) : 
            flash("Cannot Proceed with zero files","failure")
            return render_template("create.html",myid=myid)
        with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
            f.write(desc)
        n = len(input_files)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt")

        with open(input_path, "w") as f:
            for fi in input_files:
                f.write(f"file '{fi}'\n")
                f.write("duration 10\n")

            f.write(f"file '{input_files[-1]}'\n")

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    return render_template("gallery.html",reels = reels)

if __name__ == "__main__" : 
    app.run(debug=False)

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from PIL import Image
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

current_user1 = ["אורח", "0", "0", "0", "guest", "0", "Dfss".encode()]
# volunteer data numbers
volunteer_name = 0
volunteer_Description = 1
volunteer_loc = 2
volunteer_pic = 3
volunteer_pic_data = 4
volunteer_date = 5
volunteer_time = 6
volunteer_limit = 7
volunteer_tag = 8
volunteer_user_data = 9
# user data numbers
user_name = 0
user_pass = 1
user_email = 2
user_phoneN = 3
user_title = 4
user_pic = 5
user_pic_data = 6

admin_code = "12345"
Auser_code = "11111"


# check if there is user active
def is_active():
    global current_user1
    if current_user1 == ["אורח", "0", "0", "0", "guest", "0", "Dfss".encode()]:
        return False
    else:
        return True


# check if admin or Auser
def is_permission():
    global current_user1
    if current_user1[4] == "admin" or current_user1[4] == "Auser":
        return True
    else:
        return False


# gets tag name return tag img address
def find_tag_img(tag):
    tag_address = []
    tag_name = 0
    tag_pic = 1
    dict_tag_adrs = {
        "גינה קהילתית": r"static\images\tree.png",
        "גינה שיקומית": "static\images\heart.png",
        "יער מאכל": "static\images\strawberry.png",
        "קבוצות וואטסאפ": "static\images\whatsapp.png",
        "החלפת זרעים ויחוריים": r"static\images\flower.png",
        "התנדבות": r"static\images\volunteer.png",
        "נטיעות": r"static\images\to_plant.png",
        "חוג בית": "static\images\home.png",
        "סיורים והדרכות": r"static\images\tours.png",
        "קורסים": "static\images\courses.png"
    }
    # run on dict check what if what tag was given and insert his address into var-tag_address.
    for item in dict_tag_adrs.items():
        if item[tag_name] == tag:
            tag_address = item[tag_pic]
    return tag_address


# from binary data to download img into library
def download_pic(pic_data, pic_name):
    stream = BytesIO(pic_data)
    image = Image.open(stream).convert("RGBA")
    photo_path = "static\\images" + "\\" + pic_name
    image.save(photo_path, format="PNG")
    return photo_path


# raise error if not active
def error():
    # e holds description of the error
    error_text = "<h1>המשתמש לא נמצא במערכת<h1>"
    error_button = " <a href='login'>התחברות</a>"
    return error_text + error_button


# sends email to the person
def send_email(gmail):
    mail_content1 = "היי,"
    mail_content2 = "ראינו שאתה מעוניין להקים פעילויות והשארת פרטים."
    mail_content3 = "נחזור אליך בהקדם!"
    mail_content4 = "תודה,"
    mail_content5 = "עמותת ונטעת"
    mail_content = mail_content1 + "\n" + mail_content2 + "\n" + mail_content3 + "\n" + mail_content4 + "\n" + mail_content5
    # The mail addresses and password
    sender_address = 'forestcity208@gmail.com'
    sender_pass = 'forestc123'
    receiver_address = gmail
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'תודה על בקשתך להיות בעל התנדבות בעמותת ונטעת'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


class volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    Description = db.Column(db.String(50), unique=False)
    loc = db.Column(db.String(200), unique=False)
    pic = db.Column(db.Text(100), unique=False)
    pic_data = db.Column(db.LargeBinary, unique=False)
    date = db.Column(db.String(10), unique=False)
    time = db.Column(db.String(10), unique=False)
    limit = db.Column(db.String(5), unique=False)
    tag = db.Column(db.String(20), unique=False)
    user_data = db.Column(db.String(200), unique=False)

    def __init__(self, name, Description, loc, pic, pic_data, date, time, limit, tag, user_data):
        self.name = name
        self.Description = Description
        self.loc = loc
        self.pic = pic
        self.pic_data = pic_data
        self.date = date
        self.time = time
        self.limit = limit
        self.tag = tag
        self.user_data = user_data

    def __repr__(self):
        return "<v  '%r, '%r, '%r','%r', '%r, '%r, '%r','%r','%r' '%r'>" % (
            self.loc, self.name, self.Description, self.pic, self.pic_data, self.date, self.time, self.limit, self.tag,
            self.user_data)

    def list_of_v(self):
        return [self.name, self.Description, self.loc, self.pic, self.pic_data, self.time, self.date, self.limit,
                self.tag, self.user_data]


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Uname = db.Column(db.String(10), unique=False)
    Upass = db.Column(db.String(10), unique=False)
    email = db.Column(db.String(30), unique=False)
    phoneN = db.Column(db.String(10), unique=False)
    title = db.Column(db.String(10), unique=False)
    pic = db.Column(db.Text(100), unique=False)
    pic_data = db.Column(db.LargeBinary, unique=False)

    def __init__(self, Uname, Upass, email, phoneN, title, pic, pic_data):
        self.Uname = Uname
        self.Upass = Upass
        self.email = email
        self.phoneN = phoneN
        self.title = title
        self.pic = pic
        self.pic_data = pic_data

    def __repr__(self):
        return '<U %r>' % self.Uname

    def list_of_u(self):
        return [self.Uname, self.Upass, self.email, self.phoneN, self.title, self.pic, self.pic_data]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        locs = []
        tags = []
        # get list of locs-will be marked on map
        for i in range(len(volunteer.query.all())):
            v_from_db = volunteer.list_of_v(volunteer.query.get(i + 1))
            locs.append(v_from_db[volunteer_loc])
            tags.append(v_from_db[volunteer_tag])
        return render_template("index.html", data=locs, tags=tags)
    if request.method == "POST":
        print(1)
        return render_template("index.html")


@app.route('/list_page', methods=['GET', 'POST'])
def list_page():
    if request.method == "GET":
        # prints to screen the list of volunteering
        v1 = volunteer.query.all()
        sock_text = []
        locs = []
        for v in v1:
            photo_path = download_pic(v.pic_data, v.pic)
            sock_text.append(
                (v.name, v.Description, v.loc, photo_path, v.pic, v.date, v.time, v.limit, v.tag, v.user_data,
                 find_tag_img(v.tag)))
            locs.append(v.loc)
        return render_template("list_page.html", data=sock_text)


@app.route('/add', methods=['GET', 'POST'])
def add():
    volunteeringS = []
    # if admin or Auser you can access
    if request.method == "GET":
        if is_permission():
            return render_template("add.html")
        else:
            return redirect("Selection_to_add")

    # add to db the info,make list of class of volunteering
    if request.method == "POST":
        name = request.form["name"]
        des = request.form["des"]
        pic = request.files['pic']
        loc = request.form["loc"]
        date = request.form["date"]
        time = request.form["time"]
        limit = request.form["limit"]
        tag = request.form["tag"]
        # binary data
        pic_data = pic.read()
        # all your data except of the user pic inserted to db and and sent to list page
        cu = current_user1
        cu.pop()
        db.session.add(
            volunteer(name=name, Description=des, loc=loc, pic=pic.filename, pic_data=pic_data, date=date, time=time,
                      limit=limit, tag=tag, user_data=str(cu)))
        db.session.commit()
        # for i in range(len(volunteer.query.all())):
        #     v = volunteer.list_of_v(volunteer.query.get(i + 1))
        #     volunteeringS.append(
        #         volunteer(v[volunteer_name], v[volunteer_Description], v[volunteer_loc], v[volunteer_pic],
        #                   v[volunteer_pic_data], v[volunteer_date], v[volunteer_time], v[volunteer_limit],
        #                   v[volunteer_tag], str(cu)))
        return render_template("add.html")



@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/amuta')
def amuta():
    return render_template("amuta.html")


@app.route('/user_place', methods=['GET', 'POST'])
def user_place():
    global current_user1
    if request.method == "GET":
        # if you are not active sends you to login
        if not is_active():
            return redirect("login")
        # if you active tou can access user page
        else:
            photo_path = "static\\images" + "\\" + current_user1[user_pic]
            return render_template("user_place.html", data=current_user1[user_name], pic=photo_path)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user1
    if request.method == "POST":
        name = request.form["username"]
        pas = request.form["psw"]
        # check login:
        for i in range(len(user.query.all())):
            users = user.list_of_u(user.query.get(i + 1))
            # check if the inserted pas equals encrypted pass in db
            print(sha256_crypt.verify(pas, users[1]))
            if name == users[0] and (pas, users[1]):
                print(1)
                # current_user1=all user data
                current_user1 = users
        if not is_active():
            return error()
        download_pic(current_user1[user_pic_data], current_user1[user_pic])
        # redirect to user place take data from there that is global and paa it to html file
        return redirect("user_place")

    if request.method == "GET":
        # if you logged in and gets here that means you pressed logout if not shoes as usual
        if is_active():
            # deletes your pic file from library
            photo_path = "static\\images\\" + current_user1[user_pic]
            os.remove(photo_path)
            # makes you guest
            current_user1 = ["אורח", "0", "0", "0", "guest", "0", "Dfss".encode()]
            photo_path = "static\\images\\profile.png"
            return redirect("/")
            # return render_template("user_place.html", data=current_user1[user_name], pic=photo_path, logOutIn="התחברות")
        else:
            photo_path = "static\\images\\profile.png"
            return render_template("login.html", pic=photo_path)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        name = request.form["name"]
        pas = request.form["psw"]
        phone = request.form["phoneN"]
        email = request.form["email"]
        code = request.form["code"]
        pic = request.files['pic1']
        pic_data = pic.read()
        # encrypt the pass
        encrypte_password = sha256_crypt.encrypt(pas)

        # if you enter as a admin:
        if code == admin_code:
            db.session.add(
                user(Uname=name, Upass=encrypte_password, phoneN=phone, email=email, title="admin", pic=pic.filename,
                     pic_data=pic_data))
            db.session.commit()
        # if you enter as a Auser:
        if code == Auser_code:
            db.session.add(
                user(Uname=name, Upass=encrypte_password, phoneN=phone, email=email, title="Auser", pic=pic.filename,
                     pic_data=pic_data))
            db.session.commit()
        # if you enter as a guest:
        if not code:
            db.session.add(
                user(Uname=name, Upass=encrypte_password, phoneN=phone, email=email, title="guest", pic=pic.filename,
                     pic_data=pic_data))
            db.session.commit()
        return redirect("login")
    if request.method == "GET":
        return render_template("sign_up.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/volunteering.html', methods=['GET', 'POST'])
def volunteering():
    if request.method == "GET":
        # gets it from client(list page) sends to (volunteering)
        my_loc = request.args.get('my_loc', None)
        title = request.args.get('title', None)
        des = request.args.get('des', None)
        pic = request.args.get('pic', None)
        date = request.args.get('date', None)
        time = request.args.get('time', None)
        limit = request.args.get('limit', None)
        tag = request.args.get('tag', None)
        user_data = request.args.get('user_data', None)
        return render_template("volunteering.html", data=my_loc, data1=title, data2=des, data3=pic, data4=date,
                               data5=time, data6=limit, data7=tag, data8=user_data)


@app.route('/Selection_to_add', methods=['GET', 'POST'])
def Selection_to_add():
    if request.method == "GET":
        return render_template("Selection_to_add.html")
    # sends email to the person
    if request.method == "POST":
        try:
            print(1)
            Email = request.form["Email"]
            send_email(Email)
            return redirect("/")
        except:
            return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)

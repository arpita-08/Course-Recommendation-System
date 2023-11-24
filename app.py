from flask import Flask,render_template,request

app=Flask(__name__)


users={'admin@gmail.com':['admin','Parthiv']}  #email:[password,username]
names_li=[value[1] for value in users.values()]

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        if 'login_email' in request.form:   
            email=request.form['login_email']
            password=request.form['login_pass']
            if email in users and users[email][0] == password:
                return render_template('index.html')
            else:
                return render_template('login3.html',message="Error: Incorrect username or password")

        elif 'signup_email' in request.form:
            signup_name=request.form['signup_name']
            signup_email=request.form['signup_email']
            signup_pass=request.form['signup_pass']

            if len(signup_pass)<6:
                return render_template('login3.html',message='small pass')

            if signup_email in users or signup_name in names_li:
                return render_template('login3.html',message='Error: Already registered')
            
            users[signup_email]=[signup_pass,signup_name]

            return render_template('index.html')


    return render_template('login3.html')


if __name__=="__main__":
    app.run(debug=True)
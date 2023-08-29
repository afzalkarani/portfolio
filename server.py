from flask import Flask, render_template, request, redirect
import  requests
import csv
app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    return   render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return   render_template('./' +page_name+'.html')

@app.route('/submit_form', methods=['POST','GET'])
def submit_contact():
    print   (   request )
    if request.method == 'POST':
        try:
            data = request.form.to_dict();
            write_to_file(data)
            write_to_csv(data)
            return   redirect('/thankyou')
        except:
            return 'something went wrong while saving file'
    else:
        return 'something went wrong while submitting data'



def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject=data['subject']
        message=data['message']
        file= database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database, delimiter=',', quotechar='"',   quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


app.run('127.0.0.1', port=5000, debug=True)
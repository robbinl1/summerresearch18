
from appfolder import appFlask
from appfolder.camera import take, send
from flask import render_template, redirect
from appfolder.forms import SubmitForm
filelist = []
config = {"filename": "image.jpg", "recognized": False}
@appFlask.route('/')
@appFlask.route('/home', methods=['GET', 'POST'])
def home():
    form = SubmitForm()
    print("stuff")
    if form.validate_on_submit():
        print("validated")
        config["filename"] = form.filename.data
        print(config["filename"])
        if config["filename"][-4:] != ".jpg":
            config["filename"]+=".jpg"
        if config["filename"] in filelist:
            i = 1
            while config["filename"] in filelist:
                config["filename"]=config["filename"][:-4]+str(i)+config["filename"][-4:]
                i+=1
        print(config["filename"])
        filelist.append(config["filename"])
        return redirect('/taking')
    return render_template('template.html', title='Turn on Camera', form=form)
@appFlask.route('/taking', methods=['GET', 'POST'])
def secondinterface():
    take(config["filename"])
    send(config["filename"])
    return redirect('/captured')

# Above this line is a sample use of a template without a form.



@appFlask.route('/captured', methods=['GET', 'POST'])
def captured():
    form = SubmitForm()
    if form.validate_on_submit():
        return redirect('/taking')
    return render_template('secondinterface.html', title='Picture Taken!',  form=form)

# Above this line is a sample use of a template with a form. 
	
# from flask_restful import Resource, Api, reqparse, abort
# api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('name')

# class FullList(Resource):
#     def get(self):
#         return user

#     def post(self):
#         args = parser.parse_args()
#         user['username'] = args['name']
#         return user['username'], 201

# api.add_resource(FullList, '/devices')

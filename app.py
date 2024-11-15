##flask app rounting



from flask import Flask

## create simple flask application using ojbect name app
app=Flask(__name__)  ##__name__ is entry point 

#crate route means when we go home page below function trigger
@app.route("/",methods=["GET"])  # GET: Used to retrieve data from the server. It's used for read-only operations.
def welcome():
    return "<h1>Welcome to the channel</h1>"  #here we also use html tag

#create rounte for index function
@app.route("/index",methods=["GET"])
def index():
    return "Welcome to index page"


# Flast HTTP GET and POST
# Variable rule if we want to give some value  ... below score is addition parameter
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is "+ str(score)




#request useful to find whether http request GET or POST
#render_template use fo
from flask import render_template,request

#for redirect another form we use redirect and url_for
from flask import redirect, url_for

#crete form 
@app.route("/form", methods=['GET','POST'])
def form():
    if request.method == 'GET': # display form
        return render_template("form.html")  #we render to that form we want to open
    else: #when request is post
        maths=float(request.form['Maths'])  #we collect all value from form for that we use 'name' field on form
        english=float(request.form['English'])
        science=float(request.form['Science'])

        average_marks = (maths + english + science)/3

        # return render_template("form.html",score=average_marks)

        # redirect to sucess and fail page
        if average_marks >= 50:
            res='success'
        else:
            res='fail'

        return redirect(url_for(res, score=average_marks))
    


#import jsonify
from flask import jsonify
# use api for this we use postman app to create api..from there we get info (more about krish naik youtube channel)
@app.route("/api",methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)





if __name__ == '__main__':
    app.run(debug=True) # wheneven we do some changes we don't need to run server again cause we do debug=True
                # bydefault it takes two argument one is url but if we don't proovide any url it takes localhost 
                # and port (port bydefaulst= 5000)

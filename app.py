from flask import Flask

## create simple flask application using ojbect name app
app=Flask(__name__)  ##__name__ is entry point 

if __name__ == '__main__':
    app.run(debug=True) # wheneven we do some changes we don't need to run server again cause we do debug=True
                # bydefault it takes two argument one is url but if we don't proovide any url it takes localhost 
                # and port (port bydefaulst= 5000)

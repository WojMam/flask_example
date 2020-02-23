# Flask example
This is exemplary flask application

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png)


## Run
To run application use below command:
```$ flask run```

Application will be available at "http://127.0.0.1:5000/" address.

## Endpoints

Endpoints         | Content
----------------- | -------------
/                 | Welcome Page
/users/{username} | Hello User Endpoint
/hello/{name}     | Hello User Page
/image            | Image exemplary Page


## Project Structure
```
/application
    /app.py
    /static
        /flaskLogo.png
    /templates
        /hello.html
        /image.html
```
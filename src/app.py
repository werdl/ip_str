from flask import Flask, request, redirect
import json
import ipstr
import socket

app=Flask("ip_str")

@app.route("/gen/<ip>")
def gen(ip):
    try:
        return json.dumps(ipstr.ip_str(ip))
    except:
        try:
            return json.dumps(ipstr.ip_str(socket.gethostbyname(ip)))
        except:
            pass
        return json.dumps({
            "code": 400,
            "content": "bad input"
        })
    

@app.route("/ip/<strd>")
def ip(strd):
    try:
        print(strd)
        return json.dumps(ipstr.str_ip(strd))
    except Exception as e:
        print(e)
        return json.dumps({
            "code": 400,
            "content": "bad input"
        })
    
@app.route("/me")
def me():
    return gen(str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)))

@app.route("/redirect/<strd>")
@app.route("/redirect/<strd>/<path>")
def redirectt(strd, path=""):
    return redirect("http://"+json.loads(ip(strd))+"/"+path)
from flask import Flask
import json
import ipstr

app=Flask("ip_str")

@app.route("/gen/<ip>")
def gen(ip):
    try:
        return json.dumps(ipstr.ip_str(ip))
    except:
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
    

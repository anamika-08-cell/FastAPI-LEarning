from fastapi import FastAPI, Depends, Header,HTTPException

app = FastAPI()

#auth example
def verify_token(token : str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code = 401,
            detail = {
                "msg": "unauthorized user !"
            }
        )
    return {
        "msg":"secure authorized access."
    }

@app.get("/secuire-user")
def secure_user(user = Depends(verify_token)):
    return user



# def common_logic():
#     return{
#         "msg":"common logic executed."
#     }

# @app.get("/home")
# def user(data = Depends(common_logic)):
#     return data

# def get_currrent_user():
#     return {
#         "msg":"Mohit"
#     }

# @app.get("/profile")
# def users(user = Depends(get_currrent_user)):
#     return user

# @app.get("/dashboard")
# def dashboard(dashboards = Depends(get_currrent_user)):
#     return dashboards





    


        

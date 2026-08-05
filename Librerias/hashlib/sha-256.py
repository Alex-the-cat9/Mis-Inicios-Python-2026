import hashlib
from secrets import token_bytes  # Cryptographically secure random generator
import json
from typing import Final
try:
    with open("DataBase.json", "r") as f:
        user_repository = json.load(f)
except FileNotFoundError:
    user_repository = {}
    with open("DataBase.json", "w", encoding="utf-8") as f:
        json.dump(user_repository, f, indent=4, ensure_ascii=False)
class Adminregister:
    def __init__(self, Username:str, Password:str):
        Password_segurity = str(Password)
        if len(Password_segurity) <= 2:
            raise PermissionError("Password short")
        if Username in user_repository:
            raise PermissionError("Username busy")
        salt: Final[bytes] = token_bytes(16)
        conbined = salt + Password_segurity.encode("utf-8")
        hash1: Final[str] = hashlib.sha256(conbined).hexdigest()
        salt_segurity = salt.hex()
        user_repository[Username] = {"Salt":salt_segurity, "password_hash":hash1}
        with open("DataBase.json", "w", encoding="utf-8") as f:
            json.dump(user_repository, f, indent=4, ensure_ascii=False)
class LogIn:
    def Login(self, Username:str, password:str) -> bool:
        try:
            password_segurity = str(password)
            if Username not in user_repository:
                return False
            conbined = bytes.fromhex(user_repository[Username]["Salt"]) + password_segurity.encode("utf-8")
            hash1: Final[str] = hashlib.sha256(conbined).hexdigest()
            if hash1 == user_repository[Username]["password_hash"]:
                return True
            else:
                return False
        except Exception:
            return False        
if __name__ == "__main__":
    try:
        on1 = Adminregister("Alex", "alex109")
        print("Alex registered")
        on2 = Adminregister("Maria", "koi1")
        print("Maria registered")
        on3 = Adminregister("Pedro", "pez10")
        print("pedro registered")
    except Exception as error:
        print(f"Error:{str(error)}")
    #proof
    try:
        view = LogIn()
        Alex = view.Login("Alex", "alex109")
        Maria = view.Login("Maria", "koi1")
        Pedro = view.Login("Pedro", "pez10")
    except Exception as error:
        print(f"Error:{str(error)}")
    else:
        if Alex and Maria and Pedro:
            print("Alex entered")
            print("Maria entered")
            print("Pedro entered")
    #test security
    try:
        #No short passwords
        pleople = Adminregister("ale", "ki")
    except PermissionError as error:
        print(f"error:{error}")
    try:
        #no duplicate users
        pleople1 = Adminregister("Alex", "ki1021")
    except PermissionError as error:
        print(f"error:{error}")
    #sha256 works
    system = LogIn()
    hacker1 = system.Login("Alex", "alex102")
    if hacker1:
        print("alert segurity")
    else:
        print("No alert segurity")
    hacker2 = system.Login("Maria", "koi4")
    if hacker2:
        print("alert segurity")
    else:
        print("No alert segurity")
    hacker3 = system.Login("Pedro", "Pez10")
    if hacker3:
        print("alert segurity")
    else:
        print("No alert segurity")
#Alex:This code took a lot of effort, but I’m well aware that it’s likely vulnerable to things like brute-force attacks; I’m going to build a better one using FastAPI.


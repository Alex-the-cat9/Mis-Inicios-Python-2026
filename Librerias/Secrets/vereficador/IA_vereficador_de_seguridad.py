def IA_vereficador_de_seguridad(token:str):
    if " " in token:
        raise PermissionError("Token con espacios en blanco")
    elif len(token) <= 10:
        raise PermissionError("Token muy corto")
    elif "12345" in token or "abcd" in token.lower():
        raise PermissionError("token predecible")
    elif not any(c.isdigit() for c in token):
        raise PermissionError("El token es inseguro: requiere al menos un número")
    
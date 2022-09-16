from bd_conection import select

def traer_nombre(cc):
    sql = "SELECT usuario.nombre FROM usuario WHERE usuario.idUsuario = %s"
    ans = select(sql, [cc])
    if len(ans) == 0: ans = ""
    else: ans = str(ans[0][0]).strip(" ")
    return ans

def verificar_contrasena(cc, password):
    ans = False
    sql = "SELECT * FROM retornarclave(%s)"
    data = select(sql, [str(cc)])
    if len(data) != 0 and data[0][0].strip() == str(password).strip(): ans = True 
    return ans

def is_admin(cc):
    sql = "SELECT tipo FROM usuario WHERE idUsuario = %s"
    data = select(sql, [cc])
    return data[0][0]

if __name__ == "__main__":
    is_admin(1000000000)
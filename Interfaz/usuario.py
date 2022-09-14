from bd_conection import select

def verificar_contrasena(cc, password):
    ans = False
    sql = "SELECT * FROM retornarclave(%s)"
    data = select(sql, [str(cc)])
    if len(data) != 0 and data[0][0].strip() == str(password).strip(): ans = True 
    return ans

if __name__ == "__main__":
    print(verificar_contrasena(1000000000, "1234"))
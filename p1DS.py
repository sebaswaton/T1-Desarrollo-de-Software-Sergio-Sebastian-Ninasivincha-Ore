import sys

def simular_enrutamiento():
    input_data = sys.stdin.read().strip().split('\n')
    if not input_data or input_data[0] == "":
        return
    
    lineas = [linea.strip() for linea in input_data if linea.strip()]
    
    n = int(lineas[0])
    rutas = []
    
    for i in range(1, n + 1):
        partes = lineas[i].split()
        path_template = partes[0]

        contenido_base = partes[1] 
        rutas.append((path_template, contenido_base))
        
    m_index = n + 1
    m = int(lineas[m_index])
    
    for i in range(m_index + 1, m_index + 1 + m):
        transicion = lineas[i]
        encontrado = False
        
        for path_template, contenido_base in rutas:
            template_parts = path_template.split('/')
            transicion_parts = transicion.split('/')
            
            if len(template_parts) == len(transicion_parts):
                es_coincidencia = True
                parametros = []
                
                for temp_part, trans_part in zip(template_parts, transicion_parts):
                    if temp_part.startswith(':'):
                        parametros.append(trans_part)
                    elif temp_part != trans_part:
                        es_coincidencia = False
                        break
                
                if es_coincidencia:
                    if parametros:
                        print(f"{contenido_base} {' '.join(parametros)}")
                    else:
                        print(contenido_base)
                    
                    encontrado = True
                    break
        
        if not encontrado:
            print("404 Not Found")

if __name__ == '__main__':
    simular_enrutamiento()
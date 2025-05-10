# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

# Procesar y extraer lexemas del buffer
def procesar_buffer(entrada, inicio, tamano_buffer):
  
  flag_saltador = " "
  flag_final = "eof"
  flag_proceso = True
  buffer = cargar_buffer(entrada=entrada, inicio=inicio, tamano_buffer=tamano_buffer)
  inicioBuffer = inicio
  inicioLexema  = inicio
  avance = 0
  lexema = ""
  
  while flag_proceso:
    
    # Creación de buffer para nueva lectura
    if avance < tamano_buffer:
      caracter = buffer[avance]
    else:
      inicioBuffer += avance
      buffer = cargar_buffer(entrada=entrada, inicio=inicioBuffer, tamano_buffer=tamano_buffer)
      avance = 0
      caracter = buffer[avance]
    
    
    # Comportamiento para punteros
    if caracter == flag_saltador:
      inicioLexema = avance + 1
      print("Lexema procesado:", lexema)
      lexema = ""  
    elif caracter == flag_final:
      print("Lexema procesado:", lexema)
      flag_proceso = False
    else:
      lexema += caracter

    avance +=1

def exampleData():  
  entrada = list("Esto es un ejemplo eof")
  inicio = 0
  tamano_buffer = 10
  procesar_buffer(inicio=inicio, tamano_buffer=tamano_buffer, entrada=entrada)
  
if __name__ == "__main__":
    exampleData()
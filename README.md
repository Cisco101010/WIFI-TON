WIFI-TON
WIFI-TON es una herramienta de Wi-Fi hacking que permite escanear redes Wi-Fi, detectar dispositivos conectados a una red y realizar ataques de fuerza bruta para intentar acceder a redes Wi-Fi protegidas.

Instalaci�n
Clona el repositorio de WIFI-TON en tu m�quina local:
shell
Copy code
git clone https://github.com/tu_usuario/WIFI-TON.git
Navega al directorio del proyecto:
shell
Copy code
cd WIFI-TON
Instala las dependencias necesarias utilizando pip:
shell
Copy code
pip install -r requirements.txt
Ejecuci�n
Aseg�rate de estar en el directorio del proyecto WIFI-TON:
shell
Copy code
cd WIFI-TON
Ejecuta el script principal main.py:
shell
Copy code
python main.py
Uso
Al ejecutar el script main.py, se presentar� un men� con diferentes opciones:

Escaneo de red: Esta opci�n permite escanear una red local para detectar los dispositivos conectados a ella. El script mostrar� una tabla con la direcci�n IP, direcci�n MAC y fabricante de cada dispositivo detectado.

Detecci�n de redes Wi-Fi: Esta opci�n realiza un escaneo de las redes Wi-Fi disponibles en el �rea. Se mostrar� una tabla con el n�mero de red, el SSID, la direcci�n BSSID y la fuerza de la se�al de cada red encontrada.

Selecciona la opci�n deseada ingresando el n�mero correspondiente. Para cancelar y salir del programa, ingresa 0 en cualquier momento.

Si seleccionas la opci�n de escaneo de red, se te pedir� ingresar la direcci�n IP del router de tu red local. Despu�s de cada escaneo, tendr�s la opci�n de regresar al men� principal o continuar con un nuevo escaneo.

Si seleccionas la opci�n de detecci�n de redes Wi-Fi, se mostrar� una lista de las redes encontradas. Podr�s seleccionar una red espec�fica ingresando su n�mero y tambi�n deber�s proporcionar una lista de contrase�as en un archivo de texto para realizar un ataque de fuerza bruta. El script intentar� conectar a la red seleccionada utilizando las contrase�as de la lista. Al finalizar, se mostrar� si se encontr� la contrase�a correcta o no.

Despu�s de cada operaci�n, se te dar� la opci�n de intentar nuevamente o volver al men� principal.

Requisitos
Python 3.6 o superior
Bibliotecas y dependencias especificadas en el archivo requirements.txt
Notas adicionales
Ten en cuenta que el uso de esta herramienta para acceder a redes Wi-Fi protegidas sin autorizaci�n es ilegal y est� sujeto a las leyes y regulaciones de tu pa�s. Utiliza esta herramienta solo con fines educativos o en redes en las que tengas permiso expl�cito para realizar pruebas de seguridad.

El desarrollador de esta herramienta no se hace responsable de ning�n uso indebido o ilegal de la misma.





import network
import socket
import time
import machine

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print(f'Conectando a la red {ssid}...')
        wlan.connect(ssid, password)

        max_wait = 15
        while max_wait > 0:
            if wlan.isconnected():
                print('Conexión exitosa')
                print('Configuración de red:', wlan.ifconfig())
                return wlan.ifconfig()[0]  # Devuelve la IP asignada
            max_wait -= 1
            print('Esperando conexión...')
            time.sleep(1)

    if wlan.isconnected():
        return wlan.ifconfig()[0]
    else:
        print('No se pudo conectar a la red WiFi')
        return None

def setup_leds():
    gpios = [machine.Pin(i, machine.Pin.OUT) for i in [15, 14, 13, 12, 11, 10]]
    return gpios

def update_leds(value, gpios):
    binary = '{:03b}'.format(value)
    for i, bit in enumerate(binary):
        gpios[i].value(int(bit))

def process_data(data):
    marker1 = data[0]
    marker2 = data[1]
    print(f"Marcador 1: {marker1}, Marcador 2: {marker2}")

    leds_marker1 = setup_leds()[:3]
    leds_marker2 = setup_leds()[3:]

    update_leds(marker1, leds_marker1)
    update_leds(marker2, leds_marker2)

# Credenciales WiFi
ssid = "MATTHEW 4711"
password = "12345678"

ip_address = connect_wifi(ssid, password)
if ip_address:
    print('Dirección IP:', ip_address)
else:
    print('Error al conectar a WiFi')
    raise SystemExit

# Socket setup
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Esperando conexión...')

while True:
    cl, addr = s.accept()
    print('Cliente conectado desde', addr)
    data = cl.recv(1024)
    if data:
        data = list(map(int, data.decode().split(',')))
        process_data(data)
    cl.close()


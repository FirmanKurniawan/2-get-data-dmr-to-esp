import serial
import time

ser_dmr = serial.Serial('COM4', 19200, timeout=1)
ser_esp = serial.Serial('COM5', 115200, timeout=1)

try:
    while True:
        data = ser_dmr.readline().decode('utf-8')
        if data == "S1":
            ser_esp.write("S1".encode('utf-8'))
            
            # Membaca data yang dikirimkan oleh perangkat ESP8266 dari COM5
            response = ser_esp.readline().decode('utf-8')
            response2 = ser_dmr.write(response.encode('utf-8'))
            print("Data yang diterima dari COM5:", response)
            print("Data yang diterima dari COM4:", response2)

except KeyboardInterrupt:
    pass
finally:
    ser_dmr.close()
    ser_esp.close()

import serial
import time

# Buka port serial di luar loop
ser = serial.Serial('COM19', 19200, timeout=1)

try:
    with open('data.txt', 'a') as file:
        while True:
            # Baca data dari port serial
            data = ser.readline().decode('utf-8').strip()
            file.write(data + '\n')
            file.flush()

            print("Data yang diterima:", data)

except KeyboardInterrupt:
    print("Proses berhenti.")
    ser.close()  # Tutup port serial saat Anda selesai

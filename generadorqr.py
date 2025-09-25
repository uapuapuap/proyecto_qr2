import qrcode

# URL de tu portafolio
url = "https://uapuapuap.github.io/proyecto_qr/"

# Crear el QR
img = qrcode.make(url)

# Guardar el QR como imagen en la misma carpeta
img.save("qr_portafolio.png")

print("QR generado correctamente.")


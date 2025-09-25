import os
import subprocess
import qrcode

# -------------------------------
# Configuración
# -------------------------------
usuario_git = "uapuapuap"
email_git = "pauamgrsm@gmail.com"
repositorio_git = "https://github.com/uapuapuap/proyecto_qr1.git"
carpeta_proyecto = r"C:\Users\Usuario\Desktop\Proyecto QR\01_CODIGO\PROYECTO_QR"
url_portafolio = "https://uapuapuap.github.io/proyecto_qr1/"
mensaje_commit = "Actualización del portafolio"

# -------------------------------
# Función para ejecutar comandos en la terminal
# -------------------------------
def run_cmd(comando, cwd=None):
    resultado = subprocess.run(comando, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(resultado.stdout)
    if resultado.stderr:
        print("Error:", resultado.stderr)

# -------------------------------
# 1. Configurar Git
# -------------------------------
run_cmd(f'git config --global user.name "{usuario_git}"')
run_cmd(f'git config --global user.email "{email_git}"')

# -------------------------------
# 2. Inicializar Git si no existe
# -------------------------------
if not os.path.exists(os.path.join(carpeta_proyecto, ".git")):
    run_cmd("git init", cwd=carpeta_proyecto)

# -------------------------------
# 3. Agregar remoto (si no existe)
# -------------------------------
remotes = subprocess.run("git remote", shell=True, cwd=carpeta_proyecto, stdout=subprocess.PIPE, text=True).stdout.split()
if "origin" not in remotes:
    run_cmd(f"git remote add origin {repositorio_git}", cwd=carpeta_proyecto)

# -------------------------------
# 4. Agregar archivos, commit y push
# -------------------------------
run_cmd("git add .", cwd=carpeta_proyecto)
run_cmd(f'git commit -m "{mensaje_commit}"', cwd=carpeta_proyecto)
run_cmd("git branch -M main", cwd=carpeta_proyecto)
run_cmd("git push -u origin main --force", cwd=carpeta_proyecto)

# -------------------------------
# 5. Generar QR
# -------------------------------
img = qrcode.make(url_portafolio)

# Carpeta para guardar el QR dentro del proyecto
qr_carpeta = os.path.join(carpeta_proyecto, "qr")
os.makedirs(qr_carpeta, exist_ok=True)
ruta_qr = os.path.join(qr_carpeta, "qr_portafolio.png")

img.save(ruta_qr)
print(f"QR generado en: {ruta_qr}")


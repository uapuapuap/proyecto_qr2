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
mensaje_commit = "Actualizar HTML avanzado y regenerar QR"

# -------------------------------
# Función para ejecutar comandos en la terminal
# -------------------------------
def run_cmd(comando, cwd=None):
    resultado = subprocess.run(comando, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if resultado.stdout:
        print(resultado.stdout)
    if resultado.stderr:
        print("Error:", resultado.stderr)

# -------------------------------
# 1. Configurar Git globalmente
# -------------------------------
run_cmd(f'git config --global user.name "{usuario_git}"')
run_cmd(f'git config --global user.email "{email_git}"')

# -------------------------------
# 2. Inicializar Git si no existe
# -------------------------------
if not os.path.exists(os.path.join(carpeta_proyecto, ".git")):
    run_cmd("git init", cwd=carpeta_proyecto)

# -------------------------------
# 3. Configurar remoto
# -------------------------------
remotes = subprocess.run("git remote", shell=True, cwd=carpeta_proyecto, stdout=subprocess.PIPE, text=True).stdout.split()
if "origin" not in remotes:
    run_cmd(f"git remote add origin {repositorio_git}", cwd=carpeta_proyecto)
else:
    # Actualizar la URL del remoto si ya existe
    run_cmd(f"git remote set-url origin {repositorio_git}", cwd=carpeta_proyecto)

# -------------------------------
# 4. Hacer commit solo si hay cambios
# -------------------------------
status = subprocess.run("git status --porcelain", shell=True, cwd=carpeta_proyecto, stdout=subprocess.PIPE, text=True).stdout
if status.strip():
    run_cmd("git add .", cwd=carpeta_proyecto)
    run_cmd(f'git commit -m "{mensaje_commit}"', cwd=carpeta_proyecto)
    run_cmd("git branch -M main", cwd=carpeta_proyecto)
    run_cmd("git push -u origin main --force", cwd=carpeta_proyecto)
else:
    print("No hay cambios nuevos para commitear. Se omite commit y push.")

# -------------------------------
# 5. Generar QR del portafolio
# -------------------------------
img = qrcode.make(url_portafolio)

qr_carpeta = os.path.join(carpeta_proyecto, "qr")
os.makedirs(qr_carpeta, exist_ok=True)
ruta_qr = os.path.join(qr_carpeta, "qr_portafolio.png")

img.save(ruta_qr)
print(f"QR generado correctamente en: {ruta_qr}")

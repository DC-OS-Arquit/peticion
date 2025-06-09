# entrar_a_wara.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Podés poner headless=False para ver el navegador
    page = browser.new_page()

    # Ir a la página de login
    page.goto("https://apps.visionblo.com/rb/")

    # Rellenar usuario y contraseña
    page.fill("#usuario", "coop12deoctubre")
    page.fill("#contrasena", "12deoctubre")

    # Hacer clic en el botón de ingresar
    page.click("button[type=submit]")

    # Esperar a que se redirija o cargue panel principal
    page.wait_for_timeout(5000)  # o usar wait_for_url()

    # Guardar la página del panel para inspección
    with open("/tmp/wara_panel.html", "w") as f:
        f.write(page.content())

    print("✅ Login exitoso. HTML del panel guardado en /tmp/wara_panel.html")

    browser.close()

# Evaluacion2Urra_Backend

## Integrante
- Nombre: Gabriel Urra
- Correo Institucional: gabriel.urra04@inacapmail.cl

## Ejecución local

Define una clave secreta antes de iniciar Django. En PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(50))"
python manage.py runserver
```
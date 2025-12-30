@echo off
setlocal

set "ROOT=%~dp0"
set "COLLECTION=%ROOT%docs\api.postman.json"

if not exist "%COLLECTION%" (
  echo [ERROR] Koleksi Postman tidak ditemukan: %COLLECTION%
  exit /b 1
)

where newman >nul 2>&1
if errorlevel 1 (
  set "NEWMAN_CMD=npx newman"
) else (
  set "NEWMAN_CMD=newman"
)

set "ARGS=run \"%COLLECTION%\""

if defined ENV_FILE (
  set "ARGS=%ARGS% -e \"%ENV_FILE%\""
)

if defined BASE_URL (
  set "ARGS=%ARGS% --env-var \"baseUrl=%BASE_URL%\""
)

if defined TOKEN (
  set "ARGS=%ARGS% --env-var \"token=%TOKEN%\""
)

echo Menjalankan Postman collection dengan perintah:
echo %NEWMAN_CMD% %ARGS% %*

call %NEWMAN_CMD% %ARGS% %*
exit /b %errorlevel%

$exclude = @("venv", "RPA_ProcesarPreparacion.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPA_ProcesarPreparacion.zip" -Force
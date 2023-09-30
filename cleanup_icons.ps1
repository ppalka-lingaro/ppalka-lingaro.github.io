# Define the path where you want to start the search.
$rootPath = ".\AWS asset package" # Replace with your start directory.

# Define folder names to search and remove
$folderNames = @("16", "32", "48")

# Recursively find and remove folders with specified names
Get-ChildItem -Path $rootPath -Recurse -Directory | ForEach-Object {
    if ($folderNames -contains $_.Name) {
        Remove-Item -Path $_.FullName -Recurse -Force
        Write-Host ("Removed: " + $_.FullName)
    }
}

# Recursively find and remove all .png files
Get-ChildItem -Path $rootPath -Recurse -File -Filter "*.png" | ForEach-Object {
    Write-Host ("Removed File: " + $_.FullName)
    Remove-Item -Path $_.FullName -Force
}

Write-Host "Script Execution Completed!"

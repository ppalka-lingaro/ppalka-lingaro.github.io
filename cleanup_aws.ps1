# Define the path where you want to start the search.
$rootPath = "icons\AWS asset package" # Replace with your start directory.

# Define folder name to search for
$folderName = "64"

# Recursively find all folders with the specified name
Get-ChildItem -Path $rootPath -Recurse -Directory -Filter $folderName | ForEach-Object {
    $parentDir = $_.Parent.FullName
    $svgFiles = Get-ChildItem -Path $_.FullName -File -Filter "*.svg"

    # Move each SVG file found to the parent directory
    foreach ($svgFile in $svgFiles) {
        $destination = Join-Path -Path $parentDir -ChildPath $svgFile.Name
        Move-Item -Path $svgFile.FullName -Destination $destination -Force
        Write-Host ("Moved: " + $svgFile.FullName + " to " + $destination)
    }
}

Write-Host "Script Execution Completed!"

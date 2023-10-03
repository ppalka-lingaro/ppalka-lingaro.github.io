# Define the path where you want to start the search.
$rootPath = "icons\AWS asset package" # Replace with your start directory.

# Define folder name to search for
#$folderName = "64"

# Recursively find all folders with the specified name
#Get-ChildItem -Path $rootPath -Recurse -Directory -Filter $folderName | ForEach-Object {
#    $parentDir = $_.Parent.FullName
#    $svgFiles = Get-ChildItem -Path $_.FullName -File -Filter "*.svg"
#
#    # Move each SVG file found to the parent directory
#    foreach ($svgFile in $svgFiles) {
#        $destination = Join-Path -Path $parentDir -ChildPath $svgFile.Name
#        Move-Item -Path $svgFile.FullName -Destination $destination -Force
#        Write-Host ("Moved: " + $svgFile.FullName + " to " + $destination)
#    }
#}

# Get all files in the directory that start with "Arch_"
$items = Get-ChildItem -Path $rootPath -Recurse | Where-Object { $_.Name -match "^Arch_" }

# Loop through the files and rename them
foreach ($item in $items) {
    #$parentDir = $item.Parent.FullName
    #Write-Host ("ParentDir: " + $parentDir)
    # Construct the new name by removing the "Arch_" prefix
    $newName = $item.Name -replace '^Arch_', ''

    # Construct the full path for the new name
    $destinationPath = Join-Path -Path $item.PSParentPath -ChildPath $newName
    #$destinationPath = Join-Path -Path $parentDir -ChildPath $newName
    # Rename the item
    Rename-Item -Path $item.FullName -NewName $newName -Force
    Write-Host ("Moved: " + $item.FullName + " to " + $newName)
}

Write-Output "Renaming completed!"

Write-Host "Script Execution Completed!"


# Set the root folder where you want to start searching
$rootFolder = "icons\Google cloud icons"

# Search for .cvg files in subfolders and move them to their parent folders
Get-ChildItem -Path $rootFolder -Filter "*.svg" -File -Recurse | ForEach-Object {
    # Calculate the destination path by combining the parent folder and the file name
    $parentFolder = $_.Directory.Parent.FullName
    $destinationPath = Join-Path -Path $parentFolder -ChildPath $_.Name

    # Move the file to its parent folder
    Move-Item -Path $_.FullName -Destination $destinationPath -Force
    Write-Host "Moved $($_.FullName) to $destinationPath"
}

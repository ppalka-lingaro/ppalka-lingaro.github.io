# Set the path to the directory where you want to search for SVG files
$directoryPath = "icons"

# Get all SVG files in the directory and its subdirectories
$svgFiles = Get-ChildItem -Path $directoryPath -Filter "*.svg" -File -Recurse

# Loop through each SVG file
foreach ($svgFile in $svgFiles) {
    # Get the relative path to the SVG file
    $relativePath = $svgFile.FullName.Replace($directoryPath, '')

    # Remove the file extension and keep only letters, spaces, and dots
    $newFileName = $svgFile.BaseName -replace "[^a-zA-Z\s\.]", ""

    # Replace underscores and hyphens with spaces
    $newFileName = $newFileName -replace "[_-]", "\ "

    # Remove any leading or trailing spaces
    $newFileName = $newFileName.Trim()

    # Combine the new file name with the .svg extension
    $newFileName = $newFileName + ".svg"

    # Create the new file path
    $newFilePath = Join-Path -Path $svgFile.Directory.FullName -ChildPath $newFileName

    # Rename the SVG file
    #Rename-Item -Path $svgFile.FullName -NewName $newFileName

    Write-Host "Renamed $($relativePath) to $newFileName"
}
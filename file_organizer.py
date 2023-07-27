import os
import pathlib
import shutil

fileFormat = {
"Web": [".html5", ".html", ".htm", ".xhtml",".csv",".webp",".acsm"],

"Picture": [".jpeg", ".jpg", ".tiff", ".gif",".heic",".HEIC"
             ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],

"Video": [".avi", ".mkv", ".flv", ".wmv",
          ".mov", ".mp4", "..webm", ". vob",
          ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],

"Document": [".oxps", ".epub", ".pages", ".docx",
              ".txt", ".pdf", ".doc", ".fdf",
              ".ods", ".odt", ".pwi", ". xsn",
              ". xps" , ".dotx", ".docm", ".dox",
              ".rvg", ".rtf", ".rtfd", ".wpd",
              ".xls", ".xlsx", ".ppt", "pptx"],

"Compressed": [".a", ".ar", ".cpio", ".iso",
                ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip"],

"Audio": [".aac", ".aa", ".aac", ".dvf",
          ".m4a", ".m4b", ".m4p", ".mp3",
           ".msv", "ogg", "oga", ".raw", 
          ".vox", ".wav", ".wma"],

"Torrent":[".srt",".torrent"],

"Installable":[".exe"],

"apk":[".apk"],

"c_cpp":[".c",".cpp"],

"python":[".py"],

"JSON":[".json"],

"font_style":[".otf"],

}

fileTypes = list(fileFormat.keys())
fileFormats= list(fileFormat.values())

# print(fileFormats)
# print(fileTypes)

for file in os.scandir():
    fileName = pathlib.Path(file)
    fileFormatType = fileName.suffix.lower()
    if fileName != "file_organizer" and fileFormatType != ".py":
        src = str(fileName)
        destination = "Other"
        if fileFormatType == "":
            print(f" {src} has no file Format")
        else:
            for formats in fileFormats:
                if fileFormatType in formats:
                    folder = fileTypes[fileFormats.index(formats)]
                    print(folder)
                    if os.path.isdir(folder) == False:
                        os.mkdir(folder)
                    destination = folder
            else :
                if os.path.isdir("Other") == False:
                    os.mkdir("Other")
            print(src,"moved to ",destination,"!")
            shutil.move(src,destination) 
    
    
print("File organizer started")  
input("\nPress Enter to exit")         
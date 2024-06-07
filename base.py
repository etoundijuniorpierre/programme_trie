from pathlib import Path

exten = {
    ".png": "Images",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".opt": "Documents",
    ".PDF": "Documents",
    ".json": "Documents",
    ".mp3": "Musiques",
    ".wav": "Musiques",
    ".iso": "Application"
}

tri_doc = Path.home()
tri_doc = tri_doc / "/home/junior/Téléchargements"
files = [f for f in tri_doc.iterdir() if f.is_file()]
for f in files:
    output_doc = tri_doc / exten.get(f.suffix, "Autres")
    output_doc.mkdir(exist_ok=True)
    f.rename(output_doc / f.name)
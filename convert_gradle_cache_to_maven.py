import os
import shutil
from pathlib import Path
from xml.etree import ElementTree as ET

INPUT_DIR = Path("~/.gradle/caches/modules-2/files-2.1").expanduser()
OUTPUT_DIR = Path("maven_repo_output")

def extract_info_from_path(path):
    parts = path.relative_to(INPUT_DIR).parts
    if len(parts) >= 3:
        group = ".".join(parts[:-3])
        artifact = parts[-3]
        version = parts[-2]
        return group, artifact, version
    return None, None, None

def convert():
    print(f"[+] Scanning: {INPUT_DIR}")
    for root, dirs, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith((".pom", ".jar", ".aar")):
                full_path = Path(root) / file
                rel_path = full_path.relative_to(INPUT_DIR)
                try:
                    parts = rel_path.parts
                    group = ".".join(parts[:-3])
                    artifact = parts[-3]
                    version = parts[-2]
                    filename = f"{artifact}-{version}{full_path.suffix}"
                    dest_path = OUTPUT_DIR / Path(group.replace(".", "/")) / artifact / version
                    dest_path.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(full_path, dest_path / filename)
                    print(f"[✓] Copied: {group}:{artifact}:{version} ({file})")
                except Exception as e:
                    print(f"[!] Error processing {full_path}: {e}")

if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    convert()
    print(f"\n[✓] Maven-style repo created at: {OUTPUT_DIR.resolve()}")

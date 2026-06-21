from importlib.metadata import files
import pathlib
import subprocess
import hashlib
import shutil

def md5_checksum(filepath):
    md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()

base_yaml = "../yaml/ithodaalderop-amber.yaml"
base_yaml_json = pathlib.Path(base_yaml).read_text()
release_file_json = pathlib.Path("./release-file-base.json").read_text()

import re
match = re.search(r'version:\s*([^\s]+)', base_yaml_json)
version_number = match.group(1) if match else "notfound"
match = re.search(r'device_name:\s*([^\s]+)', base_yaml_json)
project_name = match.group(1) if match else "notfound"

build_path = f"../yaml/.esphome/build/{project_name}"
compiled_file = f"{build_path}/.pioenvs/{project_name}/firmware.bin"

variants = [
    {"pcb": "v2", "relays": "4", "updatefile": "release-v2-4relay.json", "foldername": "firmware-4relay"},
    {"pcb": "v2", "relays": "2", "updatefile": "release-v2-2relay.json", "foldername": "firmware-2relay"},
    {"pcb": "v3", "relays": "4", "updatefile": "release-v3-4relay.json", "foldername": "firmware-4relay"},
    {"pcb": "v3", "relays": "2", "updatefile": "release-v3-2relay.json", "foldername": "firmware-2relay"},
]

for v in variants:
    version = f"PCB {v['pcb']} with {v['relays']} relays"

    print("============================================================================")
    print(f"Starting generation of firmware for {version}")
    print("============================================================================")

    # STEP 3: Compile generated YAML into ESPHome binary file
    print(f"Compiling firmware")

    result = subprocess.run(f"esphome -s relays {v['relays']} -s pcb_version {v['pcb']} compile {base_yaml}", capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Copy firmware binary to deployment directory")

        # STEP 4: Copy compiled file into version binary in correct publish directory
        version_filename = f"version-{version_number.replace('.', '-')}-{v['pcb']}.bin"
        version_path = f"../{v['foldername']}/{version_filename}"
        shutil.copy(compiled_file, version_path)

        # STEP 5: Copy compiled file into latest binary in correct publish directory
        latest_filename = f"../{v['foldername']}/latest-{v['pcb']}.bin"
        shutil.copy(compiled_file, latest_filename)

        # STEP 6: Calculate MD5 checksum
        md5 = md5_checksum(latest_filename)
        print(f"Calculated checksum: {md5}")

        # STEP 7: Update release file
        out_yaml = release_file_json.replace("##MD5##", md5).replace("##FOLDER##", v["foldername"]).replace("##FILE##", version_filename).replace("##VERSION##", version_number)
        pathlib.Path(f"../{v['updatefile']}").write_text(out_yaml)
    else:
        print(f"Compilation failed for {version}")
        print("Error output:")
        print(result.stderr)

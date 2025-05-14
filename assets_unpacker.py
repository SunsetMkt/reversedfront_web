import logging
import os
import zipfile

apk_filename = "app-release.apk"
output_dir = "extracted"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s.%(funcName)s:%(lineno)d - %(message)s",
)


def unzip_assets():
    apk_zip = apk_filename
    with zipfile.ZipFile(apk_zip, "r") as zip_ref:
        zip_ref.extractall(output_dir)


# Get script file path
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

if __name__ == "__main__":
    logging.info("开始解压资源文件")
    unzip_assets()
    logging.info("资源文件解压完成")

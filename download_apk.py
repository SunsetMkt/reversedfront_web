import logging
import os

import gdown

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s.%(funcName)s:%(lineno)d - %(message)s",
)

# Copy from https://www.reversedfront.tw/pages/tc
gdrive_url = (
    "https://drive.google.com/uc?export=download&id=1GBzaOinzk6quz88mpd7UO-KNo8qHGSSW"
)

# Get script file path
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

if __name__ == "__main__":
    output = "app-release.apk"
    logging.info(f"开始下载 {output}")
    gdown.download(url=gdrive_url, output=output, fuzzy=True)
    logging.info(f"{output} 下载完成")

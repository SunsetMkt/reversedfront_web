import logging
import os
import urllib.parse

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s.%(funcName)s:%(lineno)d - %(message)s",
)

# Copy from https://www.reversedfront.tw/pages/tc
sharepoint_url = "https://komisureiya-my.sharepoint.com/:u:/p/service/ER7BDHV4jU1Kjzh-tNITUaMBwF52Y4uHPDzaxv8Q755lpg?e=tE9aFb"


def get_sharepoint_file(url, output):
    session = requests.Session()
    r = session.get(url, allow_redirects=True)
    logging.info(f"跳转到详细页 {r.url}")
    parsed = urllib.parse.urlparse(r.url)
    base = parsed.scheme + "://" + parsed.netloc + parsed.path
    logging.info(f"基础 URL {base}")
    params = urllib.parse.parse_qs(parsed.query)
    logging.info(f"参数 {params}")
    download_base = base.replace("onedrive.aspx", "download.aspx")
    download_params = {
        "SourceUrl": params["id"][0],
    }
    download_url = download_base + "?" + urllib.parse.urlencode(download_params)
    logging.info(f"下载 URL {download_url}")
    with session.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(output, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


def get_sharepoint_file_v2(url, output):
    # Thanks to @ChinHongTan
    if "download=1" not in url:
        url = url + "&download=1"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(output, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


# Get script file path
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

if __name__ == "__main__":
    output = "app-release.apk"
    logging.info(f"开始下载 {output}")
    get_sharepoint_file(sharepoint_url, output)
    logging.info(f"{output} 下载完成")

import requests
import zipfile
import os
import io


def download_and_unzip(url, extract_to="./temp"):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Files extracted to: {extract_to}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except zipfile.BadZipFile:
        print("Error: The downloaded file is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    zip_url = "https://code.s3.yandex.net/datasets/dsplus_integrated_project_4.zip"
    output_directory = "./datasets"
    os.makedirs(output_directory, exist_ok=True)
    download_and_unzip(zip_url, output_directory)

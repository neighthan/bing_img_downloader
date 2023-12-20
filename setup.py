from setuptools import find_packages, setup

setup(
    name="bing_img_downloader",
    version="0.1.0",
    url="https://github.com/neighthan/bing_img_downloader",
    description="",
        entry_points={
        "console_scripts": [
            "dl_bing_imgs = bing_img_downloader.main:dl_bing_imgs_cli",
        ],
    },
    data_files=[
        ("config", ["config/config.toml", "config/.env"])
    ],
    install_requires=[
        "aiofiles~=23.2.1",
        "aiohttp~=3.9.0",
        "aiohttp_retry~=2.8.3",
        "piexif~=1.1.3",
        "Pillow~=10.1.0",
        "python-dateutil~=2.8.2",
        "python-dotenv~=1.0.0",
        "requests~=2.31.0",
        "urllib3~=2.0.7",
        "auto-argparse~=0.0.8",
    ],
    license="MIT",
    packages=find_packages(),
)

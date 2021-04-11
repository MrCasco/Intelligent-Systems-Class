import tarfile
from urllib import request


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
TGZ_PATH = "housing.tgz"

request.urlretrieve(HOUSING_URL, TGZ_PATH)
housing_tgz = tarfile.open(TGZ_PATH)
housing_tgz.extractall()
housing_tgz.close()

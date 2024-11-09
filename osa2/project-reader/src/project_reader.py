from urllib import request
import tomllib
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        parsed_toml = tomllib.loads(content)
        #print(parsed_toml)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            parsed_toml["tool"]["poetry"]["name"],
            parsed_toml["tool"]["poetry"]["description"],
            parsed_toml["tool"]["poetry"]["license"],
            parsed_toml["tool"]["poetry"]["authors"],
            parsed_toml["tool"]["poetry"]["dependencies"],
            parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"])

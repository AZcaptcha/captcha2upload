from distutils.core import setup

setup(
    name='captcha2upload',
    packages=['captcha2upload'],
    package_dir={'captcha2upload': 'src/captcha2upload'},
    version='0.2',
    install_requires=['requests'],
    description='Upload your image and solve captche using the AZCaptcha.com '
                  'Service',
    author='Thomanphan',
    author_email='mail@azcaptcha.com',
    url='https://github.com/Thomanphan/captcha2upload',
    download_url='https://github.com/Thomanphan/captcha2upload/tarball/0.1',
    keywords=['2captcha', 'captcha', 'Image Recognition'],
    classifiers=["Topic :: Scientific/Engineering :: Image Recognition"],
)

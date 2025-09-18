from setuptools import find_packages, setup

package_name = 'language_model'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'openai', 'chromadb', 'sentence-transformers'],
    zip_safe=True,
    maintainer='Muhammed Danso',
    maintainer_email='mahadanso79@gmail.com',
    description='RAG system server wrapper for large language model',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = language_model.ragApplication:main',
        ],
    },
)

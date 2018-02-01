from setuptools import setup

setup(
    name='ServiceLayerClient',
    version='1.0',
    py_modules=['service_layer_client'],
    license='BSD 3-Clause',
    description="A Python tool that connects to the Studyportals ServiceLayer using Studyportals reflector and retrieves data.",
    url='https://github.com/studyportals/ServiceLayerClient-python',
    author='Ugne Laima Ciziute',
    author_email='devops@studyportals.com',
    install_requires=['requests'],
	python_requires='>=3'
)
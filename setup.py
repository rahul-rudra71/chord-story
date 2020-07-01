from setuptools import setup, find_packages

setup(
    name='chord_story',
    version='0.5.0',
    author='Chord Story',
    description='fundamental game play and audio processing',
    py_modules=['chord_story.main'],
    packages = ['chord_story',],
    install_requires=['librosa','numba==0.48.0','pygame==2.0.0.dev10'],

    entry_points={
        'console_scripts': [
            'chordstory = chord_story.main:main_menu'
        ]
    }
)

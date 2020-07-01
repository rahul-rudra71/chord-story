from setuptools import setup, find_packages

setup(
    name='chordstory',
    version='0.5.0',
    author='Chord Story',
    description='fundamental game play and audio processing',
    packages = find_packages('chord_story'),
    install_requires=['librosa','numba==0.48.0','pygame==2.0.0.dev10'],

    entry_points={
        'console_scripts': [
            'chordStory = chord_story.main:start'
        ]
    }
)

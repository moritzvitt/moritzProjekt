# TODO configure the setup

from setuptools import setup, find_packages

# Project information
project_name = 'LR2Anki'
version = '0.1.0'
author = 'Your Name'
author_email = 'your_email@example.com'
description = 'Automatic Flashcard Creation with ChatGPT (LR2Anki)'

# Package requirements
requirements = [
    'pandas',
    'pyyaml',
    'logging',
]

# Additional dependencies (replace with actual library names)
# Make sure these libraries are compatible with your Python version
optional_requirements = {
    'chatgpt': ['your_chatgpt_library'],  # If using ChatGPT API
    'anki': ['your_anki_library'],  # If using a specific Anki library
    'furigana': ['your_furigana_library'],  # If using a specific furigana library
}

setup(
    name=project_name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    packages=find_packages(exclude=['tests*']),  # Excludes test directories
    install_requires=requirements,
    extras_require=optional_requirements,
    entry_points={
        'console_scripts': [
            'lr2anki = main:main',  # Replace 'main' with your script's module name
        ]
    },
)

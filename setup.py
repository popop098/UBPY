import setuptools

setuptools.setup(
    name="UBPY",
    version="1.0",
    license='MIT',
    author="Gawi_pr",
    author_email="popop098@naver.com",
    description="UniqueBot python SDK",
    long_description=open('README.md').read(),
    url="https://github.com/popop098/UBPY",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)

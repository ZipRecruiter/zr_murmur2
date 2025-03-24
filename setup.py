from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc

setup(
    name='zr_murmur2',
    version='3.4.2',
    ext_modules=[
        Extension(
            "zr_murmur2",
            [
                "src/zr_murmur2.cc",
                "src/MurmurHash2.cpp",
            ],
            include_dirs=[
                get_python_inc(),
                'include/'
            ],

        )
    ],
    url="https://github.com/gsmcwhirter/zr_murmur2",
    author="Gregory McWhirter",
    author_email="greg@ideafreemonoid.org",
    description="murmur2 python wrapper"
)

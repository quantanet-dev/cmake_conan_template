import os

os.system("conan install . -sbuild_type=Debug -of=build/generators --build=missing")
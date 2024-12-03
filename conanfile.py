from conan import ConanFile

class UnifyEngine(ConanFile):
    settings = ("os", "compiler", "build_type", "arch")
    generators = ("CMakeToolchain", "CMakeDeps")

    # def requirements(self):

    def build_requirements(self):
        self.tool_requires("cmake/3.31.0")

    def layout(self):
        self.folders.generators = ""
  
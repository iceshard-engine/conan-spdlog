from conans import ConanFile, MSBuild, CMake, tools
import shutil
import os

class spdlogConan(ConanFile):
    name = "spdlog"
    license = "MIT"
    url = "https://github.com/gabime/spdlog"
    description = "Fast C++ logging library."

    # Settings and options
    settings = "os", "compiler", "arch"

    # Iceshard conan tools
    python_requires = "conan-iceshard-tools/0.3@iceshard/stable"
    python_requires_extend = "conan-iceshard-tools.IceTools"


    # Initialize the package
    def init(self):
        self.ice_init("cmake")
        self.build_requires = self._ice.build_requires

    # Build both the debug and release builds
    def ice_build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        pass

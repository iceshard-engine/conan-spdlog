from conans import ConanFile
import os

class spdlogConan(ConanFile):
    name = "spdlog"
    license = "MIT"
    url = "https://github.com/gabime/spdlog"
    description = "Fast C++ logging library."

    # Settings and options
    settings = "os", "compiler", "arch"

    options = {
        "latest": [True, False],
        "fmt_external": [True, False]
    }
    default_options = {
        "latest": False,
        "fmt_external": False
    }

    # Iceshard conan tools
    python_requires = "conan-iceshard-tools/0.5.1@iceshard/stable"
    python_requires_extend = "conan-iceshard-tools.IceTools"


    def init(self):
        self.ice_init("cmake")
        self.build_requires = self._ice.build_requires

    def ice_source_entry(self, version):
        if self.options.latest == True:
            return "latest"
        else:
            return version

    def requirements(self):
        if self.options.fmt_external == True:
            self.requires("fmt/7.0.3@iceshard/stable")

    def ice_build(self):
        if self.options.fmt_external == True:
            self.ice_build_cmake(["Debug", "Release"], definitions={"SPDLOG_FMT_EXTERNAL":""})
        else:
            self.ice_build_cmake(["Debug", "Release"])

    def package(self):
        self.copy("LICENSE", src=self._ice.source_dir, dst="LICENSE")

        self.copy("*.h", "include/spdlog", src="{}/include/spdlog".format(self._ice.source_dir), keep_path=True, excludes=("examples/*", "misc/*"))

        build_dir = os.path.join(self._ice.out_dir, "build")
        if self.settings.os == "Windows":
            self.copy("*.lib", "lib", build_dir, keep_path=True)
        if self.settings.os == "Linux":
            self.copy("*.a", "lib", build_dir, keep_path=True)

    def package_info(self):
        self.cpp_info.includedirs = ["include/spdlog"]
        self.cpp_info.debug.libdirs = ["lib/Debug"]
        self.cpp_info.release.libdirs = ["lib/Release"]
        self.cpp_info.libdirs = []
        self.cpp_info.debug.libs = ["spdlogd"]
        self.cpp_info.release.libs = ["spdlog"]

        if self.options.fmt_external == True:
            self.cpp_info.defines = ["SPDLOG_FMT_EXTERNAL"]

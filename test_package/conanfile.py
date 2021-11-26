import os

from conans import ConanFile, CMake, tools


class EffekseerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.a", dst="bin", src="lib")
        self.copy('*.lib', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            if self.settings.os == "Windows":
                self.run(".%seffekseer_test.exe" % os.sep)
            else:
                self.run(".%seffekseer_test" % os.sep)

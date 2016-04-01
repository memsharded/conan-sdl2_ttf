from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="SDL2_ttf:shared", pure_c=True)
    x86_64_builds = []
    for build in builder.builds: # Problems installing native GL libs for x86
        if not build[0]["arch"] == "x86":
            x86_64_builds.append([build[0], build[1]])
    builder.builds = x86_64_builds
    builder.run()
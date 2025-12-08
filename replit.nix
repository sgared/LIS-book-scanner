{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
    pkgs.tesseract
    pkgs.pkg-config
    pkgs.libpng
    pkgs.libjpeg
    pkgs.zlib
    pkgs.freetype
    pkgs.fontconfig
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      pkgs.glib
      pkgs.libGL
      pkgs.libxkbcommon
      pkgs.xorg.libX11
      pkgs.xorg.libXcursor
      pkgs.xorg.libXi
      pkgs.xorg.libXrandr
      pkgs.xorg.libxcb
      pkgs.libpng
      pkgs.libjpeg
      pkgs.freetype
      pkgs.fontconfig
    ];
    PYTHONHOME = "${pkgs.python310Full}";
    PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
    LANG = "en_US.UTF-8";
    STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
    PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";
    TESSDATA_PREFIX = "${pkgs.tesseract}/share/tessdata";
  };
}
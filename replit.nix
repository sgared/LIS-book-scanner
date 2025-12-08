{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
    pkgs.tesseract4
    pkgs.pkg-config
    pkgs.zlib
    pkgs.libjpeg
    pkgs.libpng
    pkgs.freetype
    pkgs.fontconfig
    pkgs.glib
    pkgs.cairo
    pkgs.pango
    pkgs.gtk3
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      pkgs.glib
      pkgs.xorg.libX11
      pkgs.xorg.libXext
      pkgs.xorg.libXrender
      pkgs.xorg.libxcb
      pkgs.xorg.libXau
      pkgs.xorg.libXdmcp
      pkgs.libjpeg
      pkgs.libpng
      pkgs.freetype
      pkgs.fontconfig
      pkgs.cairo
      pkgs.pango
      pkgs.gtk3
    ];
    PYTHONHOME = "${pkgs.python310Full}";
    PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
    LANG = "en_US.UTF-8";
    TESSDATA_PREFIX = "${pkgs.tesseract4}/share/tessdata";
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      pkgs.glib
    ];
  };
}
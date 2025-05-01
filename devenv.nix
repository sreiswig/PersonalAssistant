{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:
let
  buildInputs = with pkgs; [
    cudaPackages.cudatoolkit
  ];
in
{
  # https://devenv.sh/basics/
  env.GREET = "Python Environment Personal Assistant";

  # https://devenv.sh/packages/
  packages = [
    pkgs.git
    pkgs.portaudio
    pkgs.ffmpeg
    pkgs.libGL
    pkgs.fontconfig
    pkgs.libxkbcommon
    pkgs.freetype
    pkgs.zstd
    pkgs.dbus
    pkgs.krb5
    pkgs.kdePackages.kirigami
    pkgs.wayland
  ];

  env = {
    LD_LIBRARY_PATH = "${lib.makeLibraryPath buildInputs}:/run/opengl-driver/lib:/run/opengl-driver-32/lib";
    CUDA_PATH = pkgs.cudaPackages.cudatoolkit;
  };

  # https://devenv.sh/languages/
  # languages.rust.enable = true;
  languages.python = {
    enable = true;
    uv.enable = true;
    venv.enable = true;
    venv.requirements = ./requirements.txt;
  };

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
  scripts.hello.exec = ''
    echo hello from $GREET
  '';

  enterShell = ''
    hello
    git --version
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}

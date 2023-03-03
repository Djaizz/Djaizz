# TODO: adapt to & test on Windows


python -m pip install Poetry --upgrade --user


# Options:
#   -G, --group=GROUP          The group to add the dependency to. [default: "main"]
#   -D, --dev                  Add as a development dependency. (Deprecated)
#   -e, --editable             Add vcs/path dependencies as editable.
#   -E, --extras=EXTRAS        Extras to activate for the dependency. (multiple values allowed)
#       --optional             Add as an optional dependency.
#       --python=PYTHON        Python version for which the dependency must be installed.
#       --platform=PLATFORM    Platforms for which the dependency must be installed.
#       --source=SOURCE        Name of the source to use to install the package.
#?      --allow-prereleases    Accept prereleases.
#?      --dry-run              Output the operations but do not execute anything (implicitly enables --verbose).
#+      --lock                 Do not perform operations (only update the lockfile).
#   -h, --help                 Display help for the given command. When no command is given display help for the list command.
#   -q, --quiet                Do not output any message.
#   -V, --version              Display this application version.
#       --ansi                 Force ANSI output.
#       --no-ansi              Disable ANSI output.
#+  -n, --no-interaction       Do not ask any interactive question.
#       --no-plugins           Disables plugins.
#       --no-cache             Disables Poetry source caches.
#   -C, --directory=DIRECTORY  The working directory for the Poetry command (defaults to the current working directory).
#+  -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.

# base/main deps
grep '^[A-Za-z].*' metadata/requirements/base.txt | sed 's/.*/"&"/' | ^
  xargs poetry add ^
  --lock ^
  --no-interaction ^
  --verbose

# optional deps
for DEP_GRP in build dev doc lint publish test viz
do
  grep '^[A-Za-z].*' metadata/requirements/$DEP_GRP.txt | sed 's/.*/"&"/' | ^
    xargs poetry add ^
    --group=$DEP_GRP ^
    --optional ^
    --lock ^
    --no-interaction ^
    --verbose
done

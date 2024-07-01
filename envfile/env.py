import os
import argparse
import sys

workspace_dir = os.getenv("GPTSCRIPT_WORKSPACE_DIR", "./")
file = os.path.join(workspace_dir, "gptscript.env")


class DefaultHelpArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stdout.write("Set and update environment variables using this tool")
        sys.exit(0)


def read_env_vars(filename=file):
    """Read environment variables from a file and return them as a dictionary."""
    env_vars = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if not line.strip() or line.strip().startswith("#"):
                    continue  # Skip comments and empty lines
                key, value = line.strip().split("=", 1)
                env_vars[key] = value
    except FileNotFoundError:
        pass  # If file not found, return an empty dict
    return env_vars


def save_env_vars(env_vars, filename=file):
    """Save environment variables to a file."""
    with open(filename, "w") as file:
        for key, value in env_vars.items():
            file.write(f"{key}={value}\n")


def set_env_var(key, value, env_vars):
    """Set an environment variable in the dictionary."""
    env_vars[key] = value


def get_env_var(key, env_vars):
    """Get an environment variable from the dictionary."""
    return env_vars.get(key)


def remove_env_var(key, env_vars):
    """Remove an environment variable from the dictionary."""
    if key in env_vars:
        del env_vars[key]


def main():
    parser = DefaultHelpArgParser(
        description="Manage environment variables in gptscript.env file."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand 'get'
    parser_get = subparsers.add_parser(
        "get", help="Get the value of an environment variable"
    )
    parser_get.add_argument(
        "key",
        type=str,
        help="Key of the environment variable to get",
        default=os.getenv("key"),
        nargs="?",
    )

    # Subcommand 'set'
    parser_set = subparsers.add_parser(
        "set", help="Set the value of an environment variable"
    )
    parser_set.add_argument(
        "key",
        type=str,
        help="Key of the environment variable",
        default=os.getenv("key"),
        nargs="?",
    )
    parser_set.add_argument(
        "value", type=str, help="Value to set", default=os.getenv("value"), nargs="?"
    )

    # Subcommand 'remove'
    parser_remove = subparsers.add_parser(
        "remove", help="Remove an environment variable"
    )
    parser_remove.add_argument(
        "key",
        type=str,
        help="Key of the environment variable to remove",
        default=os.getenv("key"),
        nargs="?",
    )

    args = parser.parse_args()

    env_vars = read_env_vars()  # Read variables at the start

    if args.command == "get":
        print(get_env_var(args.key, env_vars))
    elif args.command == "set":
        set_env_var(args.key, args.value, env_vars)
        save_env_vars(env_vars)
    elif args.command == "remove":
        remove_env_var(args.key, env_vars)
        save_env_vars(env_vars)


if __name__ == "__main__":
    main()

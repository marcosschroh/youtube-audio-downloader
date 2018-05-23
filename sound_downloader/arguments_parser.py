import os
import click

ALLOWED_FILE_EXTENSIONS = ("yml", "yaml")


def get_file_extension(path_file):
        return path_file.split(".")[-1]


def validate_config_file(ctx, param, file_path_value):
    if not file_path_value:
        raise click.BadParameter(
            "Please provide a config file.")

    if not os.path.exists(file_path_value) or not os.path.isfile(file_path_value):
        raise click.BadParameter(
            "The config file %s does not exists." % file_path_value)

    file_extension = get_file_extension(file_path_value)

    if file_extension not in ALLOWED_FILE_EXTENSIONS:
        raise click.BadParameter("Only allow .yml and .yaml files.")

    return file_path_value


def validate_target(ctx, param, destiny):
    if not os.path.isdir(destiny):
        raise click.BadParameter("Invalid PATH TO SAVE.")

    return destiny

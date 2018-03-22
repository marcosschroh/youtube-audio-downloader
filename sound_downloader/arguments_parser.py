import os
import click

ALLOWED_FILE_EXTENSIONS = ("txt", "csv", "json")


def get_file_extension(path_file):
        return path_file.split(".")[-1]


def validate_file(ctx, param, file_path_value):
    if not file_path_value or not os.path.exists(file_path_value) or not os.path.isfile(file_path_value):
        raise click.BadParameter(
            "The file %s does not exists" % file_path_value)

    file_extension = get_file_extension(file_path_value)

    if file_extension not in ALLOWED_FILE_EXTENSIONS:
        raise click.BadParameter("Only allow .txt, .json and .csv files.")

    return file_path_value


def validate_target(ctx, param, destiny):
    if not os.path.isdir(destiny):
        raise click.BadParameter("Invalid PATH TO SAVE.")

    return destiny

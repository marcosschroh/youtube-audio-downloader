import os
import click


def validate_config_file(ctx, param, file_path_value):
    if not file_path_value or not os.path.exists(file_path_value) or not os.path.isfile(file_path_value):
        raise click.BadParameter(
            "The config file %s does not exists" % file_path_value)

    return file_path_value


def validate_target(ctx, param, destiny):
    if not os.path.isdir(destiny):
        raise click.BadParameter("Invalid PATH TO SAVE.")

    return destiny

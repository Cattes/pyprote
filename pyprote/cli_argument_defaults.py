"""This module contains the cli arguments with their default values."""
format_dict_defaults = {
    "package_name": "my_cool_package_name",
    "package_version": "0.1.0",
    "package_description": "My cool package description",
    "package_author_name": "John Doe",
    "package_author_email": "john@doe",
    "package_link": "https://cool.package",
}

out_dir_default = "pyprote_output_dir"

example_call = "pyprote "
for argument_name, default_val in format_dict_defaults.items():
    example_call = f"{example_call} --{argument_name} '{default_val}'"
example_call = f"{example_call} --out_dir '{out_dir_default}'"

def copy_file(command: str) -> None:
    rep_command = command.split(" ")
    if len(rep_command) != 3:
        return

    cp, source_file, new_file = rep_command

    if cp != "cp":
        return

    if source_file == new_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not exists.")

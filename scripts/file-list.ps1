function file-list {
    param(
        [Alias("i")][string]$include = "",
        [Alias("e")][string]$exclude = ""
    )

    $scriptPath = "<ABSOLUTE PATH TO file_list.py>"
    $arguments = @()

    if ($include) {
        $arguments += "--include"
        $arguments += $include
    }

    if ($exclude) {
        $arguments += "--exclude"
        $arguments += $exclude
    }

    & python $scriptPath $arguments
}
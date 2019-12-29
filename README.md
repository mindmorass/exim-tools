# exim-tools

## exipick2json.py

### example usage

Optional `--show-vars` can be added by creating a file name called [`exim-show-vars.txt`](exim-show-vars.txt) in the same directory that houses `exipick2json.py`.
Within this text file, drop the variables you want to see as JSON, one per line.

see https://linux.die.net/man/8/exipick for available variables to put into this file.

```
exipick -bpa --flatq --unsorted --show-vars message_exim_id,message_body,recipients | ./exipick2json.py
```

Do no use `message_headers`, this is a special case that is not yet supprted. The `recipients` variable is always inerpreted, make sure it is passed to `--show-vars`


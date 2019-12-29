# exim-tools

## exipick2json.py

### example usage

Optional `--show-vars` can be added by creating a file name called [`exim-show-vars.txt`](exim-show-vars.txt) and dropping the headers you want to see, one per line.
see https://linux.die.net/man/8/exipick for available variables.

hand in hand, make sure to pass the same variables to the `--show-vars` argument for exipick.  The result will be JSON.

```
exipick -bpa --flatq --unsorted --show-vars message_exim_id,message_body,recipients | ./exipick2json.py
```

Do no use `message_headers`, this is a special case that is not yet supprted. The `recipients` variable is always inerpreted, make sure it is passed to `--show-vars`


# exim-tools

## exipick2json.py

### example usage

update the variables to show for the exipick command in the `exipick2json.py` script.

```
o.set_show_vars([
    'message_exim_id',
    'message_body'
])
```

hand in hand, make sure to pass the same variables to the `--show-vars` argument for exipick.  The result will be JSON.

```
exipick -bpa --flatq --unsorted --show-vars message_exim_id,message_body,recipients | ./exipick2json.py
```

Do no use `message_headers`, this is a special case that is not yet supprted. The `recipients` variable is always inerpreted, make sure it is passed to `--show-vars`


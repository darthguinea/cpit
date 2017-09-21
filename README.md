# Cpit (README.md)

Application to copy encrypted message from the console (and in plaintext to the clipboard)

[HowTo Documentation](https://github.com/darthguinea/cpit/wiki)


**Quick Example:**

Create an .py file (in this case, example.py),
be warned that this will build a server when you execute it:
```bash
cat /some/large/textfile.txt | cpit -v
```

```bash
> echo "hello world\!" | cpit -v
[21/09/2017 05:22:23] [INFO]: Data copied from stdin.
[21/09/2017 05:22:23] [INFO]: Message [{'ks': 128, 'cipher': 'aes', 'mode': 'ccm', 'v': 1, 'adata': '', 'iv': 'W6oc68PgTqxWbVIxajFj+Q==', 'salt': 'k332Fe7RBBw=', 'ts': 64, 'iter': 1000, 'ct': 'lZvXzzYnZiEk/aQ+C8pRNYu6isoz+Q=='}]
```


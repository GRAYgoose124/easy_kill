# About

I don't like how the python terminal behaves on keyboard interrupt.

This fixes that. Yep, that's it.


# Installing & Running

    git clone git@github.com:GRAYgoose124/easy_kill.git
    cd easy_kill

    pip install poetry
    poetry install
    
That'll do it.

To use simply:
```python
    from easy_kill import die_easy

    if __name__ == '__main__':
        die_easy()

        # Ctrl-C to exit().
        input()
```
or
```python
    from easy_kill import die_easy

    @die_easy
    def func_to_die():
        # Ctrl-C to exit().
        input()
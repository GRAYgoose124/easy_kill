import pytest


def fake_input(func):
    """Decorator to fake input() calls in tests."""

    def wrapper(*args, **kwargs):
        old_input = input
        
        def new_input(prompt=""):
            raise KeyboardInterrupt
        
        g = globals()['__builtins__']
        g['input'] = new_input

        func(*args, **kwargs)

        g['input'] = old_input
    return wrapper


def with_raises_sysexit(f):
    """Decorator to assert that a function raises a non-error SystemExit."""

    with pytest.raises(SystemExit) as wrapped_e:
        f()

        assert wrapped_e.type == SystemExit
        assert wrapped_e.value.code == 0

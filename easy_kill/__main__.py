from typing import Callable


def die_easy(func: Callable = None) -> Callable:
    """Decorator and global hook to kill interactive Python sessions easily. 
    
    If used as a global function it replaces the default input() function 
    with a wrapper that catches KeyboardInterrupt and exits the program instead.

    If used as a decorator it catches KeyboardInterrupt from the decorated
    function and exits the program instead.
    """
    
    if func is not None:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                exit()

        return wrapper
    else:
        old_input = input
        def input_wrapper(prompt=""):
            try:
                return old_input(prompt)
            except KeyboardInterrupt:
                exit()


        g = globals()['__builtins__']
        if hasattr(g, '__dict__'):
            g = g.__dict__

        g['input'] = input_wrapper


def main():
    import code
    import readline

    die_easy()
    
    console = code.InteractiveConsole(locals=globals())
    console.interact()
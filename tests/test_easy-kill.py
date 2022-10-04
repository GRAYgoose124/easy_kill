import code

from easy_kill import die_easy
from tests.helpers import fake_input, with_raises_sysexit


def test_easy_kill_deco():
    @die_easy
    def func_to_die():
        raise KeyboardInterrupt
        
    with_raises_sysexit(func_to_die)


@fake_input
def test_easy_kill_hook():
    die_easy()
    console = code.InteractiveConsole()

    with_raises_sysexit(console.raw_input)


@fake_input
def test_easy_kill_hook_interact():
    die_easy()
    console = code.InteractiveConsole()

    with_raises_sysexit(console.interact)

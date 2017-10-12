# encoding: utf8

import click
import subprocess


VOICES = {
    "english",
    "english-mb-en1",
    "english-us",
    "en-scottish",
    "default",
    "english-north",
    "english_rp",
    "us-mbrola-2",
    "us-mbrola-1",
    "us-mbrola-3",
    "en-german",
    "en-german-5",
    "en-greek",
    "en-romanian",
    "english_wmids",
    "en-dutch",
    "en-french",
    "en-french",
    "en-hungarian",
    "en-swedish-f",
    "en-westindies",
    "en-afrikaans",
    "en-polish",
    "en-swedish",
}


def speak(voice, speed, words):
    words = list(words)
    command = ['espeak', '-v', voice, '-s', speed, ' '.join(words)]
    subprocess.check_output(command)


@click.command()
@click.option('--voice', default='en-german-5')
@click.option('--speed', default='175')
@click.argument('words', nargs=-1, required=True)
def say(voice, speed, words):
    """Speak words!"""
    speak(voice, speed, words)


@click.command()
def voices():
    """List voices!"""
    for voice in sorted(VOICES):
        click.echo(voice)


@click.group(commands={'say': say, 'voices': voices})
def zae():
    pass


def main():
    """Assemble and run the tool."""
    zae()

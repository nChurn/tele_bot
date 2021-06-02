from loguru import logger
import sys

from settings import DEBUG_MODE
log = logger

if DEBUG_MODE:
    log.add(sys.stdout, format="{time}  -{level}    -{message}", level='DEBUG')
    log.add('logs/info.log', format="{time} -   <green>{level}</green>  -   {message}", rotation="5 MB", colorize=True, level='INFO', compression='zip')
    log.add(sys.stdout, format="{time}  -   <yellow>{level}</yellow> -   {message}", colorize=True, level='WARNING')
    log.add(sys.stdout, format="{time}  -   <red>{level}</red>  -   {message}", colorize=True, level='ERROR')

else:
    log.add(sys.stdout, format="{time}     -     {level}     -     {message}", level='DEBUG')
    log.add('logs/info.log', format="{time}     -<green>     {level}     -     {message}", rotation="5 MB", colorize=True, level='INFO', compression='zip')
    log.add(sys.stdout, format="{time}     -     {level}     -     {message}", level='WARNING')
    log.add(sys.stdout, format="{time}     -    {level}     -     {message}", level='ERROR')

if __name__ == '__main__':
    log.error('sosi')
    log.warning('pisos')
    log.info('mraz')
    log.debug('tupaya')
from setuptools import setup

setup(name='tic_tac_toe',
      version='0.1.0',
      description='Command Line TicTacToe with win/loss/draw prediction per box, per move',
      url='https://github.com/HusainZafar/tic_tac_toe',
      author='Husain Zafar',
      author_email='husainzafar1996@gmail.com',
      license='MIT',
      packages=['tic_tac_toe'],
      install_requires=[
        'future',
      ],

      entry_points = {
      'console_scripts':[
          'tic_tac_toe = tic_tac_toe.tic_tac_toe:main'
      ]
      },
)

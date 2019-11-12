# Console Game
Launch the project (in the terminal):
python3 main.py

Running tests (in the terminal):
python3 -m unittest -v TestCreating.py

Description of the project architecture:
The used pattern is Abstract Factory, Composite and Proxy.

There are four army: Water, Earth, Fire and Air. The user can choose one of them and create some soldiers (Magic Girl, Magic Bor or Magic Pet). The user has some coins, and if there is not enough coins, the user can't create new soldiers. When the user create new soldier, he should come up with a original name for it. 
If the user write the wrong name of soldier or army, the program asks to repeat correctly.
The user has the opportunity to change the army and create soldiers in another.

The user can create two armies and begin the war between them. Every soldier has some parametrs : healthy, force, protection.
The army can consist of both individual soldiers and union of several units. There are functions to attack, treat and find out the health of armies.

Write "attack" - armies attack each other.
Write "treat" - armies treat their soldiers only if they have Magic Animals, because only this kind of soldier can treat other soldiers.
Write "health" - the health of each armies is displayed.

To complete the program, you should enter Q.

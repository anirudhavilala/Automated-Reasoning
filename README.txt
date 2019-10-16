****** AI PROJECT - 2 AUTOMATED REASONING ******

-------------------------------------------------------------------------------------
The Programs use the following built-in packages

1.copy
3.random
4.time
5.sys

-------------------------------------------------------------------------------------

To run the programs: Open command prompt at the folder where the files are present or open the command prompt and change working directory to that folder.


1. To run Basic Model Checking - truth table enumeration program, Type the following command in cmd:
	
	ModCheck.py
   
// The program runs in a loop, after checking a given propositional sentence it asks whether you have any more sentences to check,
Press "y" to check more sentences
Press "n" to terminate the program.

// The propositional sentences for the problems in the appropriate input format are given below:
#1
P , P -> Q |= Q

#2
! P11 , B11 <> P12 v P21 , B21 <> P11 v P22 v P31 , ! B11 , B21 |= P12
! P11 , B11 <> P12 v P21 , B21 <> P11 v P22 v P31 , ! B11 , B21 |= ! P12

#3
Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Mythical
Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= ! Mythical
Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Magical
Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Horned

#4.a
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Amy
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Amy
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Bob
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Bob
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Cal
Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Cal

#4.b 
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Amy
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Amy
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Bob
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Bob
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Cal
Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Cal

2. To run WalkSAT program, Type the following command in cmd:
	
	WalkSAT.py
   
// The program runs in a loop, after checking a given propositional sentence it asks whether you have any more sentences to check,
Press "y" to check more sentences
Press "n" to terminate the program.

// The propositional sentences for the problems in the CNF form in the appropriate input format are given below:
#1.  
P , ! P v Q |= Q
P , ! P v Q |= ! Q

#2.
! P11 , ! B11 v P12 v P21 ^ ! P12 v B11 ^ ! P21 v B11 , ! B21 v P11 v P22 v P31 ^ ! P11 v B21 ^ ! P22 v B21 ^ ! P31 v B21 , ! B11 , B21 |= P12
! P11 , ! B11 v P12 v P21 ^ ! P12 v B11 ^ ! P21 v B11 , ! B21 v P11 v P22 v P31 ^ ! P11 v B21 ^ ! P22 v B21 ^ ! P31 v B21 , ! B11 , B21 |= ! P12

#3
! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Mythical
! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= Mythical
! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Magical
! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Horned

#4.a
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Amy
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Amy
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Bob
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Bob
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Cal
! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Cal

#4.b
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Amy
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Amy
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Bob
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Bob
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Cal
! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Cal

// The Problems in the appropriate input format have also been commented in the programs

The End.
*************************************************************************************
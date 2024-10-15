DROP DATABASE IF EXISTS colosseum;
CREATE DATABASE colosseum;
USE colosseum;

DROP TABLE IF EXISTS Prompts;
CREATE TABLE Prompts(Scene VARCHAR(20), Prompt VARCHAR(255));
TRUNCATE TABLE Prompts;
INSERT INTO Prompts (Scene, Prompt) VALUES
		('Main','In front of you stands the Grand Colosseum, and to your left is a shop called \"Bragge\'s Armoury & Training!\"'),
        ('Shop','Welcome! We\'ve got everything from swords and armour to training!');
        
DROP TABLE IF EXISTS Weapons;
CREATE TABLE Weapons(WeaponName VARCHAR(20), BaseDamage INT, Auxillary BOOL);
TRUNCATE TABLE Weapons;
INSERT INTO Weapons (WeaponName, BaseDamage, Auxillary) Values 
		('none', 0, False),
		('shield', 1, True),
        ('dagger', 1, True),
        ('sword', 3, False),
        ('curved sword', 3, False),
        ('great sword', 5, False),
        ('war axe', 4, False),
        ('great axe', 6, False);


DROP TABLE IF EXISTS Skills;
CREATE TABLE Skills(SkillName VARCHAR(20), Equipable VARCHAR(25), Multiplier INT, Cooldown INT);
TRUNCATE TABLE Skills;
INSERT INTO Skills (SkillName, Equipable, Multiplier, Cooldown) VALUES
		('basic attack', 'all', 1, 0),
        ('bash', 'shield/great', 1, 2),
        ('blind spot', 'curved sword/dagger', 3, 2),
        ('backstab', 'dagger', 5, 3),
        ('thrust', 'sword', 2, 1),
        ('giant hunt', 'great sword', 5, 3),
        ('block', 'shield', 0, 0),
        ('guard', 'all', 0, 2),
        ('tree feller', 'great axe', 3, 2),
        ('sweep', 'axe', 2, 1);
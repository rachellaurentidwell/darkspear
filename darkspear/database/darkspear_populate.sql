/*

NAME:          darkspear_populate.sql
LAST MODIFIED: November 21, 2018
DESCRIPTION:   Table population for Darkspear database.

*/

use darkspear;

delete from Clan_announcement;
delete from Clan_event;
delete from C_chat;
delete from F_chat;
delete from Clan_games;
delete from Plays_game;
delete from Player_in_clan;
delete from Game_platform;
delete from Clan;
delete from Player;
delete from Game;



-- Player table
-- ===========================================================================

insert into Player
values
('starryfrog', 'rachellaurentidwell@gmail.com',
 '23peachbubbles', false, 'My name is Rachel
  and I love frogs');

insert into Player
values
('Zuroke', 'heredia.m.jeffrey@gmail.com',
 'poophead', true, 'My name is Jeff
  and I love voldemort');

insert into Player
values
('Stoick', 'att162@humboldt.edu',
 'freyaisthebest', true, 'My name is Andy and I love
  freya');

insert into Player
values
('Bitandia', 'mtt177@humboldt.edu',
 'Applejuicelife', true, 'My name is Michael
  and I love WoW');

-- Game table
-- ===========================================================================

insert into Game
values
('League of Legends', 'MOBA', 5, 'Teen', 1, 0, 1);

insert into Game
values
('World of Warcraft', 'MMORPG', 100, 'T', 1, 1, 1);

insert into Game
values
('Overwatch', 'FPS', 6, 'PEGI 12', 1, 0, 1);

insert into Game
values
('Monster Hunter World', 'ARPG', 4, 'T', 0, 1, 0);

insert into Game
values
('Runescape', 'MMORPG', 100, 'E', 0, 1, 1);

-- Game platform table
-- ===========================================================================

insert into Game_platform
values
('League of Legends', 'PC');

insert into Game_platform
values
('World of Warcraft', 'PC');

insert into Game_platform
values
('Overwatch', 'PC');

insert into Game_platform
values
('Overwatch', 'XBOX');

insert into Game_platform
values
('Overwatch', 'Playstation');

insert into Game_platform
values
('Monster Hunter World', 'PC');

insert into Game_platform
values
('Monster Hunter World', 'XBOX');

insert into Game_platform
values
('Monster Hunter World', 'Playstation');

insert into Game_platform
values
('Runescape', 'PC');

-- Clan table
-- ===========================================================================

insert into Clan
values
('Voldemorts Army', 'Zuroke', 5, 20, 'We will obliterate all muggles
and put mudbloods in their place');

insert into Clan
values
('Ron Weaslies', 'starryfrog', 10, 20, 'We are here to do the Ron Weasly
on all your asses');

insert into Clan
values
('Ravenclaws', 'Bitandia', 7, 100, 'For the Horde');

insert into Clan
values
('Freyas', 'Stoick', 10, 40, 'Freya will end you, watch out.');


-- Player_in_clan table
-- ===========================================================================

insert into Player_in_clan
values
('Zuroke', 'Voldemorts Army');

insert into Player_in_clan
values
('starryfrog', 'Voldemorts Army');

insert into Player_in_clan
values
('Bitandia', 'Voldemorts Army');

insert into Player_in_clan
values
('Stoick', 'Voldemorts Army');

insert into Player_in_clan
values
('starryfrog', 'Ron Weaslies');

insert into Player_in_clan
values
('Bitandia', 'Ron Weaslies');

insert into Player_in_clan
values
('Stoick', 'Ron Weaslies');

insert into Player_in_clan
values
('starryfrog', 'Ravenclaws');

insert into Player_in_clan
values
('Bitandia', 'Ravenclaws');

insert into Player_in_clan
values
('Stoick', 'Ravenclaws');

insert into Player_in_clan
values
('starryfrog', 'Freyas');

insert into Player_in_clan
values
('Bitandia', 'Freyas');

insert into Player_in_clan
values
('Stoick', 'Freyas');

-- Plays_game table
-- ===========================================================================

insert into Plays_game
values
('Zuroke', 'League of Legends');

insert into Plays_game
values
('Zuroke', 'Overwatch');

insert into Plays_game
values
('Zuroke', 'Runescape');

insert into Plays_game
values
('Zuroke', 'Monster Hunter World');

insert into Plays_game
values
('starryfrog', 'League of Legends');

insert into Plays_game
values
('starryfrog', 'Runescape');

insert into Plays_game
values
('Bitandia', 'Overwatch');

insert into Plays_game
values
('Bitandia', 'World of Warcraft');

insert into Plays_game
values
('Bitandia', 'Monster Hunter World');

insert into Plays_game
values
('Stoick', 'Overwatch');

insert into Plays_game
values
('Stoick', 'Monster Hunter World');

-- Clan_games table
-- ===========================================================================

insert into Clan_games
values
('Voldemorts Army', 'League of Legends', 'Gold3');

insert into Clan_games
values
('Voldemorts Army', 'Overwatch', 'gold');

insert into Clan_games
values
('Ron Weaslies', 'League of Legends', 'diamond4');

insert into Clan_games
values
('Ravenclaws', 'Overwatch', 'silver');

insert into Clan_games
values
('Ravenclaws', 'World of Warcraft', '2000');

insert into Clan_games
values
('Freyas', 'Overwatch', 'gold');


-- F_chat table
-- ===========================================================================

 insert into F_chat
 values
 ('Zuroke', 'starryfrog', 'starryfrog', 'nooblife', '2018-11-25 11:50:01');

  insert into F_chat
  values
  ('Zuroke', 'starryfrog', 'Zuroke', 'boats and hoes', '2018-11-25 11:50:11');

  insert into F_chat
  values
  ('Zuroke', 'starryfrog', 'starryfrog', 'your mother', '2018-11-25 11:50:21');

  insert into F_chat
  values
  ('Zuroke', 'starryfrog', 'Zuroke', 'I love you and you are the best
  girlfriend in the whole world', '2018-11-25 11:50:31');

  insert into F_chat
  values
  ('Zuroke', 'starryfrog', 'starryfrog', 'In the words of Hans Solo:
  I know.', '2018-11-25 11:50:41');

  insert into F_chat
    values
    ('Zuroke', 'Stoick', 'Stoick', 'I suck', '2018-11-25 10:10:11');

  insert into F_chat
    values
    ('Zuroke', 'Stoick', 'Zuroke', 'of course you do nub', '2018-11-25 10:11:05');

  insert into F_chat
    values
    ('Zuroke', 'Bitandia', 'Zuroke', 'hi', '2018-11-25 11:11:11');

  insert into F_chat
    values
    ('Zuroke', 'Bitandia', 'Bitandia', 'go away', '2018-11-25 12:12:12');

-- C_chat table
-- ===========================================================================

insert into C_chat
values
('Zuroke', 'Voldemorts Army', 'its tearing', '2018-11-25 11:51:01');

insert into C_chat
values
('Stoick', 'Voldemorts Army', 'up my heart', '2018-11-25 11:52:01');

insert into C_chat
values
('Bitandia', 'Voldemorts Army', 'when Im', '2018-11-25 11:53:01');

insert into C_chat
values
('starryfrog', 'Voldemorts Army', 'with you', '2018-11-25 11:54:01');

-- Clan_event table
-- ===========================================================================

insert into Clan_event
values
('Voldemorts Army', 'Voldemort Dance Party', 'If you love the Imperius Curse
and you love to dance, you belong at this event!', '2018-11-30 12:00:00');

insert into Clan_event
values
('Ron Weaslies', 'Cat-tasia', 'BYOC', '2018-12-22 13:00:00');

insert into Clan_event
values
('Ravenclaws', 'WoW Party', 'WoW party, everyone is invited!', '2018-12-22 13:00:00');

insert into Clan_event
values
('Freyas', 'DOG-tasia', 'Bring treats', '2018-12-22 13:00:00');


-- Clan_announcement table
-- ===========================================================================

insert into Clan_announcement
values
('Ravenclaws', 'Welcome to the Clan!', '2018-11-20 12:00:00');

insert into Clan_announcement
values
('Freyas', 'Freya welcomes you to the Clan.', '2018-11-21 12:00:00');

insert into Clan_announcement
values
('Voldemorts Army', 'Voldemort welcomes you to the Clan.', '2018-11-21 12:00:00');

insert into Clan_announcement
values
('Ron Weaslies', 'Ron welcomes you to the Clan.', '2018-11-21 12:00:00');

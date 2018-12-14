/*

NAME:          darkspear_design.sql
LAST MODIFIED: November 21, 2018
DESCRIPTION:   Table creation for the Darkspear database.

*/



/* ==========================================

Table: Player. This table contains the player's
       username, email, password, whether or not
       the player is competitive, and a 500
       character max bio for the player.
============================================= */

create database if not exists darkspear;

use darkspear;

drop table if exists Clan_announcement;
drop table if exists Clan_event;
drop table if exists C_chat;
drop table if exists F_chat;
drop table if exists Clan_games;
drop table if exists Plays_game;
drop table if exists Player_in_clan;
drop table if exists Clan_officer;
drop table if exists Game_platform;
drop table if exists Game;
drop table if exists Clan;
drop table if exists Player;

create table Player
(username       varchar(20),
 email          varchar(40),
 pswd       	varchar(20),
 comp_player	bit,
 bio            varchar(500),
 PRIMARY KEY(username)
);

 /* ==========================================

 Table: Clan. This table holds the clan's name,
        the leader's username,  the number of
        members, the maximum number of members
        for the clan, and a short bio for the
        clan (500 max characters).
 ============================================= */

create table Clan
(clan_name       varchar(25),
 leader_username varchar(20),
 member_count    integer,
 max_members     integer,
 bio             varchar(500),
 primary key(clan_name),
 foreign key(leader_username) references Player(username)
);

 /* ==========================================

 Table: Game. This table contains the game's name,
        genre, the maximum team size for the
        game, the rating of the game, whether
        the game is competitive or not, whether
        the game is player vs environment, and
        whether the game is player v player
 ============================================= */

 create table Game
 (game_name       varchar(25),
  genre           varchar(20),
  max_team_size   integer,
  rating          varchar(10),
  has_comp        bit,
  is_pve          bit,
  is_pvp          bit,
  primary key(game_name)
 );


/* ==========================================

 Table: Game_platform. This table contains
        the game's name and its platform.
 ============================================= */


 create table Game_platform
 (game_name       varchar(25),
  game_platform   varchar(20),
  primary key(game_name, game_platform),
  foreign key(game_name) references Game(game_name)
 );


/* ==========================================

Table: Player_in_clan. This contains the player's
       username, and their clan name.
============================================= */

create table Player_in_clan
(username       varchar(20),
 clan_name      varchar(25),
 primary key(username, clan_name),
 foreign key(username) references Player(username),
 foreign key(clan_name) references Clan(clan_name)
);

/* ==========================================

Table: Plays_game. This table contains the
       player's username, and the game name.
============================================= */

create table Plays_game
(username       varchar(20),
 game_name      varchar(25),
 primary key(username, game_name),
 foreign key(username) references Player(username),
 foreign key(game_name) references Game(game_name)
 );

 /* ==========================================

 Table: Clan_games. This table has the clan's
        name, the game's name, and the rank title.
 ============================================= */

create table Clan_games
(clan_name        varchar(25),
 game_name        varchar(25),
 rank_title       varchar(20),
 primary key(clan_name, game_name),
 foreign key(clan_name) references Clan(clan_name),
 foreign key(game_name) references Game(game_name)
);


/* ==========================================

Table: F_chat. This is the friend chat table.
       It contains the chat's ID number, the
       usernames of the two people in the chat,
       the message, and the time.
============================================= */

 create table F_chat
 (p1_username     varchar(20),
  p2_username     varchar(20),
  sender 		  varchar(20),
  message         varchar(500),
  msg_time        datetime DEFAULT CURRENT_TIMESTAMP,
  primary key(p1_username, p2_username, msg_time),
  foreign key(p1_username) references player(username),
  foreign key(p2_username) references player(username)
 );



  /* ==========================================

 Table: C_chat. This is the clan chat. It contains
        a chat id, poster username, clan name, the
        message, time and board.
 ============================================= */

 create table C_chat
 (poster_username varchar(20),
  clan_name       varchar(25),
  message         varchar(500),
  msg_time        datetime DEFAULT CURRENT_TIMESTAMP,
  primary key(poster_username, msg_time),
  foreign key(poster_username) references player(username),
  foreign key(clan_name) references Clan(clan_name)
 );


 /* ==========================================

 Table: Clan_event. This table has the event id,
        the clan's name, the event name, a
        description of the clan event, and the
        date of the clan event.
 ============================================= */

 create table Clan_event
 (clan_name       varchar(25),
  event_name      varchar(25),
  description     varchar(500),
  event_date      datetime DEFAULT CURRENT_TIMESTAMP,
  primary key(clan_name, event_name),
  foreign key(clan_name) references Clan(clan_name)
 );


  /* ==========================================

 Table: Clan_announcement. This table has an
        announcement id for the announcement,
        the clan's name, the announcement,
        and the date of the announcement.
 ============================================= */

 create table Clan_announcement
 (clan_name             varchar(25),
  announcement          varchar(500),
  announcement_time     datetime DEFAULT CURRENT_TIMESTAMP,
  primary key(clan_name, announcement_time),
  foreign key(clan_name) references Clan(clan_name)
 );

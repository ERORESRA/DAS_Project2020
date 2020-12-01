use Music_Database;
create table Artist(
id int PRIMARY KEY AUTO_INCREMENT,
name text,
genre text,
image_link text,
bio text
);
create table Album(
id int PRIMARY KEY AUTO_INCREMENT,
title text,
artist text,
genre text,
art text
);
create table Track(
id int PRIMARY KEY AUTO_INCREMENT,
number int,
title text,
artist text,
album text,
duration text
);

use Music_Database;
create table Artist(
id int primary key not null,
name text,
genre text,
image_link text,
bio text
);
create table Album(
id int primary key not null,
title text,
artist text,
genre text,
art text
);
create table Track(
number int,
title text,
artist text,
album text
);
